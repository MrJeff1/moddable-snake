class GameAPI:
    """A thin, controlled API object passed to mods.
    Mods should only use these helper methods instead of poking internals.
    """
    def __init__(self, game):
        self._game = game

    # read-only snapshot of game state
    def get_state(self):
        return {
            'snake': list(self._game.snake),
            'food': self._game.food,
            'speed': self._game.speed,
            'tick': self._game.tick_count,
        }

    def spawn_food(self, pos=None):
        self._game.spawn_food(pos)

    def grow(self, amount=1):
        self._game.grow(amount)

    def set_speed(self, speed):
        self._game.set_speed(speed)

    def register(self, event_name, handler):
        # allow mods to register callbacks dynamically
        self._game.register(event_name, handler)

    def log(self, *args):
        print('[MOD]', *args)
