
def inc(x):
    return x + 1


def test_fail():
    assert inc(3) == 5

def test_succeeds():
    assert inc(4) == 5