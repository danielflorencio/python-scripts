import math



montante = [0, 0]
#tempo_meses = [int(24), int(24)]
tempo_meses = [int(0), int(0)]
valorização_mensal = [1.05, 1.2]
aporte_mensal = [20000, 20000]

montly_yield = float(0.05) # average yield you can get monthly on your investments
desired_income = [10000] # how much money you wanna make monthly only through your investments

print('montante mês 0 caso 1: ' + str(montante[0]) + ' --- ' + ' montante mês 0 caso 2:' + str(montante[1]) + '\n______________________________')

i = 0
while montly_yield*montante[i] < desired_income:
    montante[0] = montante[0]*valorização_mensal[0] + aporte_mensal[0]
    montante[1] = montante[1]*valorização_mensal[1] + aporte_mensal[1]
    tempo_meses[0] = tempo_meses[0] + 1
    tempo_meses[1] = tempo_meses[1] + 1
    i = i + 1
    


for i in range(tempo_meses[0]):    
    montante[0] = montante[0]*valorização_mensal[0] + aporte_mensal[0]
    montante[1] = montante[1]*valorização_mensal[1] + aporte_mensal[1]
    if i == 0: 
        montante[0] = montante[0] - aporte_mensal[0]
        montante[1] = montante[1] - aporte_mensal[1]
    print("mes " + str(i+1))
    print("montante caso 1 = " + str(round(montante[0], 2)) + " -- Roi " + str(valorização_mensal[0]) + '\n montante caso 2 = ' + str(round(montante[1], 2)) + " -- Roi " + str(valorização_mensal[1]))
    print("_________________________________________") 


montante_final_1 = str(round(montante[0], 2))
montante_final_2 = str(round(montante[1], 2))

print("O montante final do caso 1 foi: " + montante_final_1 + " -- Roi " + str(valorização_mensal[0]))
print("O montante final do caso 2 foi: " + montante_final_2 + " -- Roi " + str(valorização_mensal[1]))

