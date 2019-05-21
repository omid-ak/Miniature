- lw 1,0,five
- lw 2,1,2
- lw 3,1,4
start add 1,1,2
- beeq 0,1,done  # incorrect opcode
- j start
done halt
five .fill 5
neg1 .fill -1
stAddr .fill start