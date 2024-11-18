import pygame
from pygame.mixer_music import get_pos
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))

        def init_grid(g_length, g_height):
            for g_length in range(0, 641, 32):
                for g_height in range(0, 513, 32):
                    pygame.draw.line(screen, "black", (g_length, 0), (g_length, g_height))
                    pygame.draw.line(screen, "black", (0, g_height), (g_length, g_height))

        def init_mole(m_x, m_y):
            m_x *= 32
            m_y *= 32
            screen.blit(mole_image, mole_image.get_rect(topleft=(m_x, m_y)))


        clock = pygame.time.Clock()
        running = True
        m_x, m_y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    grid_x, grid_y = x // 32, y // 32
                    if grid_x == m_x and grid_y == m_y:
                        m_x = random.randint(0, 19)
                        m_y = random.randint(0, 15)

            screen.fill("light green")
            init_grid(0, 0)
            init_mole(m_x, m_y)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
