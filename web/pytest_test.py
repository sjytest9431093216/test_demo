import sys
#print(sys.path)
sys.path.append('..')
from web.calc import Calc
import pytest


class TestCalc:
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result


    def test_div(self):
        self.calc = Calc()
        result = self.calc.div(2, 2)
        print(result)
        assert 1 == result


if __name__ == '__main__':
    pytest.main(['-vs','pytest_test::TestCalc::test_div'])
