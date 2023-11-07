#Abrir e reproduzir MP3
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("Taylor Swif-I Knew You Were Trouble.mp3")
pygame.mixer_music.play()
pygame.event.wait()