def car_race_collision(n: int):
    
    return n**2




def test():
    assert car_race_collision(0) == 0
    assert car_race_collision(1) == 1
    assert car_race_collision(2) == 4
    assert car_race_collision(3) == 9
    assert car_race_collision(4) == 16
    assert car_race_collision(10) == 100
    assert car_race_collision(-1) == 1
    assert car_race_collision(-2) == 4
