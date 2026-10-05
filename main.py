import sys
import pygame

# Инициализация всех модулей Pygame
pygame.init()

# Настройки окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета (RGB)
DARK_GRAY = (30, 30, 30)

# Создание окна
screen = pygame.display.set_caption("Survival 2D - Step 1")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    running = True

    # Главный игровой цикл
    while running:
        # 1. Обработка событий (закрытие окна, нажатия клавиш)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 2. Отрисовка (пока просто чистый фон)
        screen.fill(DARK_GRAY)

        # Обновление экрана
        pygame.display.flip()

        # Ограничение кадровой частоты
        clock.tick(FPS)

    # Завершение работы
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
