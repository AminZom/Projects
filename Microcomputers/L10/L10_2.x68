DUART   EQU      $C001  ;68681 base address
SRA     EQU      2
TBA     EQU      6
CR      EQU      $D
LF      EQU      $A

        ORG      $8000
LOOP    MOVEA.L  #MESSAGE,A1
        BSR      PRINT
        BNE      LOOP
        TRAP     #14
        
PRINT   MOVE.B   (A1)+,D0
        BEQ      EXIT
        MOVEA.L  #DUART,A0
PRTCHR  MOVE.B   SRA(A0),D7
        ANDI.B   #4,D7
        BEQ      PRTCHR
        MOVE.B   D0,TBA(A0)
        BRA      PRINT
EXIT    RTS
        
MESSAGE DC.B     CR,LF,'This is so fun',0
        END      LOOP



*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
