            ORG         $8000
START       LEA         $9022,SP
            MOVE.L      #$D0D0D0D0,D0
            MOVE.L      #$D1D1D1D1,D0
            MOVE.L      #$D2D2D2D2,D0
            LEA         $A0A0A0A0,A0
            PEA         X
            PEA         Y
            PEA         Z
            PEA         W
            JSR         Quad
            LEA         16(SP),SP
            TRAP        #14
        
Quad        MOVEM.L     D0-D2/A0,-(SP)
            MOVEA.L     32(SP),A0
            MOVE.W      (A0),D0
            MULS        D0,D0
            MULS        #5,D0
            MOVE.W      (A0),D1
            MULS        #4,D1
            MOVEA.L     28(SP),A0
            MOVE.W      (A0),D2
            MULS        D2,D1
            MOVEA.L     24(SP),A0
            MOVE.W      (A0),D2
            MULS        D2,D2
            SUB.W       D1,D0
            ADD.W       D2,D0
            MOVEA.L     20(SP),A0
            MOVE.W      D0,(A0)
            MOVEM.L     (SP)+,D0-D2/A0
            RTS
            
            ORG         $8500
X           DC.W        3
Y           DC.W        4
Z           DC.W        5
W           DS.W        1
            END         START







*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
