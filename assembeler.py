"""
this is an assembler known as Miniature.
It's Instructions has 3 kinds of format: R type, I type and J type
"""

import re
import os.path

I_file_name = input('Enter the path and name of Input file in form of : filename.as\n')
# while True:
#     if os.path.isfile(I_file_name):
#         break
#     else:
#         print("please Enter an existance path")
O_file_name = input('Enter the path and name of Output file in form of : program.mc\n')
fn = open(I_file_name, 'r')
fw = open(O_file_name, 'a')
pc = 0
line_counter = -1
command_list = ['add', 'sub', 'slt', 'or', 'nand', 'addi', 'ori', ' slti', 'lui', 'lw', 'sw', 'beq', 'jalr', 'j', '.space', '.fill']
Label_list = {}

########## Negative Number Extender ##########################################################

def negative_extender(s):
     res = "{0:1>16s}".format(s)
     return res
############## Calculation R type Instruction ######################

def R_Instruction(op, rs, rt, rd):
    res = ''
    res = res.zfill(4) + op.zfill(4) + rs.zfill(4) + rt.zfill(4) + rd.zfill(4) + res.zfill(12)
    return res
############## Calculation I type Instruction ######################

def I_Instruction(op, rs, rt, offset):
    res = ''
    # if offset > 0:
    #     offset = offset.zfill(16)
    # else:
    #     offset = negative_extender(offset)
    res = res.zfill(4) + op.zfill(4) + rs.zfill(4) + rt.zfill(4) + offset.zfill(16)
    return res

############## Calculation J Type Instruction ######################

def J_Instruction(op, target):
    res  = ''
    res = res.zfill(4) + op.zfill(4) + res.zfill(8) + target.zfill(16)
    return res

############## a Function to convert decimal numbers to Binary #############################

def Convertor_to_binary(number):
    res = bin(int(number)).lstrip('0b')
    return res
############## a function to convert decimal numbers to Hexadecimal #########################

def Convert_to_Hexa(number):
    res = hex(int(number))
    return res
############# a function to Handle not defined labels ########################################

def Not_define_label_Error(Label, LC):
    if Label not in Label_list.keys():
        print("an error occurred on line %d" % LC)
        print("This Label Not Defined")
        exit(1)
############ a function to Handle the offset overheading #####################################

def Offset_overheading_Error(offset_value, LC):
    if len(offset_value) > 16:
        print("an error occurred on line %d" % LC)
        print("offset overheading error")
        exit(1)


##################################### First Scan ###############################################

file_ls = fn.read().splitlines()
L_C = -1
for line in file_ls:
    L_C += 1
    argsls = line.split()
    if argsls[0] in Label_list.keys():
        print("an error occurred on line %d" % L_C)
        print("Duplicate Label Error")
        exit(1)
    if argsls[0] != "-":
        Label_list[argsls[0]] = L_C

###################################### Second Scan #############################################

for l in file_ls:

#################### R Type Instructions #######################################################

#################### add Instruction ################################

    if 'add' in l:
        opcode_0 = '0000'
        pc += 1
        line_counter += 1
        match_0  = re.search(r'.* add .*,.*,.*', str(l))
        argsls_0 = match_0.group().split()
        argsls_0[2] = argsls_0[2].split(',')
        rd_0 = Convertor_to_binary(int(argsls_0[2][0]))
        rs_0 = Convertor_to_binary(int(argsls_0[2][1]))
        rt_0 = Convertor_to_binary(int(argsls_0[2][2]))
        binary_code_address_0 = R_Instruction(opcode_0, rs_0, rt_0, rd_0)
        decima_code_address_0 = int(binary_code_address_0, 2)
        hexa_code_address_0   = Convert_to_Hexa(decima_code_address_0)
        result_str_0 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_0, decima_code_address_0, hexa_code_address_0)
        fw.write(result_str_0)

