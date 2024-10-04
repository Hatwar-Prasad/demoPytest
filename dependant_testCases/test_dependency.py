import pytest

class Test_dependcency:
    @pytest.mark.dependency
    def test_testCase1(self):
        print("test case 1")
        #assert  False

    @pytest.mark.dependency(depends=['Test_dependcency::test_testCase1'])
    def test_testCase2(self):
        print("test case 2")

    @pytest.mark.dependency()
    def test_addToCart_Product(self):
        print("Product is added into cart successfully")
        assert False

class Test_buyProduct:
    @pytest.mark.dependency(depends=['Test_dependcency::test_addToCart_Product'])
    def test_buy_product(self):
        print("product is ready to shipment")



