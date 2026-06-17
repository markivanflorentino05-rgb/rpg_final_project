from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACTION
# ==========================================
# We create an abstract base class that acts as a blueprint.
# You cannot create an instance of BaseCharacter directly.
class BaseCharacter(ABC):
    def __init__(self, character_name, base_health):
        self.character_name = character_name