import pytest
import yaml

from python.clac import Calc


class TestCalc:
    test_data = [1, 1]

    @pytest.fixture()
    def test_calc_qianzhi(self):
        self.calc = Calc()

    @pytest.mark.parametrize(['a', 'b', 'c'],
                             yaml.safe_load(open("/Users/v_liuzhen01/PycharmProjects/mywork12/data/calcdataadd.yaml"),
                                            ))
    def test_add(self, test_calc_qianzhi, a, b, c):
        o = self.calc.add(a, b)
        assert o == c

    @pytest.mark.parametrize(['a', 'b', 'c'],
                             yaml.safe_load(open("/Users/v_liuzhen01/PycharmProjects/mywork12/data/calcdata.yaml"),
                                            ))
    def test_div(self, test_calc_qianzhi, a, b, c):
        if b == 0:
            print("b等于0，不符合除法规则")
        else:
            o = self.calc.div(a, b)
            assert o == c


if __name__ == '__main__':
    pytest.main('-v', 'test_calccase.py')
