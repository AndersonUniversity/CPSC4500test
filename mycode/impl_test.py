
def test_f():
	assert f(1, 2, 3) == 6
	assert f(2, 4, 6) == 12

def test_h():
	assert h(0) == 45.34, "this should fail"
	assert h(0) == 0.0, "this should pass"
