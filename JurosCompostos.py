import math
#print('Valorização mensal sem aportes mensais = 1.')
#print('Valorização mensal com aportes mensais = 2.')
#escolha = int(input("Quer fazer um cálculo considerando uma valorização mensal sem investimentos mensais, ou com investimentos mensais? "))
    #amount = float(input("Insira aqui o valor inicial do investimento: "))
    #interestRate = float(input("Insira aqui a valorização mensal do investimento em porcentagem: "))
    #timeInMonths = int(input("Quantos meses no futuro você quer prever o seu amount financeiro? "))
    #interestRate = str(interestRate)
    #variavel_descartavel = str('1.' + interestRate)
    #valoriz222ação_mensal = float(variavel_descartavel)



# print('how')
amount = [0, 0, 0]
timeInMonths = int(12*12)
interestRate = [1.008, 1.008, 1.01]
monthlyInvestments = [4000, 8000, 28000]
print('amount month 0 case 1: ' + str(amount[0]) + ' --- ' + ' amount month 0 case 2:' + str(amount[1]) + '\n______________________________')
for i in range(timeInMonths):    
    amount[0] = amount[0]*interestRate[0] + monthlyInvestments[0]
    amount[1] = amount[1]*interestRate[1] + monthlyInvestments[1]
    amount[2] = amount[2]*interestRate[2] + monthlyInvestments[2]
    # if i == 0: 
    #     amount[0] = amount[0] - monthlyInvestments[0]
    #     amount[1] = amount[1] - monthlyInvestments[1]
    print("mes " + str(i+1))
    # print("amount case 1 = " + str(round(amount[0], 2)) + " -- Roi " + str(interestRate[0]) + '\namount case 2 = ' + str(round(amount[1], 2)) + " -- Roi " + str(interestRate[1]))
    for j in range(3):
        print("amount case " + str(j + 1) + " = " + str(round(amount[j], 2)) + " -- Roi " + str(interestRate[j]))
    if amount[0] > amount[1]:
        print('Difference: ' + str(round(amount[0] - amount[1], 2)))
    elif amount[0] < amount[1]:
        print('Difference: ' + str(round(amount[1] - amount[0], 2)))
    else:
        print('Difference: 0')
    print("_________________________________________") 
finalAmount1 = str(round(amount[0], 2))
finalAmount2 = str(round(amount[1], 2))
finalAmount3 = str(round(amount[2], 2))
print("The final amount of the case 1 was: " + finalAmount1 + " -- Roi " + str(interestRate[0]))
print("The final amount of the case21 was: " + finalAmount2 + " -- Roi " + str(interestRate[1]))
if amount[0] > amount[1]:
    print('Difference: ' + str(round(amount[0] - amount[1], 2)))
elif amount[0] < amount[1]:
    print('Difference: ' + str(round(amount[1] - amount[0], 2)))
else:
        print('Difference: 0')

    #amount_printado = round(amount, 2)
    #amount_printado = str(round(amount, 2))
    #for i in range(amount_printado):
    #    count = 0
    #    if (i+1) % 3 == 0:
    #        amount_printado[i].add
    #print("amount " + amount_printado)
    
#print("O amount final foi: " + str(round(amount,2)))
#else: 
 #   valor_inicial = float(input("Insira aqui o valor inicial do investimento: "))
  #  aportes_mensais = float(input("Insira aqui o valor médio dos aportes mensais: "))
   # interestRate = float(input("Insira aqui a valorização mensal do investimento em porcentagem: "))
    #timeInMonths = float(input("Quantos meses no futuro você quer prever o seu amount financeiro? "))
    
