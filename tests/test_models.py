class TestModels:
    def setUpTestData(self):
        print("Run once to set up")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        assert 1 + 1 == 2
