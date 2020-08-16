all: targ1 targ2 targ3 targ4 targ5

targ1:
	python -m pytest -k "not Fail" -v

targ2:
	python -m pytest -v test_functions.py::test_productNumbers

targ3:
	python -m pytest -v -m strings

targ4:
	python -m pytest -v -m numbers

targ5:
	python -m pytest -v --maxfail=2
