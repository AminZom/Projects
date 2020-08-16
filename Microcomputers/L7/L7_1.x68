  	    ORG		$8000
START	MOVE.W  #30,D0
        MOVE.W  #25,D1
        CMPI.W  #1,D1
        BNE     LOOP
        ADD.W   D0,D2
        BRA     EXIT
LOOP    LSR.W   #1,D1
        BCC     MULT
        ADD.W   D0,D2
MULT    LSL.W   #1,D0
        CMPI.W  #1,D1
        BNE     LOOP
        ADD.W   D0,D2
EXIT    TRAP    #14
        END     START

*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
