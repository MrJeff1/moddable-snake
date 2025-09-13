import pygame
import random
from mod_api import GameAPI

CELL = 20
WIDTH_CELLS = 32
HEIGHT_CELLS = 24
SCREEN_W = CELL * WIDTH_CELLS
SCREEN_H = CELL * HEIGHT_CELLS

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.speed = 8  # ticks per second
        self.tick_count = 0

        # game state
        midx = WIDTH_CELLS // 2
        midy = HEIGHT_CELLS // 2
        self.snake = [(midx, midy), (midx-1, midy), (midx-2, midy)]
        self.direction = (1, 0)
        self.food = None
        self.spawn_food()

        # event listeners (populated by mods)
        self._listeners = {
            'on_game_start': [],
            'on_tick': [],
            'on_food_eaten': [],
            'on_key': [],
            'on_snake_move': [],
        }

        # create the API wrapper passed to mods
        self.api = GameAPI(self)
        self._called_on_start = False

    # --- event registration (used by ModLoader / mods) ---
    def register(self, event_name, handler):
        if event_name in self._listeners:
            self._listeners[event_name].append(handler)

    def emit(self, event_name, *args, **kwargs):
        for handler in list(self._listeners.get(event_name, [])):
            try:
                handler(self.api, *args, **kwargs)
            except Exception as e:
                # simple error handling per-mod
                print(f"Error in mod handler {handler}:", e)

    # --- game helpers used by mods via API ---
    def spawn_food(self, pos=None):
        if pos:
            self.food = pos
            return
        while True:
            p = (random.randrange(0, WIDTH_CELLS), random.randrange(0, HEIGHT_CELLS))
            if p not in self.snake:
                self.food = p
                return

    def grow(self, amount=1):
        for _ in range(amount):
            tail = self.snake[-1]
            self.snake.append(tail)

    def set_speed(self, speed):
        self.speed = max(1, int(speed))

    # --- main loop ---
    def run(self):
        # call mods' on_game_start
        if not self._called_on_start:
            self.emit('on_game_start')
            self._called_on_start = True

        while self.running:
            dt = self.clock.tick(self.speed)
            self.tick_count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # simple input handling (arrow keys)
                    if event.key == pygame.K_UP:
                        self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.direction = (1, 0)
                    # let mods see the key event too
                    self.emit('on_key', event)

            # move snake
            head = self.snake[0]
            new_head = ((head[0] + self.direction[0]) % WIDTH_CELLS,
                        (head[1] + self.direction[1]) % HEIGHT_CELLS)
            self.snake.insert(0, new_head)
            self.emit('on_snake_move')

            if new_head == self.food:
                # ate food
                self.emit('on_food_eaten', self.food)
                self.spawn_food()
            else:
                # normal move: pop tail
                self.snake.pop()

            # mods tick hook
            self.emit('on_tick')

            # render
            self.screen.fill((10, 10, 10))
            # draw food
            if self.food:
                pygame.draw.rect(self.screen, (200, 60, 60),
                                 (self.food[0]*CELL, self.food[1]*CELL, CELL, CELL))
            # draw snake
            for i, seg in enumerate(self.snake):
                color = (50, 200, 50) if i == 0 else (30, 180, 30)
                pygame.draw.rect(self.screen, color,
                                 (seg[0]*CELL, seg[1]*CELL, CELL-1, CELL-1))

            pygame.display.flip()
        pygame.quit()
