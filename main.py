
import sys, colors, pygame


pygame.init()
 

size=(550,800)

jugador_x =250
jugador_y = 760
pelota_x = 275
pelota_y = 650
velocidad_jugador_x = 0
velocidad_pelota_x= 0
velocidad_pelota_y = 0

#FPS
clock = pygame.time.Clock()
#crear ventana
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        sys.exit()
#colores de pantalla
    screen.fill(colors.BLANCO)

#enemigos
    for i in range(0,490,70):
         rojos = pygame.draw.rect(screen, colors.ROJO,(40,i, 100,30))
         
         azules = pygame.draw.rect(screen, colors.AZUL,(160,i,100,30))

         verdes =  pygame.draw.rect(screen, colors.VERDE,(280,i,100,30))
         
         morados = pygame.draw.rect(screen, colors.MORADO,(400,i,100,30))

#jugador
    jugador_x+=velocidad_jugador_x
    jugador = pygame.draw.rect(screen, colors.NEGRO,(jugador_x,760,150,20))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            velocidad_jugador_x= -3
        if event.key ==pygame.K_RIGHT:
            velocidad_jugador_x=3
   
    if event.type == pygame.KEYUP:       
        if event.key == pygame.K_LEFT:
            velocidad_jugador_x = 0
        if event.key == pygame.K_RIGHT:
            velocidad_jugador_x = 0

    if(jugador_x<0):
            jugador_x=0



    if(jugador_x>=400):
            jugador_x=400


#pelota
    pelota_x+=velocidad_pelota_y
    pelota_y+=velocidad_pelota_y
    pelota = pygame.draw.circle(screen, colors.AZUL, (pelota_x,pelota_y), 15)
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_SPACE:
            velocidad_pelota_x=3
            velocidad_pelota_y=3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            velocidad_pelota_x=3
            velocidad_pelota_y=3

#funcionamiento del juego
    #rebote de paredes
 



    if pelota.colliderect(jugador):
        velocidad_pelota_y *= -1

#fPS
    clock.tick(60)
#actualiza la pantalla
    pygame.display.flip()