DUART   EQU      $C001  ;68681 base address
SRA     EQU      2
RBA     EQU      6
OPR_SET EQU      14*2        ;set bit command reg.
OPR_CLR EQU      15*2        ;clear bit cmd. reg.

        ORG      $8000
LOOP    MOVEA.L  #MESSAGE,A1
        BSR      PRINT
        TRAP     #14
        
PRINT   MOVE.B   D0,(A1)+
        ADD.B    D0,D1
        MOVEA.L  #DUART,A0
PRTCHR  MOVE.B   SRA(A0),D7
        ANDI.B   #1,D7
        BEQ      PRTCHR
        MOVE.B   RBA(A0),D0
        MOVE.B   D0,D1
        BSR      OUT
        CMPI     #113,D0
        BEQ      EXIT
        BRA      PRINT
EXIT    MOVE.B   #$FF,OPR_CLR(A0)
        RTS

OUT     MOVE.B   #$FF,OPR_CLR(A0)
        MOVE.B   D1,OPR_CLR(A0)
        MOVE.B   D1,OPR_SET(A0)
        CLR.L    D1
        RTS
        
MESSAGE DC.L     1
        END      LOOP


*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
