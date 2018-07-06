from enum import IntEnum, unique


''' Pin out for current raspberry pi. Config the GPIO appropriately  
                     3V3  (1) (2)  5V    
                   GPIO2  (3) (4)  5V    
                   GPIO3  (5) (6)  GND   
                   GPIO4  (7) (8)  GPIO14
                     GND  (9) (10) GPIO15
                  GPIO17 (11) (12) GPIO18
                  GPIO27 (13) (14) GND   
                  GPIO22 (15) (16) GPIO23
                     3V3 (17) (18) GPIO24
                  GPIO10 (19) (20) GND   
                   GPIO9 (21) (22) GPIO25
                  GPIO11 (23) (24) GPIO8 
                     GND (25) (26) GPIO7 
                   GPIO0 (27) (28) GPIO1 
                   GPIO5 (29) (30) GND   
                   GPIO6 (31) (32) GPIO12
                  GPIO13 (33) (34) GND   
                  GPIO19 (35) (36) GPIO16
                  GPIO26 (37) (38) GPIO20
                     GND (39) (40) GPIO21

		,--------------------------------.
		| oooooooooooooooooooo J8     +====
		| 1ooooooooooooooooooo        | USB
		|                             +====
		|      Pi Model 3B V1.2          |
		|      +----+                 +====
		| |D|  |SoC |                 | USB
		| |S|  |    |                 +====
		| |I|  +----+                    |
		|                   |C|     +======
		|                   |S|     |   Net
		| pwr        |HDMI| |I||A|  +======
		`-| |--------|    |----|V|-------'           '''


@unique
class gpio_config(IntEnum):
	
	pin_3V3_1 	 = 1 
	pin_5V_1  	 = 2
	gpio_2  	 = 3 
	pin_5V_2   	 = 4
	gpio_3  	 = 5 
	gnd_1	  	 = 6
	stepper_1_red    = 7
	gpio_14 	 = 8
	gnd_2		 = 9
	gpio_15		 = 10
	stepper_1_green  = 11
	gpio_18		 = 12
	stepper_1_blue   = 13
	gnd_3 		 = 14
	stepper_1_black  = 15
	gpio_23 	 = 16
	pin_3V3_2 	 = 17
	gpio_24 	 = 18
	gpio_10		 = 19
	gnd_4 		 = 20
	gpio_9 		 = 21
	gpio_25		 = 22
	gpio_11 	 = 23
	gpio_8 		 = 24
	gnd_5 		 = 25
	gpio_7 		 = 26
	gpio_0 	 	 = 27
	gpio_1		 = 28
	gpio_5 		 = 29
	gnd_6 		 = 30
	gpio_6 		 = 31
	gpio_12 	 = 32
	gpio_13 	 = 33
	gnd_7 		 = 34
	gpio_19		 = 35
	gpio_16		 = 36
	gpio_26		 = 37
	gpio_20 	 = 38
	gnd_8		 = 39
	gpio_21 	 = 40	
