- lui 3, 250		# Load immediate value (250) 
- or 1,2,4
- lui 2,100
- lw    4,4,value		
- add  5,2,4   	# Add
- add 6,6,5	# Add
- sub 5,3,4   	# Subtract
- sw 2,3,Zero
value .fill 12
Zero .fill 0