##################### sub Instruction #################################

    elif 'sub' in l:
        opcode_1 = '0001'
        pc += 1
        line_counter += 1
        match_1  = re.search(r'.* sub .*,.*,.*', str(l))
        argsls_1 = match_1.group().split()
        argsls_1[2] = argsls_1[2].split(',')
        rd_1 = Convertor_to_binary(int(argsls_1[2][0]))
        rs_1 = Convertor_to_binary(int(argsls_1[2][1]))
        rt_1 = Convertor_to_binary(int(argsls_1[2][2]))
        binary_code_address_1 = R_Instruction(opcode_1, rs_1, rt_1, rd_1)
        decima_code_address_1 = int(binary_code_address_1, 2)
        hexa_code_address_1 = Convert_to_Hexa(decima_code_address_1)
        result_str_1 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_1, decima_code_address_1, hexa_code_address_1)
        fw.write(result_str_1)

##################### slt Instruction #################################

    elif 'slt' in l:
        opcode_2 = '0010'
        pc += 1
        line_counter += 1
        match_2  = re.search(r'.* slt .*,.*,.*', str(l))
        argsls_2 = match_2.group().split()
        argsls_2[2] = argsls_2[2].split(',')
        rd_2 = Convertor_to_binary(int(argsls_2[2][0]))
        rs_2 = Convertor_to_binary(int(argsls_2[2][1]))
        rt_2 = Convertor_to_binary(int(argsls_2[2][2]))
        binary_code_address_2 = R_Instruction(opcode_2, rs_2, rt_2, rd_2)
        decima_code_address_2 = int(binary_code_address_2, 2)
        hexa_code_address_2   = Convert_to_Hexa(decima_code_address_2)
        result_str_2 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_2, decima_code_address_2, hexa_code_address_2)
        fw.write(result_str_2)

#################### or Instruction ###################################

    elif 'or' in l:
        opcode_3 = '0011'
        pc += 1
        line_counter += 1
        match_3  = re.search(r'.* or .*,.*,.*', str(l))
        argsls_3 = match_3.group().split()
        argsls_3[2] = argsls_3[2].split(',')
        rd_3 = Convertor_to_binary(int(argsls_3[2][0]))
        rs_3 = Convertor_to_binary(int(argsls_3[2][1]))
        rt_3 = Convertor_to_binary(int(argsls_3[2][2]))
        binary_code_address_3 = R_Instruction(opcode_3, rs_3, rt_3, rd_3)
        decima_code_address_3 = int(binary_code_address_3, 2)
        hexa_code_address_3 = Convert_to_Hexa(decima_code_address_3)
        result_str_3 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_3, decima_code_address_3, hexa_code_address_3)
        fw.write(result_str_3)

################## nand Instruction ###################################

    elif 'nand' in l:
        opcode_4 = '0100'
        pc += 1
        line_counter += 1
        match_4  = re.search(r'.* nand .*,.*,.*', str(l))
        argsls_4 = match_4.group().split()
        argsls_4[2] = argsls_4[2].split(',')
        rd_4 = Convertor_to_binary(int(argsls_4[2][0]))
        rs_4 = Convertor_to_binary(int(argsls_4[2][1]))
        rt_4 = Convertor_to_binary(int(argsls_4[2][2]))
        binary_code_address_4 = R_Instruction(opcode_4, rs_4, rt_4, rd_4)
        decima_code_address_4 = int(binary_code_address_4, 2)
        hexa_code_address_4 = Convert_to_Hexa(decima_code_address_4)
        result_str_4 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_4, decima_code_address_4, hexa_code_address_4)
        fw.write(result_str_4)

####################### I Type Instructions #############################################################

####################### addi Instruction ###############################

    elif 'addi' in l:
        opcode_5 = '0101'
        pc += 1
        line_counter += 1
        match_5  = re.search(r'.* addi .*,.*,.*', str(l))
        argsls_5 = match_5.group().split()
        argsls_5[2] = argsls_5[2].split(',')
        rt_5  = Convertor_to_binary(int(argsls_5[2][0]))
        rs_5  = Convertor_to_binary(int(argsls_5[2][1]))
        imm_5 = Convertor_to_binary(int(argsls_5[2][2]))
        binary_code_address_5 = I_Instruction(opcode_5, rs_5, rt_5, imm_5)
        decima_code_address_5 = int(binary_code_address_5, 2)
        hexa_code_address_5   = Convert_to_Hexa(decima_code_address_5)
        result_str_5 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_5, decima_code_address_5, hexa_code_address_5)
        fw.write(result_str_5)

