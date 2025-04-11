def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)



def test():
        assert do_algebra(['+', '-'], [1, 2, 3]) == 0  # 1 + 2 - 3 = 0
    assert do_algebra(['*', '/'], [4, 5, 2]) == 10  # 4 * 5 / 2 = 10
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4]) == 3  # 1 + 2 * 3 - 4 = 3
    assert do_algebra(['-', '+'], [10, 3, 4]) == 11  # 10 - 3 + 4 = 11
    assert do_algebra(['/', '+'], [20, 5, 3]) == 7  # 20 / 5 + 3 = 7
    assert do_algebra(['//', '**'], [8, 2, 3]) == 1  # 8 // 2 ** 3 = 1
