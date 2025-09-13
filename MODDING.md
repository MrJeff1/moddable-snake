# Moddable Snake - Complete Modding Guide 🐍

Welcome to the complete modding guide for Moddable Snake!

This guide covers everything you need to know to create mods, customize the game, and share your creations.

---

## 1. Introduction to Modding

- Mods are Python scripts located in the `mods/` folder.
- Each `.py` file is loaded automatically when the game starts.
- Mods define a `register(mod_api)` function where you hook into the game.

Example skeleton:

```python
def register(mod_api):
    # Your mod code here
    pass
```

---

## 2. The `mod_api` System

The `mod_api` allows mods to interact with the game safely.

### Actions

1. **Override a feature**:

```python
mod_api.override(hook_name, function)
```

- `hook_name`: the feature to override (e.g., "snake_speed")
- `function`: Python function that returns the desired value

Example:

```python
def register(mod_api):
    def fast_speed(default_speed):
        return default_speed * 2
    mod_api.override("snake_speed", fast_speed)
```

2. **Hook into an event**:

```python
mod_api.event(event_name, function)
```

- `event_name`: event like "on_apple_eaten"
- `function`: called when the event happens

Example:

```python
def register(mod_api):
    def cheer_event(score):
        print("Yay! You ate an apple! Your score:", score)
    mod_api.event("on_apple_eaten", cheer_event)
```

---

## 3. Available Hooks and Events

### Visual Overrides

- `snake_head_color(default_color)` → `(r,g,b)`
- `snake_body_color(default_color)` → `(r,g,b)`
- `apple_color(default_color)` → `(r,g,b)`
- `background_color(default_color)` → `(r,g,b)`

### Gameplay Overrides

- `snake_speed(default_speed)` → `int`
- `growth_amount(default_growth)` → `int`

### Events

- `on_apple_eaten(score)` – triggered when the snake eats an apple
- `on_game_over(final_score)` – triggered when the game ends
- `on_tick(frame_count)` – runs every frame

---

## 4. Creating Your First Mod

### Example 1: Change Snake Head Color

```python
def register(mod_api):
    def blue_head(default_color):
        return (50, 150, 255)
    mod_api.override("snake_head_color", blue_head)
```

### Example 2: Double Speed

```python
def register(mod_api):
    def fast_snake(default_speed):
        return default_speed * 2
    mod_api.override("snake_speed", fast_snake)
```

### Example 3: Party Mode (random colors)

```python
import random

def register(mod_api):
    def rainbow_body(default_color):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    mod_api.override("snake_body_color", rainbow_body)
```

---

## 5. Combining Features in One Mod

```python
def register(mod_api):
    def crazy_speed(default_speed):
        return default_speed + 5

    def apple_glow(default_color):
        return (255, 100, 100)

    def cheer(score):
        print("Apple eaten! Score =", score)

    mod_api.override("snake_speed", crazy_speed)
    mod_api.override("apple_color", apple_glow)
    mod_api.event("on_apple_eaten", cheer)
```

---

## 6. Debugging Mods

- Syntax errors are printed to the terminal.
- If a mod crashes, the game may stop — check the console log.
- Test mods one at a time by temporarily moving others out of `mods/`.
- Add `print()` statements to verify functions run.

---

## 7. Best Practices

✅ Keep each mod in its own file.
✅ Add comments at the top describing the mod purpose.
✅ Avoid infinite loops — they freeze the game.
✅ Test changes incrementally.
✅ Share mods as single `.py` files. 

---

## 8. Advanced Modding Ideas

- Shrink the snake instead of growing. 
- Change background color after eating an apple. 
- Add sound effects using `pygame.mixer`. 
- Create a “hardcore mode” with increasing speed. 
- Track high scores in a file. 

---

## 9. Sharing Mods

1. Copy the `.py` file from `mods/`. 
2. Send it to a friend. 
3. They place it in their `mods/` folder. 
4. Restart the game. Mod works immediately.

---

## 10. Future Modding Roadmap

- Custom game modes 
- Custom power-ups 
- New map generation logic 
- Mod metadata (name, version, author) 
