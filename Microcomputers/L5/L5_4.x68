*L5_4.x68     

	ORG	$8000
START  	MOVE.W  num1,D0	  
	    MOVE.W	num2,D1
	    MOVE.W  num3,D2
	    CMP     d1,d0
	    BLT     else2
	    CMP     d2,d0
	    BLT     else1
    	MOVE.W  d0,d3
    	MOVE.W  d0,biggest
    	BRA     exit
else1   MOVE.W  d2,d3
        MOVE.W  d2,biggest
        BRA     exit
else2   CMP     d2,d1
        BLT     else3
        MOVE.W  d1,d3
        MOVE.W  d1,biggest
        BRA     exit
else3   MOVE.W  d2,d3
        MOVE.W  d2,biggest
exit    TRAP	#14

	ORG	$9000		
num1	DC.W	1
num2	DC.W	7
num3	DC.W	4
biggest DS.W    1
	END	START



*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
