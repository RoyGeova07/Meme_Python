import pygame
import sys

peso=input("Ingresa tu peso: ")


pygame.init()
fondo= pygame.display.set_mode((600,400))
pygame.display.set_caption("Imagen Rotando")

imagen = pygame.image.load("c:/Users/royum/OneDrive/Documentos/roy/Python/noGordas.jpg")
imagen=pygame.transform.scale(imagen,(400,400))
coordenadas=imagen.get_rect(center=(300,200))

#aqui agrego 2 variables para rotar el angulo de giro y el otro para los fps
angulo=0
reloj=pygame.time.Clock()

pygame.mixer.music.load("c:/Users/royum/OneDrive/Documentos/roy/Python/oyegela.mp3")
pygame.mixer.music.play(-1)

while True:
    for evento in pygame.event.get():
        if evento.type== pygame.QUIT:
            pygame.quit()
            sys.exit
    #aqui aumentamos el angulo de giro
    angulo +=1
    imagen_rotada = pygame.transform.rotate(imagen,angulo)#lo rotamos
    rect_rotado=imagen_rotada.get_rect(center=coordenadas.center)#aqui las nuevas coordenadas
    
    fondo.fill((255, 255, 255))
    fondo.blit(imagen_rotada,rect_rotado.topleft)
    
    pygame.display.flip()
    reloj.tick(60) #y por ultimo aqui se hace que se ejecute en 60 fps
