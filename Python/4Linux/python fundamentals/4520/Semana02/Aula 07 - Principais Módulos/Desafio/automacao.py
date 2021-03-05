from os import system
from datetime import datetime

print('Incio da execução {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M:%S')))

system('sudo apt update')

print('Fim do update {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M:S')))
