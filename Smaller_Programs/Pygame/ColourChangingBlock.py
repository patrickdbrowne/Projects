import pygame

pygame.init()

window = pygame.display.set_mode((1000, 800))

speed = 10
R = 5
G = 0
B = 0

[x, y, width, height] = [100, 100, 150, 150]
running = True
while running:
    pygame.time.delay(5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(window, (R, G, B), (x, y, width, height))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    if keys[pygame.K_SPACE]:
        R += 5
        if R == 255:
            R = 5
            G += 5
        if G == 255:
            G = 5
            B += 5
        if B == 255:
            R = 5
            G = 0
            B = 0

    pygame.display.update()
    window.fill((0, 0, 0))


pygame.quit()
