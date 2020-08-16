*-----------------------------------------------------------
* Title      :
* Written by :
* Date       :
* Description:
*-----------------------------------------------------------
            ORG    $8500

T5          MOVE        #1234,D3
            MOVE        D3,-(SP)
            JSR         DISPLAY
            LEA         2(SP),SP
            RTE
            END         T5
            
DISPLAY     LINK        A6,#-4
            MOVE.L      D0,-(SP)
            CLR.L       D0
            MOVE.W      8(A6),D0
            DIVU        #10,D0
            MOVE.W      D0,-2(A6)
            SWAP        D0
            MOVE.W      D0,-4(A6)
            CMPI.W      #0,-2(A6)
            BEQ         BASE
            MOVE.W      -2(A6),-(SP)
            JSR         DISPLAY
            LEA         2(SP),SP
BASE        CLR.L       D0
            MOVE.W      -4(A6),D0
            ADD         #$30,D0
            UNLK        A6

*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
