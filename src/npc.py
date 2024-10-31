from dataclasses import dataclass

from src.memory import Memory
from src.ocean_profile import OceanProfile
from src.emotional_state import EmotionalState
from src.dialogue_generator import generate_response


@dataclass
class IntelligentNPC:
    memory: Memory
    ocean_profile: OceanProfile
    emotional_state: EmotionalState
    possible_actions: dict

    def respond(self, dialogue: str) -> dict:
        context = {
            "memory": str(self.memory),
            "personality": str(self.ocean_profile),
            "emotion": str(self.emotional_state),
            "actions": self.possible_actions
        }
        response = generate_response(dialogue, context)

        return response
