import pygame
import pygame_gui
import agent
import snake_game_human


pygame.init()

pygame.display.set_caption('Snake Game')
window_surface = pygame.display.set_mode((840, 525))

background = pygame.Surface((840, 525))
# background.fill(pygame.Color('#000000'))
bg = pygame.image.load("image/bg.png")
manager = pygame_gui.UIManager((840, 525))

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 205), (200, 50)),
                                            text='Start training with AI',
                                            manager=manager)
human_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 265), (200, 50)),
                                            text='Play as human',
                                            manager=manager)


clock = pygame.time.Clock()

is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                agent.train()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == human_button:
                snake_game_human.SnakeGame.start_game()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(bg, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
