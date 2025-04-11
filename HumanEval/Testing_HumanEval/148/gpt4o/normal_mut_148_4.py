def bf(planet1, planet2):
    
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1 : planet1_index])



def test():
        assert bf("Earth", "Jupiter") == ("Mars",)
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mars", "Mars") == ()
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Jupiter", "Mars") == ()
    assert bf("Venus", "Venus") == ()  # new test case to check for same planet names
    assert bf("Mercury", "Venus") == ("Venus",)  # new test case to check for adjacent planets
