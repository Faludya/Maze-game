# 🌀 Maze Game — OOP Project

This project is a **maze-based adventure game** built using **Object-Oriented Programming (OOP)** principles.  
The player must navigate a labyrinth, collect items, fight enemies, and ultimately reach the exit.

---

## 🎮 Gameplay Overview
- The player starts at a random position in the maze.  
- The goal is to **find the exit** while avoiding or defeating enemies.  
- Along the way, the player can find:
  - **Weapons** (Boomstick `(`, Laser `!`, Phoenix Blaster `:`)  
  - **Coins** (`*`)  
  - **Teleporters** (`O`)  
- **Enemies** (`E`) roam the maze and can defeat the player if unprepared.  

⚔️ **Combat Rule**:  
If an enemy is adjacent and the player has a weapon, they **must fight**.  
- Winning costs: lose 1 weapon + 100 health.  
- Health starts at **201**, enough for 2 battles.  
- If the player has no weapon → the game is lost.  
- Enemies respawn at their starting positions after being killed.  

---

## ⌨️ Commands
- `n`, `s`, `e`, `w` → Move **north, south, east, west**  
- `fight` → Fight an adjacent enemy (if armed)  
- `help` → Show available commands  
- `save` → Save current game state  
- `load` → Load a saved game  
- `quit` → Exit the game  

---

## 🏗️ Main Modules

### 🔹 Labyrinth
- Loads and stores the maze (`labyrinth.txt`).  
- Handles save/load functionality (`save.txt`).  
- Displays the maze and introduction menu.

### 🔹 Items
- Manages items: **coins, weapons, teleporters**.  
- Provides mechanics for picking up items, teleporting, and weapon handling.

### 🔹 Directions
- Handles **player movement**.  
- Updates player position and interacts with items in the maze.  

### 🔹 Player
- Manages **health** and **game state**.  
- Handles combat, game-over conditions, and printing player status.

### 🔹 Enemy
- Represents maze enemies.  
- Moves randomly while avoiding walls/teleporters.  
- Respawns at starting position when defeated.

### 🔹 Main
- Initializes the game.  
- Loads either a **new game** or **saved game**.  
- Runs the main loop until win/lose conditions are met.

---

## 📊 Symbols in the Maze
| Symbol | Meaning            |
|--------|--------------------|
| `X`    | Wall               |
| ` `    | Free space         |
| `(`    | Boomstick weapon   |
| `!`    | Laser weapon       |
| `:`    | Phoenix Blaster    |
| `*`    | Coin               |
| `O`    | Teleporter         |
| `P`    | Player             |
| `E`    | Enemy              |

---

## 🚀 How to Run
1. Make sure you have Python installed.  
2. Run the game:
```bash
python main.py
```
3. Choose from the menu:
- Start new game
- Load saved game
- Quit

  ### 🧩 Example

  Start of a new game:
  ```bash
P   *   X   O   E
X   X   X   X   X
    (   :   !   *
```



