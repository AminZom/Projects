*L3_5: Evaluate


	ORG 	$8000
START	MOVE.B	$9003,D0
	EXT.W	D0
	MULS	$9001,D0
	MOVE.w	$9002,D1
	DIVS	#3,D1
	ADD	D0,D1
	TRAP    #14

	ORG	$9000
	DS.L	1
	DC.W	$2
	DC.W	$2
	DC.B	$3
	END	START



*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
