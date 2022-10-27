import pygame
import time

pygame.init()

soundObj = pygame.mixer.Sound('media/BerserkerCaster.wav')
soundObj.play()
time.sleep(3)
soundObj.stop()
pygame.quit()
