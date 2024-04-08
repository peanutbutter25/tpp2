import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
finished = False
background = pygame.image.load('/Users/nurmatto/Desktop/Labarotory work 7/images/clock.png')
second_hand = pygame.image.load('/Users/nurmatto/Desktop/Labarotory work 7/images/lhand.png')
minute_hand = pygame.image.load('/Users/nurmatto/Desktop/Labarotory work 7/images/rhand.png')
rect_center = background.get_rect(center=(415, 418))

while not finished:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    current_time = datetime.now().time()

    second_angle = -(current_time.second * 6)
    minute_angle = -(current_time.minute * 6) - (current_time.second / 10)
    hour_angle = -(current_time.hour * 30) - (current_time.minute / 2)

    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)
    sec_rect = rotated_second_hand.get_rect(center=rect_center.center)
    screen.blit(rotated_second_hand, sec_rect.topleft)

    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    min_rect = rotated_minute_hand.get_rect(center=rect_center.center)
    screen.blit(rotated_minute_hand, min_rect.topleft)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()