import math

#Notas sobre o código: devo implementar uma ferramenta de cálculo de custo de CPA. 


#def return_time(value_1, value_2):
#   str(value_1) + str(value_2) + " dias"

#def return_value:




#casos = int(input('Quantos casos você quer analisar?'))
investimento_diario = float(input('Quanto você pretende investir diariamente? '))
#cpa_medio_mercado = float(input(print('Qual o CPA médio no seu mercado?')))


# 1300 cliques mensais para 30 reais diários.
investimento_total = investimento_diario*30

valor_padrao_por_clique = 1300/30/30

cliques_diarios = valor_padrao_por_clique*investimento_diario

cliques_totais_mensais = valor_padrao_por_clique*investimento_diario*30

#cliques_totais = float(1000)

conversao_cliques_visualizacoes = float(0.7)

#visualizacoes = cliques_totais*conversao_cliques_visualizacoes

visualizacoes = cliques_totais_mensais*conversao_cliques_visualizacoes

conversao_visualizacoes_agendamentos = float(0.05)

agendamentos = visualizacoes*conversao_visualizacoes_agendamentos

conversao_agendamentos_reunioes = float(0.25)

reunioes = agendamentos*conversao_agendamentos_reunioes

conversao_reunioes_fechamentos = float(0.15)

fechamentos = reunioes*conversao_reunioes_fechamentos

custo_por_fechamento = (investimento_diario*30)/fechamentos

#tempo_médio_por_captacao = investimento_diario
contador_custo_por_fechamento = 0.0

contador_temporal_por_cliente = 0

while contador_custo_por_fechamento < custo_por_fechamento:
    contador_custo_por_fechamento += investimento_diario
    contador_temporal_por_cliente += 1


# def porcentagem(valor):
#     resultado = str(valor*100) + "%"

print('--------------------------------------------------------')
print('Investimento diário = ' + str(investimento_diario))
print("Investimento total = " + str(investimento_total))
print("Quantidade de cliques = " + str(round(cliques_totais_mensais))) #cliques baixos, melhore os anúncios.
print("Quant. de cliques diários = " + str(round(cliques_diarios, 2))) 
print("Custo médio por clique = " + str(round(valor_padrao_por_clique, 2)))
print("Quantidade de visualizações = " + str(round(visualizacoes))) #views baixos, melhore o carregamento do site.
print("Conversão de views para agendamentos = " + str(conversao_visualizacoes_agendamentos*100) + "%") #Conversão de views para agendamento baixa, melhore a copy do site.
print("Custo médio por agendamento = " + str(round(investimento_total/agendamentos, 2)))
print("Agendamentos = " + str(agendamentos)) #agendamentos baixos, melhore o follow 30up.
# print("Conversão de agendamentos em reuniões = " + porcentagem(conversao_agendamentos_reunioes)) 
print("Conversão de agendamentos em reuniões = " + str(conversao_agendamentos_reunioes*100) + "%") #Conversão de agendamentos em reuniões baixa, melhore o follow-up.
print("Reuniões = " + str(round(reunioes, 1))) #Quantidade de reuniões baixa, melhore o follow up.
print("Custo por reunião = " + str(round(investimento_total/reunioes, 2)))
print("Conversão Reuniões / fechamentos = " + str(conversao_reunioes_fechamentos*100) + "%") #Conversão de reuniões em fechamentos baixa, melhore a call de vendas.
print("Clientes fechados = " + str(round(fechamentos, 2))) #Quantidade de fechamentos baixa, melhore a call de vendas e a oferta.
print("Custo de aquisição de cliente = " + str(round(custo_por_fechamento, 2)))
print("Tempo médio por aquisição = " + str(contador_temporal_por_cliente) + " dias")
print("--------------------------------------------------------")


#print("Considerando o CPA médio de mercado, o seu funil ainda suporta um custo médio por clique de até: " + str())