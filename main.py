import pygame

pygame.init()
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
coord = [250, 250]
target = [250, 250]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('black'))
    pygame.draw.ellipse(screen, (255, 0, 0), (coord[0] - 20, coord[1] - 20, 40, 40))
    if pygame.mouse.get_pressed()[0]:
        target = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
    pygame.time.delay(20)
    if coord != target:
        if coord[1] < target[1]:
            coord[1] += 1
        elif coord[1] > target[1]:
            coord[1] -= 1
        if coord[0] < target[0]:
            coord[0] += 1
        elif coord[0] > target[0]:
            coord[0] -= 1
    pygame.display.flip()
pygame.quit()