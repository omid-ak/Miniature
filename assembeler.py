"""
this ia a assembeller known as Miniature.
It's Instructions has 3 kinds of format: R type, I type and J type
"""


# class R_type:
#     def __init__(opcode, rs, rt, rd, shamat, funcode):
#         self.operation_code = opcode                        #6bits
#         self.register_source_1_address = rs                 #5bits
#         self.register_source_2_address = rt                 #5bits
#         self.register_destination_address = rd              #5bits
#         self.shift_ammount = shamat #for shift instructions #6bits
#         pass
# class I_type(R_type):
#     def __init__(opcode, rs, rt, immediate):
#         self.operation_code = opcode                        #
#         self.register_source_1_address = rs                 #
#         self.register_source_2_address = rt                 #
#         self.Immediate = immediate                          #
#         pass
# class J_type(R_type):
#     def __init__(opcode,address):
#         self.operation_code = opcode                        #
#         self.ADDRESS = address                              #
#         pass
import re
file_name=input('Enter the filename.asm\n')
fn=open(file_name,'r').readlines()
pc = 0
line_counter=0

############## Calculation R type Instruction ######################
def R_Instruction(rd, rt, rs, op):
    res = ''
    res = res.zfill(12) + rd + rt + rs + op + res.zfill(4)
    return res
############## Calculation I type Instruction ######################
def I_Instruction(offset, rt, rs, op):
    res = ''
    res = offset + rt + rs + op + res.zfill(4)
    return res

############## Calculation J Type Instruction ######################
def J_Instruction(target, op):
    res  = ''
    res = target + res.zfill(8) + opcode + res.zfill(4)
    return res

############## a Function to convert decimal numbers to Binary #############################
def Convertor_to_binary(number):
    res = bin(int(number)).lstrip('0b')
    return res
############## a function to convert decimal numbers to Hexadecimal #########################
def Convert_to_Hexa(number):
    res = hex(int(number)).lstrip('0x')
    return res

for l in fn:

#################### R Type Instructions ############################
    if 'add' in l:
        opcode = '0000'
        match  = re.search(r'.* add .*,*,*',str(l))
        argsls = match.group().split()
        rd = argsls[2]
        rt = argsls[3]
        rs = argsls[4]
        binary_code_address = R_Instruction(rd, rt, rs, opcode)
        pc += 1
        line_counter+=1
    elif 'sub' in l:
        opcode = '0001'
        match  = re.search(r'.* sub .*,.*,.*',str(l))
        argsls = match.group().split()
        rd = argsls[2]
        rt = argsls[3]
        rs = argsls[4]
        binary_code_address = R_Instruction(rd, rt, rs, opcode)
        pc += 1
        line_counter+=1
    elif 'slt' in l:
        opcode = '0010'
        match  = re.search(r'.* slt .*,.*,.*',str(l))
        argsls = match.group().split()              #L,slt,$rd,$rs,$rt  and ignore comments
        rd = argsls[2]
        rt = argsls[3]
        rs = argsls[4]
        binary_code_address = R_Instruction(rd, rt, rs, opcode)
        pc += 1
        line_counter+=1
    elif 'or' in l:
        opcode = '0011'
        match  = re.search(r'.* or .*,.*,.*',str(l))
        argsls = match.group().split()
        rd = argsls[2]
        rt = argsls[3]
        rs = argsls[4]
        binary_code_address = R_Instruction(rd, rt, rs, opcode)
        pc += 1
        line_counter+=1
    elif 'nand' in l:
        opcode = '0100'
        match  = re.search(r'.* nand .*,.*,.*',str(l))
        argsls = match.group().split()
        rd = argsls[2]
        rt = argsls[3]
        rs = argsls[4]
        binary_code_address = R_Instruction(rd, rt, rs, opcode)
        pc += 1
        line_counter+=1
####################### I Type Instructions ############################
    elif 'addi' in l:
        opcode = '0101'
        match  = re.search(r'.* addi .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: convert to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'slti' in l:
        opcode = '0110'
        match  = re.search(r'.* slti .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: convert to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'ori' in l:
        opcode = '0111'
        match  = re.search(r'.* ori .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: convert to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'lui' in l:
        opcode = '1000'
        match  = re.search(r'.* lui .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: convert to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'lw' in l:
        opcode = '1001'
        match  = re.search(r'.* lw .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: convert to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'sw' in l:
        opcode = '1010'
        match  = re.search(r'.* sw .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: convert to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'beq' in l:
        opcode = '1011'
        match  = re.search(r'.* beq .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: conver to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'jalr' in l:
        opcode = '1100'
        match  = re.search(r'.* jalr .*,.*,.*',str(l))
        argsls = match.group().split()
        #TODO: conver to binarycode and calculate...
        pc += 1
        line_counter+=1
############### J Type Instructions ##############################
    elif 'j' in l:
        opcode = '1101'
        match  = re.search(r'.* j .*',str(l))
        argsls = match.group().split()
        #TODO: convert to binarycode and calculate...
        pc += 1
        line_counter+=1
    elif 'halt' in l:
        opcode = '1110'
        pc += 1
        line_counter+=1
        exit(0)
############### Directive Instructions ############################
    elif '.fill' in l:
        pass
    elif '.space' in  l:
        pass
############## Denied Instructions #################################
    else:
        #return "miniature: %s : command not found..." % l
        exit(1)


#############################################################################################


#TODO:getiing all Labels in lainopcodees ->Done.
#TODO: Ignore Comments --> Done
#TODO: Directive Instructions : .Space and .fill
#TODO: Hanlde Errors in Instructions and invalid instruction,Labels and offsets
#TODO: resolve an isuue in line 189
#TODO: calculation hexa for of addresses


