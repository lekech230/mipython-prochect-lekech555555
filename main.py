import pygame
import random

# Инициализация Pygame
pygame.init()

# Настраиваем экран под разрешение телефона
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Цвета
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)

# Игрок (синий квадрат)
player_size = WIDTH // 8
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]

# Враги (красные круги)
enemy_size = WIDTH // 10
enemy_list = []
enemy_speed = 10

score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)


def spawn_enemy():
    x_pos = random.randint(0, WIDTH - enemy_size)
    enemy_list.append([x_pos, -enemy_size])


running = True
while running:
    screen.fill(BLACK)

    # 1. Обработка событий (Управление касанием)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Если палец касается экрана или движется по нему
        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION]:
            # Игрок следует за пальцем по горизонтали
            player_pos[0] = event.pos[0] - player_size // 2

    # 2. Логика врагов
    if random.random() < 0.05:  # Шанс появления врага
        spawn_enemy()

    for idx, enemy_pos in enumerate(enemy_list):
        # Двигаем врага вниз
        enemy_pos[1] += enemy_speed

        # Проверка столкновения
        if (enemy_pos[1] + enemy_size > player_pos[1] and
                enemy_pos[1] < player_pos[1] + player_size):
            if (enemy_pos[0] + enemy_size > player_pos[0] and
                    enemy_pos[0] < player_pos[0] + player_size):
                # Коллизия! Сбрасываем игру
                score = 0
                enemy_list.clear()
                enemy_speed = 10

        # Удаление врагов за экраном
        if enemy_pos[1] > HEIGHT:
            enemy_list.pop(idx)
            score += 1
            enemy_speed += 0.2  # Усложняем игру

    # 3. Отрисовка
    # Рисуем игрока
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    # Рисуем врагов
    for enemy_pos in enemy_list:
        pygame.draw.circle(screen, RED, (enemy_pos[0] + enemy_size // 2, enemy_pos[1] + enemy_size // 2),
                           enemy_size // 2)

    # Текст счета
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (30, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
