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