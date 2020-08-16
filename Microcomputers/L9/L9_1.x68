            ORG         $802A
            JMP         T6
            JMP         T7
            
            ORG         $9000
T6          ORI.L       #%0010000000000000,(SP)
            RTE
            
            ORG         $9020
T7          ANDI.L      #%1101111111111111,(SP)
            RTE

            ORG         $A000
START       TRAP        #7
            TRAP        #14
            END         START








*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