################### slti Instruction ###################################

    elif 'slti' in l:
        opcode_6 = '0110'
        pc += 1
        line_counter += 1
        match_6  = re.search(r'.* slti .*,.*,.*', str(l))
        argsls_6 = match_6.group().split()
        argsls_6[2] = argsls_6[2].split(',')
        rt_6 = Convertor_to_binary(int(argsls_6[2][0]))
        rs_6 = Convertor_to_binary(int(argsls_6[2][1]))
        imm_6 = Convertor_to_binary(int(argsls_6[2][2]))
        binary_code_address_6 = I_Instruction(opcode_6, rs_6, rt_6, imm_6)
        decima_code_address_6 = int(binary_code_address_6, 2)
        hexa_code_address_6 = Convert_to_Hexa(decima_code_address_6)
        result_str_6 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_6, decima_code_address_6, hexa_code_address_6)
        fw.write(result_str_6)

################### ori Instruction ###################################

    elif 'ori' in l:
        opcode_7 = '0111'
        pc += 1
        line_counter += 1
        match_7  = re.search(r'.* ori .*,.*,.*', str(l))
        argsls_7 = match_7.group().split()
        argsls_7[2] = argsls_7[2].split(',')
        rt_7 = Convertor_to_binary(int(argsls_7[2][0]))
        rs_7 = Convertor_to_binary(int(argsls_7[2][1]))
        imm_7 = Convertor_to_binary(int(argsls_7[2][2]))
        binary_code_address_7 = I_Instruction(opcode_7, rs_7, rt_7, imm_7)
        decima_code_address_7 = int(binary_code_address_7, 2)
        hexa_code_address_7 = Convert_to_Hexa(decima_code_address_7)
        result_str_7 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_7, decima_code_address_7, hexa_code_address_7)
        fw.write(result_str_7)

################## lui Instruction ####################################

    elif 'lui' in l:
        opcode_8 = '1000'
        pc += 1
        line_counter += 1
        match_8  = re.search(r'.* lui .*,.*,.*', str(l))
        argsls_8 = match_8.group().split()
        argsls_8[2] = argsls_8[2].split(',')
        rt_8 = Convertor_to_binary(int(argsls_8[2][0]))
        rs_8 = Convertor_to_binary(int(argsls_8[2][1]))
        imm_8 = Convertor_to_binary(int(argsls_8[2][2]))
        binary_code_address_8 = I_Instruction(opcode_8, rs_8, rt_8, imm_8)
        decima_code_address_8 = int(binary_code_address_8, 2)
        hexa_code_address_8 = Convert_to_Hexa(decima_code_address_8)
        result_str_8 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_8, decima_code_address_8, hexa_code_address_8)
        fw.write(result_str_8)

################# lw Instruction ######################################

    elif 'lw' in l:
        opcode_9 = '1001'
        pc += 1
        line_counter += 1
        match_9  = re.search(r'.* lw .*,.*,.*', str(l))
        argsls_9 = match_9.group().split()
        argsls_9[2] = argsls_9[2].split(',')
        rt_9 = Convertor_to_binary(int(argsls_9[2][0]))
        rs_9 = Convertor_to_binary(int(argsls_9[2][1]))
        if len(argsls_9[2][2]) <= 2:
            offset_9 = Convertor_to_binary(int(argsls_9[2][2]))
            Offset_overheading_Error(offset_9, line_counter)
            binary_code_address_9 = I_Instruction(opcode_9, rs_9, rt_9, offset_9)
            decima_code_address_9 = int(binary_code_address_9, 2)
            hexa_code_address_9 = Convert_to_Hexa(decima_code_address_9)
            result_str_9 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_9, decima_code_address_9, hexa_code_address_9)
            fw.write(result_str_9)

        else:
            offset_9 = argsls_9[2][2]
            Not_define_label_Error(offset_9, line_counter)
            for label in Label_list.keys():
                if label == offset_9:
                    if Label_list[label] < line_counter:
                        offset_9 = negative_extender(Convertor_to_binary(Label_list[label]))
                    else:
                        offset_9 = Convertor_to_binary(Label_list[label])
                    Offset_overheading_Error(offset_9, line_counter)
                    binary_code_address_9 = I_Instruction(opcode_9, rs_9, rt_9, offset_9)
                    decima_code_address_9 = int(binary_code_address_9, 2)
                    hexa_code_address_9 = Convert_to_Hexa(decima_code_address_9)
                    result_str_9 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_9, decima_code_address_9, hexa_code_address_9)
                    fw.write(result_str_9)

