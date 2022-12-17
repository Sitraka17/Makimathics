def calculate_limits(function, limit_type, limit_point):
    # Use the sympy library to symbolically evaluate the limit
    from sympy import symbols, Limit
    x = symbols('x')
    result = Limit(function, x, limit_point, limit_type).doit()
    return result
