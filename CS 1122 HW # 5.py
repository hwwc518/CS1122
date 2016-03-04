'''
Hui Wah Chiang
CS 1122 HW # 5
'''
# Operation code to mnemonic dictionary
# You can use this to lookup the machine code
# and translate it to the mnemonic instruction
INS_REF = {
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP"
}

def disassemble(operation_code):
    s = str(operation_code)
    if s[0] == '9':
        if s[2] == '1':
            return 'INP'
        elif s[2] == '2':
            return 'OUT'
    elif s[0] == '1':
        return ('ADD ' + s[1] + s[2])
    elif s[0] == '2':
        return ('SUB ' + s[1] + s[2])
    elif s[0] == '3 ':
        return ('STA' + s[1] + s[2])
    elif s[0] == '5':
        return ('LDA' + s[1] + s[2])
    elif s[0] == '6 ':
        return ('BRA' + s[1] + s[2])
    elif s[0] == '7 ':
        return ('BRZ' + s[1] + s[2])
    elif s[0] == '8 ':
        return ('BRP' + s[1] + s[2])
    # this function should take in an integer operation code
    # and convert it to a LMC mnemonic instruction and return
    # it as a string
    pass

def main():
    lst = []
    new_lst = []
    while True:
        y = int(input("Enter an int operation code"))
        if y != 000:
            lst.append(y)
        else:
            break
        
    for element in lst:
        string = disassemble(element)
        new_lst.append(string)
                
    for ele in new_lst:
        print (ele)
    print('HLT')
    
        
    # The main function should read all operation codes from the
    # user until the HLT instruction is read. Once it is read,
    # all operation codes should be disassembled using "disasassembled"
    # and then printed out to the user
    pass

if __name__ == "__main__":
    main()