################ sw Instruction #######################################

    elif 'sw' in l:
        opcode_10 = '1010'
        pc += 1
        line_counter += 1
        match_10  = re.search(r'.* sw .*,.*,.*', str(l))
        argsls_10 = match_10.group().split()
        argsls_10[2] = argsls_10[2].split(',')
        rt_10 = Convertor_to_binary(int(argsls_10[2][0]))
        rs_10 = Convertor_to_binary(int(argsls_10[2][1]))
        if len(argsls_10[2][2]) <= 1:
            offset_10 = Convertor_to_binary(argsls_10[2][2])
            binary_code_address_10 = I_Instruction(opcode_10, rs_10, rt_10, offset_10)
            decima_code_address_10 = int(binary_code_address_10, 2)
            hexa_code_address_10 = Convert_to_Hexa(decima_code_address_10)
            result_str_10 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (
            binary_code_address_10, decima_code_address_10, hexa_code_address_10)
            fw.write(result_str_10)

        else:
            offset_10 = argsls_10[2][2]
            Not_define_label_Error(offset_10, line_counter)
            for label in Label_list.keys():
                if label == offset_10:
                    if Label_list[label] < line_counter:
                        offset_10 = negative_extender(Convertor_to_binary(Label_list[label]))
                    else:
                        offset_10 = Convertor_to_binary(Label_list[label])
                    Offset_overheading_Error(offset_10, line_counter)
                    binary_code_address_10 = I_Instruction(opcode_10, rs_10, rt_10, offset_10)
                    decima_code_address_10 = int(binary_code_address_10, 2)
                    hexa_code_address_10 = Convert_to_Hexa(decima_code_address_10)
                    result_str_10 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_10, decima_code_address_10, hexa_code_address_10)
                    fw.write(result_str_10)

################# beq Instruction #######################################

    elif 'beq' in l:
        opcode_11 = '1011'
        pc += 1
        line_counter += 1
        match_11  = re.search(r'.* beq .*,.*,.*', str(l))
        argsls_11 = match_11.group().split()
        argsls_11[2] = argsls_11[2].split(',')
        rt_11 = Convertor_to_binary(int(argsls_11[2][0]))
        rs_11 = Convertor_to_binary(int(argsls_11[2][1]))
        Not_define_label_Error(argsls_11[2][2], line_counter)
        for label in Label_list.keys():
            if label == argsls_11[2][2]:
                L = Label_list[label]
                Diff = int(L) - (line_counter + 1)
                if Diff > 0:
                    offset_11 = str(Convertor_to_binary(Diff)).zfill(16)
                else:
                    offset_11 = negative_extender(Convertor_to_binary(Diff).lstrip('-0b'))
                Offset_overheading_Error(offset_11, line_counter)
                binary_code_address_11 = I_Instruction(opcode_11, rs_11, rt_11, offset_11)
                decima_code_address_11 = int(binary_code_address_11, 2)
                hexa_code_address_11   = Convert_to_Hexa(decima_code_address_11)
                result_str_11 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_11, decima_code_address_11, hexa_code_address_11)
                fw.write(result_str_11)

################# jalr Instruction ######################################

    elif 'jalr' in l:
        opcode_12 = '1100'
        pc += 1
        line_counter += 1
        match_12  = re.search(r'.* jalr .*,.*', str(l))
        argsls_12 = match_12.group().split()
        rt_12 = Convertor_to_binary(int(argsls_12[2][0]))
        rs_12 = Convertor_to_binary(int(argsls_12[2][1]))
        offset_12 = ''
        binary_code_address_12 = I_Instruction(opcode_12, rs_12, rt_12, offset_12)
        decima_code_address_12 = int(binary_code_address_12, 2)
        hexa_code_address_12 = Convert_to_Hexa(decima_code_address_12)
        result_str_12 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_12, decima_code_address_12, hexa_code_address_12)
        fw.write(result_str_12)

