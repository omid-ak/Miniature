"""
this ia a assembeller known as Miniature.
It's Instructions has 3 kinds of format: R type, I type and J type
"""

import re

I_file_name = input('Enter the path and name of Input file in form of : filename.as\n')
O_file_name = input('Enter the path and name of Output file in form of : program.mc\n')
fn = open(I_file_name, 'r')
fw = open(O_file_name, 'a')
pc = 0
line_counter = 0
command_list = ['add', 'sub', 'slt', 'or', 'nand', 'addi', 'ori', ' slti', 'lui', 'lw', 'sw', 'beq', 'jalr', 'j', '.space', '.fill']
Label_list = []
############## Calculation R type Instruction ######################
def R_Instruction(rd, rt, rs, op):
    res = ''
    res = res.zfill(12) + rd.zfill(4) + rt.zfill(4) + rs.zfill(4) + op.zfill(4) + res.zfill(4)
    return res
############## Calculation I type Instruction ######################
def I_Instruction(offset, rt, rs, op):
    res = ''
    res = offset.zfill(16) + rt.zfill(4) + rs.zfill(4) + op.zfill(4) + res.zfill(4)
    return res

############## Calculation J Type Instruction ######################
def J_Instruction(target, op):
    res  = ''
    res = target.zfill(16) + res.zfill(8) + op.zfill(4) + res.zfill(4)
    return res

############## a Function to convert decimal numbers to Binary #############################
def Convertor_to_binary(number):
    res = bin(int(number)).lstrip('0b')
    return res
############## a function to convert decimal numbers to Hexadecimal #########################
def Convert_to_Hexa(number):
    res = hex(int(number))
    return res
file_ls = fn.read().splitlines()
for l in file_ls:

#################### R Type Instructions ############################
    if 'add' in l:
        opcode_0 = '0000'
        match_0  = re.search(r'.* add .*,*,*', str(l))
        argsls_0 = match_0.group().split()
        argsls_0[2] = argsls_0[2].split(',')
        Label_list.append(argsls_0[0])
        rd_0 = Convertor_to_binary(int(argsls_0[2][0]))
        rt_0 = Convertor_to_binary(int(argsls_0[2][1]))
        rs_0 = Convertor_to_binary(int(argsls_0[2][2]))
        binary_code_address_0 = R_Instruction(rd_0, rt_0, rs_0, opcode_0)
        decima_code_address_0 = int(binary_code_address_0,2)
        hexa_code_address_0   = Convert_to_Hexa(decima_code_address_0)
        result_str_0 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_0, decima_code_address_0, hexa_code_address_0)
        fw.write(result_str_0)
        pc += 1
        line_counter += 1
    elif 'sub' in l:
        opcode_1 = '0001'
        match_1  = re.search(r'.* sub .*,.*,.*', str(l))
        argsls_1 = match_1.group().split()
        argsls_1[2] = argsls_1[2].split(',')
        Label_list.append(argsls_1[0])
        rd_1 = Convertor_to_binary(int(argsls_1[2][0]))
        rt_1 = Convertor_to_binary(int(argsls_1[2][1]))
        rs_1 = Convertor_to_binary(int(argsls_1[2][2]))
        binary_code_address_1 = R_Instruction(rd_1, rt_1, rs_1, opcode_1)
        decima_code_address_1 = int(binary_code_address_1, 2)
        hexa_code_address_1 = Convert_to_Hexa(decima_code_address_1)
        result_str_1 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_1, decima_code_address_1, hexa_code_address_1)
        fw.write(result_str_1)
        pc += 1
        line_counter += 1
    elif 'slt' in l:
        opcode_2 = '0010'
        match_2  = re.search(r'.* slt .*,.*,.*', str(l))
        argsls_2 = match_2.group().split()              #L,slt,$rd,$rs,$rt  and ignore comments
        argsls_2[2] = argsls_2[2].split(',')
        Label_list.append(argsls_2[0])
        rd_2 = Convertor_to_binary(int(argsls_2[2][0]))
        rt_2 = Convertor_to_binary(int(argsls_2[2][1]))
        rs_2 = Convertor_to_binary(int(argsls_2[2][2]))
        binary_code_address_2 = R_Instruction(rd_2, rt_2, rs_2, opcode_2)
        decima_code_address_2 = int(binary_code_address_2, 2)
        hexa_code_address_2   = Convert_to_Hexa(decima_code_address_2)
        result_str_2 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_2, decima_code_address_2, hexa_code_address_2)
        fw.write(result_str_2)
        pc += 1
        line_counter += 1
    elif 'or' in l:
        opcode_3 = '0011'
        match_3  = re.search(r'.* or .*,.*,.*', str(l))
        argsls_3 = match_3.group().split()
        argsls_3[2] = argsls_3[2].split(',')
        Label_list.append(argsls_3[0])
        rd_3 = Convertor_to_binary(int(argsls_3[2][0]))
        rt_3 = Convertor_to_binary(int(argsls_3[2][1]))
        rs_3 = Convertor_to_binary(int(argsls_3[2][2]))
        binary_code_address_3 = R_Instruction(rd_3, rt_3, rs_3, opcode_3)
        decima_code_address_3 = int(binary_code_address_3, 2)
        hexa_code_address_3 = Convert_to_Hexa(decima_code_address_3)
        result_str_3 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_3, decima_code_address_3, hexa_code_address_3)
        fw.write(result_str_3)
        pc += 1
        line_counter += 1
    elif 'nand' in l:
        opcode_4 = '0100'
        match_4  = re.search(r'.* nand .*,.*,.*', str(l))
        argsls_4 = match_4.group().split()
        argsls_4[2] = argsls_4[2].split(',')
        Label_list.append(argsls_4[0])
        rd_4 = Convertor_to_binary(int(argsls_4[2][0]))
        rt_4 = Convertor_to_binary(int(argsls_4[2][1]))
        rs_4 = Convertor_to_binary(int(argsls_4[2][2]))
        binary_code_address_4 = R_Instruction(rd_4, rt_4, rs_4, opcode_4)
        decima_code_address_4 = int(binary_code_address_4, 2)
        hexa_code_address_4 = Convert_to_Hexa(decima_code_address_4)
        result_str_4 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_4, decima_code_address_4, hexa_code_address_4)
        fw.write(result_str_4)
        pc += 1
        line_counter += 1
