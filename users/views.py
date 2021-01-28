from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    CustomUserSerializer, EmailVerificationSerializer, LoginSerializer,ResendEmailSerializer,
    ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .utils import Util
# from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import Customers as User
import jwt
from django.conf import settings
import os


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format="json"):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                new_user = User.objects.get(email=json['email'])
                token = RefreshToken.for_user(user).access_token

                current_site = "sparklehood.web.app"
                relativeLink = "/verifyemail/"
                absurl = 'https://'+current_site+relativeLink+str(token)
                email_body = "Hi " + new_user.user_name + \
                    " Use the Link below to verify your email \n" + absurl
                data = {'email_body': email_body, 'to_email': new_user.email,
                        'email_subject': 'Verify Your Email'}
                Util.send_email(data)

                return Response(json, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])

            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({'email': 'Successfully Activated'},  status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as e:
            return Response(
                {"error": 'Activation Link Expired'},
                status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response(
                {"error": 'Invalid Token'},
                status=status.HTTP_400_BAD_REQUEST)



class ResendEmail(APIView):
    permission_classes = [AllowAny]

    def post(self,request,format="json"):
        serializer = ResendEmailSerializer(data=request.data)

        if serializer.is_valid():
            json = serializer.data
            user = User.objects.get(email=json['email'])

            if user.is_active:
                return Response({"msg":"You account is already activated"}, status=status.HTTP_200_OK)
            
            token = RefreshToken.for_user(user).access_token

            current_site = "sparklehood.web.app"
            relativeLink = "/verifyemail/"
            absurl = 'https://'+current_site+relativeLink+str(token)
            email_body = "Hi " + user.user_name + \
                " Use the Link below to verify your email \n" + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Verify Your Email'}
            Util.send_email(data)

            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))

            token = PasswordResetTokenGenerator().make_token(user)
            # current_site = get_current_site(
            #    request=request).domain
            relativeLink = "https://sparklehood.web.app/reset-password?token="+token+"&uidb="+uidb64

            absurl = relativeLink
            email_body = 'Hello,' + user.user_name + '\n Use link below to reset your password  \n' + \
                absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response(
            {'success': 'We have sent you a link to reset your password'},
            status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request,uidb64,token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error':'Token valid is false please try again'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"msg":'Token validation done','token':token,"uidb64":uidb64})

        except DjangoUnicodeDecodeError:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return Response({'error':'Token valid is false please try again'}, status=status.HTTP_400_BAD_REQUEST)

            except UnboundLocalError:
                return Response(
                    {'error': 'Token is not valid, please request a new one'},
                    status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {'success': True, 'message': 'Password reset success'},
            status=status.HTTP_200_OK)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
