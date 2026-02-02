from src.decorators import my_function


def test_my_function_success() -> None:
    assert my_function(6, 2) == 3.0


def test_my_function_division_by_zero() -> None:
    result = my_function(6, 0)
    assert result == "Inputs: (6, 0), {}"
