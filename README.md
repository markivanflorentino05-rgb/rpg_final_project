# Open-World RPG Game — OOP Implementation

## Project Overview
This repository contains a final project that adapts and enhances the core mechanics of an open-world RPG game to demonstrate the **Four Pillars of Object-Oriented Programming (OOP)** in Python. 

The primary goal of this project is to showcase how abstraction, encapsulation, inheritance, and polymorphism can be used to write clean, maintainable, and scalable game logic.

### Credits
The base architectural concept and inspiration for this project are derived from the OpenGenus community.
* **Original Repository:** [OpenGenus/Open-World-RPG-Game-in-Python](https://github.com/OpenGenus/Open-World-RPG-Game-in-Python)

---

## Code Quality Standards
This project strictly adheres to the following clean-coding constraints:
* **Naming Convention:** All functions, methods, variables, and instances are written strictly using `snake_case`.
* **Descriptive Variables:** Absolutely zero single-letter variables (e.g., `i`, `x`, `p`) are used anywhere in the codebase to ensure self-documenting code.

---

## OOP Pillars Implemented

### 1. Abstraction
Using Python's built-in `abc` (Abstract Base Class) module, we created a blueprint class called `BaseCharacter`. 
* It defines mandatory structural methods like `display_character_stats()` and `perform_attack()`.
* You cannot instantiate `BaseCharacter` directly, ensuring it acts purely as a foundational contract for all future in-game characters.

### 2. Encapsulation
To protect critical character data from unintended external manipulation, internal attributes are strictly encapsulated.
* Attributes like health status (`__current_health`) and life status (`__is_alive`) utilize double underscores to make them private.
* External game loops must safely interact with these attributes using specific getter and setter methods like `get_health_status()` and `take_damage()`.

### 3. Inheritance
Instead of rewriting redundant code for every unique entity in the game, the project utilizes inheritance.
* Subclasses like `Wizard` and `Goblin` automatically inherit foundational properties and systems (such as the health and damage systems) directly from the `BaseCharacter` parent class using `super().__init__()`.

### 4. Polymorphism
Different entities respond uniquely to the exact same commands. 
* While both `Wizard` and `Goblin` share the exact same method names (`perform_attack`), they morph their execution. The `Wizard` calculates magic-based multiplier scaling, while the `Goblin` scales via physical strength modifiers.

---

## How to Run the Demo
1. Ensure you have Python 3.x installed.
2. Clone the repository or navigate to the directory via Git Bash.
3. Run the demonstration script using:
```bash
   python rpg_oop_demo.py
