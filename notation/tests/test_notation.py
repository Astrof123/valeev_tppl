import pytest
from notation import notation


class TestNotation:
    def test_work_example(self):
        assert notation("+ 2 2") == "2 + 2"
        assert notation("+ - 13 4 55") == "13 - 4 + 55"
        assert notation("+ 2 * 2 - 2 1") == "2 + 2 * (2 - 1)"
        assert notation("+ + 10 20 30") == "10 + 20 + 30"
        assert notation("/ + 3 10 * + 2 3 - 3 5") == "(3 + 10) / ((2 + 3) * (3 - 5))"

    def test_my_function_raises_error(self):
        with pytest.raises(SyntaxError) as error:
            notation(" - - 1 2")

