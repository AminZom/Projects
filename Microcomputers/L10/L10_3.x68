DUART   EQU      $C001  ;68681 base address
SRA     EQU      2
RBA     EQU      6

        ORG      $8000
LOOP    MOVEA.L  #MESSAGE,A1
        BSR      PRINT
        TRAP     #14
        
PRINT   MOVE.B   D0,(A1)+
        MOVEA.L  #DUART,A0
PRTCHR  MOVE.B   SRA(A0),D7
        ANDI.B   #1,D7
        BEQ      PRTCHR
        MOVE.B   RBA(A0),D0
        CMPI     #$D,D0
        BEQ      EXIT
        BRA      PRINT
EXIT    RTS
        
MESSAGE DC.L     1
        END      LOOP

*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
