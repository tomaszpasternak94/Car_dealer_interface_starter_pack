import pytest

class TestParking:
    @pytest.fixture
    def audi(self):
        audi = Car('audi', 'a7', 69000)
        return audi

    @pytest.fixture
    def mercedes(self):
        mercedes = Car('mercedes', 'E-class', 20000)
        return mercedes

    @pytest.fixture
    def bentley(self):
        bentley = Car('Bentley', 'Continental GT', 400000)
        return bentley

    def test_create_parking(self):
        """ Test : 'Was the instance created correctly?' """
        parking = Parking()
        assert isinstance(parking, Parking)
        assert parking.car_dealer_cash == 100000
        assert parking.cars_amount == 0


