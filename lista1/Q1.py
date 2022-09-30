print('Seja bem vindo(a) à Mariana Encanamentos!')
print('Nós resolvemos todos os tipos de problemas com vazamentos de água.')
print('Responda esse questionário para verificarmos quão grave é sua situação!')
print('-'*50)
quantidade_dias_D = int(input('Digite por quantos dias as gotas ficaram caindo: '))
quantidade_gota_G = int(input('Digite a quantidade de gotas caídas por segundo: '))
volume_gota_V = float(input('Digite o volume de uma gota em ml: '))


diaEmSegundos = (24*60)*60 #converte um dia em segundos
gotasPorDia = diaEmSegundos * quantidade_gota_G #pega a quantidade de segundos por dia e multiplica pela quantidade de gotas por segundo, me fornecendo o numero de gotas que cairam em 1 dia
valorMililitro = (quantidade_dias_D * gotasPorDia) * volume_gota_V #multiplica a quantidade de gotas em um dia pela quantidade de dias, e depois pega o resultado e multiplica pelo volume, fornecendo assim o volume de todas as gotas em todos os n dias
valorLitro = (valorMililitro / 1000) // 1 #converte ml em l e retira o valor dos decimais
print(f'Hum, me parece que vazou um total de {valorLitro:.0f} litros de água da sua torneira!') #imprime na tela o resultado sem decimais
