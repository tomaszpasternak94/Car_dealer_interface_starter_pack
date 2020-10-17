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


