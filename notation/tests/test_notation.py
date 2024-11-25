import pytest
from notation import Notation

@pytest.fixture
def notate():
    return Notation()


class TestNotation:
    def test_work_example(self, notate):
        assert notate.notation2("+ 2 2") == "2 + 2"
        assert notate.notation2("+ - 13 4 55") == "13 - 4 + 55"
        assert notate.notation2("+ 2 * 2 - 2 1") == "2 + 2 * (2 - 1)"
        assert notate.notation2("+ + 10 20 30") == "10 + 20 + 30"
        assert notate.notation2("/ + 3 10 * + 2 3 - 3 5") == "(3 + 10) / ((2 + 3) * (3 - 5))"

    def test_my_function_raises_error(self, notate):
        with pytest.raises(SyntaxError) as error:
            notate.notation2(" - - 1 2")

