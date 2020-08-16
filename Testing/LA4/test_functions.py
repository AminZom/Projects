##name: Patrick Di Salvo
##Date: November 1st 2nd 2019


import functions

##This function defintion is complete, use it as a guideline for completing
##the rest of the functio defintions
@pytest.mark.numbers
def test_addNumbers():
    assert functions.add(2, 3) == 5


##Complete this function
@pytest.mark.numbers
def test_productNumbers():
    assert functions.product(2, 3) == 6


##Complete this function

def test_addNumbersFail():
    assert functions.add(2, 3) == 9
    
##Complete this function

def test_productNumbersFail():
    assert functions.product(2, 3) == 9
    
##Complete this function

@pytest.mark.strings
def test_addStrings():
    assert functions.add("Mary ", "Lou") == "Mary Lou"
    
##Complete this function

@pytest.mark.strings
def test_productStrings():
    assert functions.product("Mary ", 3) == "Mary Mary Mary "
    
##Complete this function

def test_subtractNumbers():
    assert functions.subtract(6, 4) == 2
    
##Complete this function such that it will be skipped when running the test

@pytest.mark.skip
def test_skip():
	##pytest.skip("We want to skip this test")
    assert functions.subtract(9, 3) == 6

