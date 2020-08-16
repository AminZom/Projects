  	    ORG		$8000
START	LEA		MATRIX,A0
OUTLOOP CMPI.B  #2,D0
        BGT     EXIT
        MOVE.L  D0,D1
        ADD.B   #1,D1
INLOOP  CMPI.B  #3,D1
        BGT     ITERI
        MOVE.B  D0,D3
        MULS    #4,D3
        ADD.L   D1,D3
        MOVE.L  (A0,D3.L),D2
        MOVE.L  D1,D4
        MULS    #4,D4
        ADD.L   D0,D4
        MOVE.L  (A0,D4.L),(A0,D3.L)
        MOVE.L  D2,(A0,D4.L)
        ADD.L   #1,D1
        BRA     INLOOP
ITERI   ADD.L   #1,D0
        BRA     OUTLOOP
EXIT    TRAP    #14
        
	    ORG	    $9000
MATRIX  DC.L    1,2,3,4
        DC.L    5,6,7,8
        DC.L    9,10,11,12
        DC.L    13,14,15,16
	    END	    START	

*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
