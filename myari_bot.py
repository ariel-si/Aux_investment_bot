from iqoptionapi.stable_api import IQ_Option
import sys, time, os

email = "robotfinanceiq@gmail.com"
senha = "botfinance24"
porcentagem_lucro = 10
entrada = 2.0
moeda = "EURUSD"
tipoConta = "PRACTICE"  # PRACTICE / REAL
operacao = "call" #put / call
timeframe = 1

API = IQ_Option(email, senha)
API.connect()
API.change_balance(tipoConta)

if API.check_connect():
	print(' Conectado com sucesso!')
else:
	print(' Erro ao conectar')
	input('\n\n Aperte enter para sair')
	sys.exit()
	

valor_minimo = round(float(entrada) * (float(porcentagem_lucro / 100)), 2)


API.subscribe_strike_list(moeda, timeframe)

status,id = API.buy_digital_spot(moeda, entrada, operacao, timeframe)
time.sleep(0.3)

while API.get_async_order(id)['position-changed']['msg']['status'] == 'open':
	vpv = round(API.get_digital_spot_profit_after_sale(id), 2)
	
	time.sleep(0.3)
	os.system('cls' if os.name == 'nt' else 'clear')
	print('Atual: $' + str(vpv) + ' - Minimo para venda: $' + str(valor_minimo))
	
	if vpv > valor_minimo:
		print('Fechando operação')
		API.close_digital_option(id)
		break
	
	time.sleep(0.3)
	
status,valor = API.check_win_digital_v2(id)
print('Resultado da operação: ' + str('WIN +' if valor > 0 else 'LOSS ') + str(round(valor, 2)))
