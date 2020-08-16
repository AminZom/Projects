            ORG         $8000
START       MOVE.W      #2,D2
            MOVE.W      #3,D3
            MOVE.W      #4,D4
            LEA         $9020,SP
            MOVE.W      D2,-(SP)
            MOVE.W      D3,-(SP)
            MOVE.W      D4,-(SP)
            JSR         solveQuad
            LEA         6(SP),SP
            TRAP        #14
        
solveQuad   MOVEM.L     D2-D4,-(SP)
            MOVE.W      20(SP),D2
            MULS        D2,D2
            MULS        #5,D2
            MOVE.W      20(SP),D3
            MULS        #2,D3
            MOVE.W      18(SP),D4
            MULS        D4,D3
            MOVE.W      16(SP),D4
            MULS        D4,D4
            SUB.W       D3,D2
            ADD.W       D4,D2
            MOVE.W      D2,D1
            MOVEM.L     (SP)+,D2-D4
            RTS
            END         START






*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