####################### I Type Instructions ############################
    elif 'addi' in l:
        opcode_5 = '0101'
        match_5  = re.search(r'.* addi .*,.*,.*', str(l))
        argsls_5 = match_5.group().split()
        argsls_5[2] = argsls_5[2].split(',')
        Label_list.append(argsls_5[0])
        rt_5  = Convertor_to_binary(int(argsls_5[2][0]))
        rs_5  = Convertor_to_binary(int(argsls_5[2][1]))
        imm_5 = Convertor_to_binary(int(argsls_5[2][2]))
        binary_code_address_5 = I_Instruction(imm_5, rt_5, rs_5, opcode_5)
        decima_code_address_5 = int(binary_code_address_5, 2)
        hexa_code_address_5   = Convert_to_Hexa(decima_code_address_5)
        result_str_5 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_5, decima_code_address_5, hexa_code_address_5)
        fw.write(result_str_5)
        pc += 1
        line_counter += 1
    elif 'slti' in l:
        opcode_6 = '0110'
        match_6  = re.search(r'.* slti .*,.*,.*', str(l))
        argsls_6 = match_6.group().split()
        argsls_6[2] = argsls_6[2].split(',')
        Label_list.append(argsls_6[0])
        rt_6 = Convertor_to_binary(int(argsls_6[2][0]))
        rs_6 = Convertor_to_binary(int(argsls_6[2][1]))
        imm_6 = Convertor_to_binary(int(argsls_6[2][2]))
        binary_code_address_6 = I_Instruction(imm_6, rt_6, rs_6, opcode_6)
        decima_code_address_6 = int(binary_code_address_6, 2)
        hexa_code_address_6 = Convert_to_Hexa(decima_code_address_6)
        result_str_6 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_6, decima_code_address_6, hexa_code_address_6)
        fw.write(result_str_6)
        pc += 1
        line_counter += 1
    elif 'ori' in l:
        opcode_7 = '0111'
        match_7  = re.search(r'.* ori .*,.*,.*', str(l))
        argsls_7 = match_7.group().split()
        argsls_7[2] = argsls_7[2].split(',')
        Label_list.append(argsls_7[0])
        rt_7 = Convertor_to_binary(int(argsls_7[2][0]))
        rs_7 = Convertor_to_binary(int(argsls_7[2][1]))
        imm_7 = Convertor_to_binary(int(argsls_7[2][2]))
        binary_code_address_7 = I_Instruction(imm_7, rt_7, rs_7, opcode_7)
        decima_code_address_7 = int(binary_code_address_7, 2)
        hexa_code_address_7 = Convert_to_Hexa(decima_code_address_7)
        result_str_7 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_7, decima_code_address_7, hexa_code_address_7)
        fw.write(result_str_7)
        pc += 1
        line_counter += 1
    elif 'lui' in l:
        opcode_8 = '1000'
        match_8  = re.search(r'.* lui .*,.*,.*', str(l))
        argsls_8 = match_8.group().split()
        argsls_8[2] = argsls_8[2].split(',')
        Label_list.append(argsls_8[0])
        rt_8 = Convertor_to_binary(int(argsls_8[2][0]))
        rs_8 = Convertor_to_binary(int(argsls_8[2][1]))
        imm_8 = Convertor_to_binary(int(argsls_8[2][2]))
        binary_code_address_8 = I_Instruction(imm_8, rt_8, rs_8, opcode_8)
        decima_code_address_8 = int(binary_code_address_8, 2)
        hexa_code_address_8 = Convert_to_Hexa(decima_code_address_8)
        result_str_8 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_8, decima_code_address_8, hexa_code_address_8)
        fw.write(result_str_8)
        pc += 1
        line_counter += 1
    elif 'lw' in l:
        opcode_9 = '1001'
        match_9  = re.search(r'.* lw .*,.*,.*', str(l))
        argsls_9 = match_9.group().split()
        argsls_9[2] = argsls_9[2].split(',')
        Label_list.append(argsls_9[0])
        rt_9 = Convertor_to_binary(int(argsls_9[2][0]))
        rs_9 = Convertor_to_binary(int(argsls_9[2][1]))
        offset_9 = Convertor_to_binary(int(argsls_9[2][2]))
        binary_code_address_9 = I_Instruction(offset_9, rt_9, rs_9,opcode_9)
        decima_code_address_9 = int(binary_code_address_9, 2)
        hexa_code_address_9 = Convert_to_Hexa(decima_code_address_9)
        result_str_9 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (
        binary_code_address_9, decima_code_address_9, hexa_code_address_9)
        fw.write(result_str_9)
        pc += 1
        line_counter += 1
    elif 'sw' in l:
        opcode_10 = '1010'
        match_10  = re.search(r'.* sw .*,.*,.*', str(l))
        argsls_10 = match_10.group().split()
        argsls_10[2] = argsls_10[2].split(',')
        Label_list.append(argsls_10[0])
        rt_10 = Convertor_to_binary(int(argsls_10[2][0]))
        rs_10 = Convertor_to_binary(int(argsls_10[2][1]))
        offset_10 = Convertor_to_binary(int(argsls_10[2][2]))
        binary_code_address_10 = I_Instruction(offset_10, rt_10, rs_10, opcode_10)
        decima_code_address_10 = int(binary_code_address_10, 2)
        hexa_code_address_10   = Convert_to_Hexa(decima_code_address_10)
        result_str_10 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_10, decima_code_address_10, hexa_code_address_10)
        fw.write(result_str_10)
        pc += 1
        line_counter += 1
    elif 'beq' in l:
        opcode_11 = '1011'
        match_11  = re.search(r'.* beq .*,.*,.*', str(l))
        argsls_11 = match_11.group().split()
        argsls_11[2] = argsls_11[2].split(',')
        Label_list.append(argsls_11[0])
        rt_11 = Convertor_to_binary(int(argsls_11[2][0]))
        rs_11 = Convertor_to_binary(int(argsls_11[2][1]))
        offset_11 = Convertor_to_binary(int(argsls_11[2][2]))
        binary_code_address_11 = I_Instruction(offset_11, rt_11, rs_11, opcode_11)
        decima_code_address_11 = int(binary_code_address_11, 2)
        hexa_code_address_11   = Convert_to_Hexa(decima_code_address_11)
        result_str_11 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_11, decima_code_address_11, hexa_code_address_11)
        fw.write(result_str_11)
        pc += 1
        line_counter += 1
    elif 'jalr' in l:
        opcode_12 = '1100'
        match_12  = re.search(r'.* jalr .*,.*', str(l))
        argsls_12 = match_12.group().split()
        Label_list.append(argsls_12[0])
        rt_12 = Convertor_to_binary(int(argsls_12[2][0]))
        rs_12 = Convertor_to_binary(int(argsls_12[2][1]))
        offset_12 = ''
        binary_code_address_12 = I_Instruction(offset_12, rt_12, rs_12, opcode_12)
        decima_code_address_12 = int(binary_code_address_12, 2)
        hexa_code_address_12 = Convert_to_Hexa(decima_code_address_12)
        result_str_12 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_12, decima_code_address_12, hexa_code_address_12)
        fw.write(result_str_12)
        pc += 1
        line_counter += 1
