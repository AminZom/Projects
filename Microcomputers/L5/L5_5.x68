*L5_5.x68     

	ORG	$8000
START  	MOVE.W  num1,D0	  
	    MOVE.W	num2,D1
	    MOVE.W  num3,D2
	    CMP     d1,d0
	    BLT     ElseIf
	    CMP     d2,d0
	    BLT     ElseIf
	    MOVE.W  d0,d3
	    MOVE.W  d0,biggest
	    BRA     exit
ElseIf  CMP     d0,d1
	    BLT     else
	    CMP     d2,d1
	    BLT     else
	    MOVE.W  d1,d3
	    MOVE.W  d1,biggest
	    BRA     exit
Else    MOVE.W  d2,d3
        MOVE.W  d2,biggest
exit    TRAP	#14

	ORG	$9000		
num1	DC.W	$A
num2	DC.W	5
num3	DC.W	$F
biggest DS.W    1
	END	START




*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
