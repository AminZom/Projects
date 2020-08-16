            ORG         $8000
START       LEA         $9020,SP
            LEA         $A0A0A0A0,A0
            LEA         $A1A1A1A1,A1
            MOVE.L      #$D0D0D0D0,D0
            MOVE.L      #$D1D1D1D1,D1
            MOVE.W      X,-(SP)
            MOVE.W      Y,-(SP)
            PEA         Z
            JSR         Square
            LEA         8(SP),SP
            TRAP        #14
        
Square      LINK        A0,#-6
            MOVEM.L     D0-D1/A1,-(SP)
            MOVE.W      14(A0),D0
            MULS        D0,D0
            MOVE.W      D0,-2(A0)
            MOVE.W      12(A0),D1
            MULS        D1,D1
            MOVE.W      D1,-4(A0)
            MOVE.W      14(A0),D0
            MOVE.W      12(A0),D1
            MULS        D1,D0
            MULS        #2,D0
            MOVE.W      D0,-6(A0)
            MOVE.W      -2(A0),D0
            ADD.W       -4(A0),D0
            ADD.W       -6(A0),D0
            MOVEA.L     8(A0),A1
            MOVE.W      D0,(A1)
            MOVEM       (SP)+,D0-D1/A1
            UNLK        A0
            RTS
            
            ORG         $8500
X           DC.W        2
Y           DC.W        3
Z           DS.W        1
            END         START








*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
