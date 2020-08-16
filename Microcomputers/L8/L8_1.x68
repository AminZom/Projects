            ORG         $8000
START       MOVE.W      #2,D0
            LEA         $9010,SP
            MOVE.W      D0,-(SP)
            JSR         solveQuad
            LEA         2(SP),SP
            TRAP        #14
        
solveQuad   MOVE.W      4(SP),D1
            MULS        D1,D1
            MULS        #5,D1
            MOVE.W      4(SP),D2
            MULS        #2,D2
            SUB.W       D2,D1
            ADD.W       #6,D1
            RTS
            END         START





*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
