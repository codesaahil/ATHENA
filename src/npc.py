from dataclasses import dataclass
from datetime import datetime

from src.memory import Memory, MemoryUnit
from src.ocean_profile import OceanProfile
from src.emotional_state import EmotionalState
from src.dialogue_generator import generate_response


@dataclass
class IntelligentNPC:
    conversation_memory: Memory
    permanent_memory: Memory
    ocean_profile: OceanProfile
    emotional_state: EmotionalState
    possible_actions: dict

    def respond(self, dialogue: str) -> dict:
        context = {
            "conversation_memory": str(self.conversation_memory),
            "permanent_memory": str(self.permanent_memory),
            "personality": str(self.ocean_profile),
            "emotion": str(self.emotional_state),
            "actions": self.possible_actions,
        }
        response = generate_response(dialogue, context)

        conversation_unit = MemoryUnit(
            timestamp=datetime.now(),
            content=response["response"],
            importance=0.5,
            tags=response["tags"],
        )
        self.conversation_memory.add_memory(conversation_unit)

        return response
