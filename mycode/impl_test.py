from . import impl

def test_f():
	assert impl.f(1, 2, 3) == 6
	assert impl.f(2, 4, 6) == 12

def test_h():
	assert impl.h(0) == 45.34, "this should fail"
	assert impl.h(0) == 0.0, "this should pass"
