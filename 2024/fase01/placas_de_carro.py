placa = input()
padrao_da_placa = 'x'

if len(placa) == 8 or len(placa) == 7:
    for i in range(3):
        if placa[i].isalpha() == False or placa[i] != placa[i].upper():
            padrao_da_placa = 0

    if padrao_da_placa == 'x':

        if placa[3] == '-':
            for i in range(4,8):
                if placa[i].isnumeric() == False:
                    padrao_da_placa = 0
            if padrao_da_placa == 'x':
                padrao_da_placa = 1

        elif placa[3].isnumeric():
            if placa[4].isalpha() and placa[4] == placa[4].upper():
                for i in range(5,7):
                    if placa[i].isnumeric() == False:
                        padrao_da_placa = 0
            else:
                padrao_da_placa = 0
            if padrao_da_placa == 'x':
                padrao_da_placa = 2
        else:
            padrao_da_placa = 0
else:
    padrao_da_placa = 0

print(padrao_da_placa)
