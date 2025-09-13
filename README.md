# Moddable Snake (Python + Pygame)

A simple Snake game with modding support. Mods are Python scripts placed in the `mods/` folder.

## Quick start

### Linux / macOS
```bash
./install.sh   # sets up venv + installs pygame
./run.sh       # runs the game
```

### Windows
```bat
install.bat    # sets up venv + installs pygame
run.bat        # runs the game
```

> Scripts automatically use `python3`. If your system uses a different command (like `py` on Windows), edit the `.bat`/`.sh` accordingly.

## Manual setup (optional)
If you prefer to do it yourself:

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 main.py
```

## Modding
Mods live in the `mods/` folder. Check `example_mod.py` to see how to change game behavior.
