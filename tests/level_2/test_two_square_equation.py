from functions.level_2.two_square_equation import solve_square_equation


def test__two_square_equation__discriminant_less_than_zero():
    square_coefficient = 15.6
    linear_coefficient = 12.3
    const_coefficient = 15.6

    test = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert test == (None, None)


def test__two_square_equation__discriminant_more_than_zero():
    square_coefficient = 4.3
    linear_coefficient = 11.3
    const_coefficient = 3

    test = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert test == (-2.3282509550950174, -0.2996560216491692)


def test__two_square_equation__square_coefficient_equal_zero():
    square_coefficient = 0
    linear_coefficient = 12.3
    const_coefficient = 15.6

    test = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert test == (-1.268292682926829, None)


def test__two_square_equation__square_coefficient_equal_zero_and_linear_coefficient_equal_zero():
    square_coefficient = 0
    linear_coefficient = 0
    const_coefficient = 15.6

    test = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert test == (None, None)


def test__two_square_equation__discriminant_more_than_zero_all_digits_are_int():
    square_coefficient = 4
    linear_coefficient = 11
    const_coefficient = 3

    test = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert test == (-2.4430004681646915, -0.3069995318353087)


def test__two_square_equation__discriminant_more_than_zero_little_digits():
    square_coefficient = 0.02
    linear_coefficient = 0.03
    const_coefficient = 0.01

    test = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert test == (-0.9999999999999998, -0.5000000000000001)