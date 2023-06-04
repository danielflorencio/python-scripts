import math

print('1 - Analyze the results of your investments.')
print('2 - Analyze if you should rent something or not.')
toDo = int(input('Type your answer: '))
montante = 0, 0
tempo_meses = int(36)
valorização_mensal = 1.1
aporte_mensal = 10000
if toDo == 1: 
    print('montante mês 0 caso 1: ' + str(montante) + ' --- ' + ' montante mês 0 caso 2:' + str(montante) + '\n______________________________')
    for i in range(tempo_meses):    
        montante = montante*valorização_mensal + aporte_mensal
        # if i == 0: 
        #     montante[0] = montante[0] - aporte_mensal[0]
        #     montante[1] = montante[1] - aporte_mensal[1]
        print("mes " + str(i+1))
        print("montante caso 1 = " + str(round(montante, 2)) + " -- Roi " + str(valorização_mensal[0]) + '\nmontante caso 2 = ' + str(round(montante, 2)) + " -- Roi " + str(valorização_mensal))
        print("_________________________________________") 
    montante_final_1 = str(round(montante, 2))
    print("O montante final do caso 1 foi: " + montante_final_1 + " -- Roi " + str(valorização_mensal))

elif todo == 2:

    wanna_rent = input('how much is worth weekly what you wanna rent? ') #950
    wanna_buy = input('how much does it cost to buy what you wanna rent? ') # 130.000
    for i in range(tempo_meses):    
        montante = montante*valorização_mensal + aporte_mensal
        # if i == 0: 
        #     montante[0] = montante[0] - aporte_mensal[0]
        #     montante[1] = montante[1] - aporte_mensal[1]
        print("mes " + str(i+1))
        print("montante caso 1 = " + str(round(montante, 2)) + " -- Roi " + str(valorização_mensal[0]) + '\nmontante caso 2 = ' + str(round(montante, 2)) + " -- Roi " + str(valorização_mensal))
        print("_________________________________________") 
    
