# reproduza um audio com o python
import os
import time
import 
pygame.init()

ouvirMusica =  str.upper(input("Você quer ouvir a música predileta? \n 1-Sim \n 2-Não \n ".upper()))

if ouvirMusica == 'SIM':
    print('ok')
    pygame.mixer.music.load("/home/wesley/Música/1.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()
elif ouvirMusica == 'S':
    print('OKSS')
elif ouvirMusica == '1':
    print('our')
if ouvirMusica == 'N':
    print('bla')
elif ouvirMusica == 'NÃO':
    print('Teste')
elif ouvirMusica == '2':
    print('jafljs1')