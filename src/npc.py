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
            "conversation_memory": self.conversation_memory,
            "permanent_memory": self.permanent_memory,
            "personality": self.ocean_profile,
            "emotion": self.emotional_state,
            "actions": self.possible_actions,
        }

        response = generate_response(dialogue, context)

        self.conversation_memory.add_memory(
            MemoryUnit(
                timestamp=datetime.now(),
                content=response.get("response"),
                importance=response.get("importance", 0.5),
                tags=response.get("tags", []),
            )
        )

        return response