############### J Type Instructions ##############################
    elif 'j' in l:
        opcode_13 = '1101'
        match_13  = re.search(r'.* j .*',str(l))
        argsls_13 = match_13.group().split()
        Label_list.append(argsls_13[0])
        targ_13 = Convertor_to_binary(int(argsls_13[2]))
        binary_code_address_13 = J_Instruction(targ_13, opcode_13)
        decima_code_address_13 = int(binary_code_address_13, 2)
        hexa_code_address_13   = Convert_to_Hexa(decima_code_address_13)
        pc += 1
        line_counter += 1
    elif 'halt' in l:
        opcode_14 = '1110'
        A = ''
        binary_code_address_14 = opcode_14 + A.zfill(28)
        decima_code_address_14 = int(binary_code_address_14, 2)
        hexa_code_address_14   = Convert_to_Hexa(decima_code_address_14)
        result_str_14 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_14, decima_code_address_14, hexa_code_address_14)
        fw.write(result_str_14)
        pc += 1
        line_counter+=1
        exit(0)
############### Directive Instructions ############################
    elif '.fill' in l:
        match_15 = re.search(r'.* .fill .*', str(l))
        argsls_15  = match_15.group().split()
        binary_code_address_15 = Convertor_to_binary(int(argsls_15[2]))
        decima_code_address_15 = int(binary_code_address_15,2)
        hexa_code_address_15   = Convert_to_Hexa(decima_code_address_15)
        result_str_15 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_15, decima_code_address_15, hexa_code_address_15)
        fw.write(result_str_15)
        pc += 1
        line_counter += 1
    elif '.space' in  l:
        match_16 = re.search(r'.* .space .*', str(l))
        argsls_16 = match_16.group().split()
        z = ''
        binary_code_address_16 = z.zfill(int(argsls_16[2]))
        decima_code_address_16 = int(binary_code_address_16, 2)
        hexa_code_address_16   = Convert_to_Hexa(decima_code_address_16)
        result_str_16 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_16, decima_code_address_16, hexa_code_address_16)
        fw.write(result_str_16)
        pc += 1
        line_counter += 1
############## Denied Instructions #################################
    else:
        line_counter += 1
        wrong_command = re.search(r'.* .*', str(l))
        wrong_command_ls = wrong_command.group().split()
        if wrong_command_ls[1] not in command_list:
            print("an error has occurred in line %d" % line_counter)
            print("miniature: %s : command not found : %s" % (l, wrong_command_ls[1]))
        exit(1)

fw.close()
#############################################################################################

#TODO: Hanlde Errors in Instructions and invalid instruction,Labels and offsets
#TODO: Jump to lines by line_counter
