# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# import os
# import time
# import 
# pygame.init()

# ouvirMusica =  str.upper(input("Você quer ouvir a música predileta? \n 1-Sim \n 2-Não \n ".upper()))

# if ouvirMusica == 'SIM':
#     print('ok')
#     pygame.mixer.music.load("/home/wesley/Música/1.mp3")
#     pygame.mixer.music.play()
#     pygame.event.wait()
# elif ouvirMusica == 'S':
#     print('OKSS')
# elif ouvirMusica == '1':
#     print('our')
# if ouvirMusica == 'N':
#     print('bla')
# elif ouvirMusica == 'NÃO':
#     print('Teste')
# elif ouvirMusica == '2':
#     print('jafljs1')

 #Importando o PyGame
# import pygame
# import os
# # Inicializando o PyGame
# pygame.init()

# # Carregando o arquivo MP3 e executando
# if os.path.exists('song.wav'):
#     pygame.mixer.music.load('/home/wesley/Wtroy/EST/CursoEmVideoPython/Mundo01/exercicios/song.wav')
#     pygame.mixer.music.play()
#     pygame.mixer.music.set_volume(1)

#     clock = pygame.time.Clock()
#     clock.tick(10)

#     while pygame.mixer.music.get_busy():
#         pygame.event.poll()
#         clock.tick(10)
# else:
#     print('O arquivo musica.mp3 não está no diretório do script Python')

import pygame
pygame.init()
pygame.mixer.music.load("/home/wesley/Wtroy/EST/CursoEmVideoPython/Mundo01/exercicios/song.wav")
pygame.mixer.music.play()
