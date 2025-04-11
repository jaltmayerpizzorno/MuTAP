from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False




def test():
    assert below_zero([10, -20, 10, -5]) == True
    assert below_zero([10, 5, -5, 0]) == False
    assert below_zero([-5, -10, 20]) == True
    assert below_zero([10, 20, -30]) == False
    assert below_zero([0, 0, 0]) == False
    assert below_zero([-1]) == True
