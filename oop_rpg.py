from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACTION
# ==========================================
# We create an abstract base class that acts as a blueprint.
# You cannot create an instance of BaseCharacter directly.
class BaseCharacter(ABC):
    def __init__(self, character_name, base_health):
        self.character_name = character_name

        # ==========================================
        # 2. ENCAPSULATION
        # ==========================================
        # Using double underscores (__) hides these attributes from the outside.
        # They can only be modified through the class's methods (getters/setters).
        self.__current_health = base_health
        self.__is_alive = True

    @abstractmethod
    def display_character_stats(self):
        pass

    @abstractmethod
    def perform_attack(self):
        pass

    # Getter method to safely access private data
    def get_health_status(self):
        return self.__current_health

    # Setter method to safely modify private data
    def take_damage(self, damage_amount):
        if damage_amount > 0:
            self.__current_health -= damage_amount
            if self.__current_health <= 0:
                self.__current_health = 0
                self.__is_alive = False

    def check_if_alive(self):
        return self.__is_alive

# ==========================================
# 3. INHERITANCE
# ==========================================
# The Wizard and Goblin classes inherit from the BaseCharacter class.
# They get all the methods and attributes of the parent class automatically.
class Wizard(BaseCharacter):
    def __init__(self, character_name, magic_power):
        # Calling the parent class's constructor
        super().__init__(character_name, base_health=100)
        self.magic_power = magic_power

    # ==========================================
    # 4. POLYMORPHISM
    # ==========================================
    # Both child classes share the same method names (display_character_stats, perform_attack)
    # but they behave differently based on the specific class calling them.
    def display_character_stats(self):
        print(f"Wizard: {self.character_name} | Health: {self.get_health_status()} | Magic: {self.magic_power}")

    def perform_attack(self):
        print(f"{self.character_name} casts a fireball!")
        return self.magic_power * 1.5

class Goblin(BaseCharacter):
    def __init__(self, character_name, physical_strength):
        super().__init__(character_name, base_health=120)
        self.physical_strength = physical_strength

    # Overriding the abstract methods differently (Polymorphism)
    def display_character_stats(self):
        print(f"Goblin: {self.character_name} | Health: {self.get_health_status()} | Strength: {self.physical_strength}")

    def perform_attack(self):
        print(f"{self.character_name} swings a heavy club!")
        return self.physical_strength * 1.2

# ==========================================
# DEMONSTRATION RUN
# ==========================================
if __name__ == "__main__":
    player_one = Wizard(character_name="Merlin", magic_power=50)
    enemy_character = Goblin(character_name="Grok", physical_strength=40)

    player_one.display_character_stats()
    enemy_character.display_character_stats()

    attack_damage = player_one.perform_attack()
    enemy_character.take_damage(damage_amount=attack_damage)

    print("\n--- After the Attack ---")
    enemy_character.display_character_stats()