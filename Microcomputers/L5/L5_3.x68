*L5_3.x68     

	ORG	$8000
START  	MOVE.B  hex,d0	  
	    MOVE.B  d0,d1
	    ADD.B   #$30,d1
	    MOVE.B  d1,d2
	    MOVE.B  d2,ascii
	    CMPI.B  #$39,d1
	    BLE     exit
	    ADD.B   #7,d2
	    MOVE.B  d2,ascii
exit    TRAP	#14

	ORG	$9000		
hex	    DC.B	$9
ascii	DS.B	1
	END	START






*~Font name~Courier New~
*~Font size~10~
*~Tab type~1~
*~Tab size~4~
