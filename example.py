def add(a, b):
	return a+b

def subtract(a,b):
	return a-b


def test_add():
	assert add(2, 3) == 5
	assert add("space", "ship") == "spaceship"

def test_1():
	assert 1==1
	
def test_subtract():
	assert subtract(1,1) == 0
	assert subtract(0,0) == 1
	assert subtract(2,1) == 1
