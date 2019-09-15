#Faça um programa em Python que abra e reproduza um arquivo em audio MP3
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.game.play()
pygame.event.wait()
