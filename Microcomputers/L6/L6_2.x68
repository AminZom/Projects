  	    ORG		$8000
START   LEA     STRING1,A0
        LEA     STRING2,A1
        MOVE.B  #$FF,D0
DO      MOVE.L  (A0)+,D1
        MOVE.L  (A1)+,D2
        CMP.L   D1,D2
        BEQ     WHILE
        MOVE.B  #$00,D0
WHILE   CMPI.L  #$0D,D1
        BEQ     EXIT
        CMPI.B  #$FF,D0
        BEQ     DO
EXIT    TRAP    #14
        
	    ORG	    $9000
STRING1 DC.L    'hello',$D
STRING2 DC.L    'hello',$D
	    END	    START	

*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