############### J Type Instructions ###############################################################################

############### j Instruction ####################################

    elif 'j' in l:
        opcode_13 = '1101'
        pc += 1
        line_counter += 1
        match_13  = re.search(r'.* j .*',str(l))
        argsls_13 = match_13.group().split()
        targ_13 = argsls_13[2]
        Not_define_label_Error(targ_13, line_counter)
        for label in Label_list.keys():
            if label == targ_13:
                targ_13 = Convertor_to_binary(int(Label_list[label]))
                Offset_overheading_Error(targ_13, line_counter)
                binary_code_address_13 = J_Instruction(opcode_13, targ_13)
                decima_code_address_13 = int(binary_code_address_13, 2)
                hexa_code_address_13   = Convert_to_Hexa(decima_code_address_13)
                result_str_13 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_13, decima_code_address_13, hexa_code_address_13)
                fw.write(result_str_13)

############### halt Instruction #################################

    elif 'halt' in l:
        opcode_14 = '1110'
        pc += 1
        line_counter += 1
        match_14 = re.search(r'.* halt', str(l))
        argsls_14 = match_14.group().split()
        A = ''
        binary_code_address_14 = A.zfill(4) + opcode_14 + A.zfill(24)
        decima_code_address_14 = int(binary_code_address_14, 2)
        hexa_code_address_14   = Convert_to_Hexa(decima_code_address_14)
        result_str_14 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_14, decima_code_address_14, hexa_code_address_14)
        fw.write(result_str_14)


############### Directive Instructions ###########################################################################

############### .fill Instruction ##################################

    elif '.fill' in l:
        pc += 1
        line_counter += 1
        match_15 = re.search(r'.* .fill .*', str(l))
        argsls_15  = match_15.group().split()

        if len(argsls_15[2]) <= 2:
            target_15 = argsls_15[2]
            binary_code_address_15 = Convertor_to_binary(int(target_15))
            decima_code_address_15 = int(binary_code_address_15, 2)
            hexa_code_address_15 = Convert_to_Hexa(decima_code_address_15)
            result_str_15 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_15, decima_code_address_15, hexa_code_address_15)
            fw.write(result_str_15)

        else:

            target_15 = argsls_15[2]
            Not_define_label_Error(target_15, line_counter)
            for label in Label_list.keys():
                if label == target_15:
                    target_15 = Convertor_to_binary(Label_list[label])
                    Offset_overheading_Error(target_15, line_counter)
                    binary_code_address_15 = target_15
                    decima_code_address_15 = int(binary_code_address_15, 2)
                    hexa_code_address_15 = Convert_to_Hexa(decima_code_address_15)
                    result_str_15 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_15, decima_code_address_15, hexa_code_address_15)
                    fw.write(result_str_15)

################ .space Instruction ####################################

    elif '.space' in l:
        pc += 1
        line_counter += 1
        match_16 = re.search(r'.* .space .*', str(l))
        argsls_16 = match_16.group().split()
        z = ''
        binary_code_address_16 = z.zfill(int(argsls_16[2]))
        decima_code_address_16 = int(binary_code_address_16, 2)
        hexa_code_address_16   = Convert_to_Hexa(decima_code_address_16)
        result_str_16 = "BINARY : %s  DECIMAL : %s  HEXADECIMAL : %s \n" % (binary_code_address_16, decima_code_address_16, hexa_code_address_16)
        fw.write(result_str_16)

############## Denied Instructions ############################################################################

    else:
        line_counter += 1
        wrong_command = re.search(r'.* .* .*', str(l))
        wrong_command_ls = wrong_command.group().split()
        if wrong_command_ls[1] not in command_list:
            print("an error occurred on line %d" % line_counter)
            print("miniature: command not found : %s" % wrong_command_ls[1])
        exit(1)

fw.close()
################################################################################################################
