import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    'square_coefficient,linear_coefficient,const_coefficient,expected_result',
    [
        (15.6, 12.3, 15.6, (None, None)),
        (4.3, 11.3, 3,  (-2.3282509550950174, -0.2996560216491692)),
        (0, 12.3, 15.6, (-1.268292682926829, None)),
        (0, 0, 15.6, (None, None)),
        (4, 11, 3, (-2.4430004681646915, -0.3069995318353087)),
        (0.02, 0.03, 0.01, (-0.9999999999999998, -0.5000000000000001))

    ]
)
def test__two_square_equation__return_solve_square_equation_with_different_data(square_coefficient, linear_coefficient, const_coefficient, expected_result):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_result
