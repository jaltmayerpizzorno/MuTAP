def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
   return int(round(a ** (1.0 * 3))) ** 3 == a
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a
