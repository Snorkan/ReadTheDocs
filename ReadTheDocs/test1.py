from main import inc

def fail():
    assert inc(3) == 5

def succeeds():
    assert inc(4) == 5