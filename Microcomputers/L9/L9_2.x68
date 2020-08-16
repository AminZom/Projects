            ORG         $8000
START       MOVE.L      #1234,D3
            TRAP        #5
            TRAP        #14
            END         START
        
            ORG         $8024
            JMP         T5
            
            ORG         $9000
T5          LEA         $9010,SP
            MOVE.L      
            RTE
            
            ORG         $A000
T7          ANDI        #$DFFF,(SP)
            RTE










*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
