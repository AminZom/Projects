*L3_5: Evaluate


	ORG 	$8000
START	MOVE.B	WVALUE+4,D0
	EXT.W	D0
	MULS	WVALUE,D0
	MOVE.w	WVALUE+2,D1
	DIVS	#3,D1
	ADD	D0,D1
	TRAP    #14

	ORG	$9000
WVALUE  DC.W	$2
	    DC.W	$2
	    DC.B	$3
	    END	START





*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
