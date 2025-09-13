import os
import importlib.util
import sys

class ModLoader:
    def __init__(self, game, mods_folder='mods'):
        self.game = game
        self.mods_folder = os.path.abspath(mods_folder)
        # ensure mods folder is a package for imports
        if self.mods_folder not in sys.path:
            sys.path.insert(0, self.mods_folder)

    def load_mods(self):
        print('Loading mods from', self.mods_folder)
        for file in os.listdir(self.mods_folder):
            if not file.endswith('.py'):
                continue
            mod_path = os.path.join(self.mods_folder, file)
            mod_name = os.path.splitext(file)[0]
            try:
                spec = importlib.util.spec_from_file_location(mod_name, mod_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                # each mod can register handlers by calling game.register via module-level setup
                # we provide a convention: if mod exposes `setup(game_api)` we'll call it
                if hasattr(module, 'setup'):
                    try:
                        module.setup(self.game.api)
                        print(f'Mod {mod_name} setup() called')
                    except Exception as e:
                        print(f'Error in mod {mod_name} setup():', e)
                else:
                    # fallback: check for functions named on_game_start, on_tick, etc and auto-register
                    for name in ('on_game_start','on_tick','on_food_eaten','on_key','on_snake_move'):
                        if hasattr(module, name):
                            handler = getattr(module, name)
                            # register wrapper so the signature is handler(api, *args)
                            self.game.register(name, handler)
                            print(f'Registered {name} from {mod_name}')
            except Exception as e:
                print(f'Failed to load mod {mod_name}:', e)
