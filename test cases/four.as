Start addi 10,0,3
-     addi 6,6,1
-     slti 8,7,0
-     slti 9,7,10
-     or 1,8,9
-     and 3,3,2
-     lw 1,2,L10
-     beq 2,3,10000000057800000000000000000  # offset over 16 bit
L10  .fill 10

