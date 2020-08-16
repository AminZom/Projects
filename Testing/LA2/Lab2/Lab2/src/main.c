

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "Calculator.h"
#include "TestCalculator.h"


/*
    In main, call driver multiple times. Once in which there are all successes and once for each test function such that each one will fail once.
*/

int main(int argc, char* argv[])
{
	driver(5.0, 1.0, 6.0, 1.5, 3.0, 2.0);
	driver(4.0, 1.0, 6.0, 1.5, 3.0, 2.0);
	driver(5.0, 2.0, 6.0, 1.5, 3.0, 2.0);
	driver(5.0, 1.0, 10.0, 1.5, 3.0, 2.0);
	driver(5.0, 1.0, 6.0, 2.5, 3.0, 2.0);

    return 0;
}
