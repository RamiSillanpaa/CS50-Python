from bank import value

def test_hello():
    assert value("hello") == 0
    
def test_h():
    assert value("Hi") == 20
    
def test_bonjour():
    assert value("bonjour") == 100