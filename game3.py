import pygame
import random

pygame.init()

window_width = 480
window_height = 640
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("게임")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\rex02\\바탕 화면\\pythonProject\\KakaoTalk_20240613_003705854.jpg")
background = pygame.transform.scale(background, (480, 640))
background = pygame.transform.rotate(background, 180)
character = pygame.image.load("C:\\Users\\rex02\\바탕 화면\\pythonProject\\사람.png")
character = pygame.transform.scale(character, (40, 40))
character_rect = character.get_rect()
character_width = character_rect.width
character_height = character_rect.height
character_x_pos = window_width / 2 - character_width / 2
character_y_pos = window_height - character_height
character_speed = 0.6

enemy = pygame.image.load("C:\\Users\\rex02\\바탕 화면\\pythonProject\\pngegg.png")
enemy = pygame.transform.scale(enemy, (50, 50))
enemy_rect = enemy.get_rect()
enemy_width = enemy_rect.width
enemy_height = enemy_rect.height
enemy_speed = 0.3

enemies = []


def create_enemy():
    enemy_x_pos = random.uniform(0, window_width - enemy_width)
    enemy_y_pos = -enemy_height
    return [enemy_x_pos, enemy_y_pos]


last_enemy_time = 0
enemy_interval = random.randint(0, 1000)

to_x = 0

game_font = pygame.font.Font(None, 40)
score = 0

running = True
while running == True:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > window_width - character_width:
        character_x_pos = window_width - character_width

    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    current_time = pygame.time.get_ticks()
    print(current_time, last_enemy_time)
    if current_time - last_enemy_time > enemy_interval:
        enemies.append(create_enemy())
        last_enemy_time = current_time
        score += 1  # 점수 증가


    enemies = [[x, y + enemy_speed * dt] for x, y in enemies]
    for enemy_e in enemies:
        enemy_e_rect = pygame.Rect(enemy_e[0], enemy_e[1], enemy_width, enemy_height)
        if character_rect.colliderect(enemy_e_rect):
            print("충돌했습니다!")
            running = False
            break

    enemies = [enemy_e for enemy_e in enemies if enemy_e[1] <= window_height]

    window.blit(background, (0, 0))
    window.blit(character, (character_x_pos, character_y_pos))

    for enemy_e in enemies:
        window.blit(enemy, (enemy_e[0], enemy_e[1]))
    score_text = game_font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
