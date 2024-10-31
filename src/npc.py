from dataclasses import dataclass
from datetime import datetime
from src.memory import Memory, MemoryUnit
from src.ocean_profile import OceanProfile
from src.emotional_state import EmotionalState
from src.dialogue_generator import generate_response


@dataclass
class IntelligentNPC:
    """
    A class representing an intelligent non-player character (NPC) capable of responding to dialogue.

    Attributes:
        conversation_memory (Memory): The memory of the current conversation.
        permanent_memory (Memory): The long-term memory of the NPC.
        ocean_profile (OceanProfile): The personality profile of the NPC based on the OCEAN model.
        emotional_state (EmotionalState): The current emotional state of the NPC.
        possible_actions (dict): A dictionary of actions that the NPC can take.
    """

    conversation_memory: Memory
    permanent_memory: Memory
    ocean_profile: OceanProfile
    emotional_state: EmotionalState
    possible_actions: dict

    def respond(self, dialogue: str) -> dict:
        """
        Generates a response to a given dialogue and updates the NPC's memory.

        Args:
            dialogue (str): The input dialogue from the user.

        Returns:
            dict: A dictionary containing the NPC's response and associated metadata.
        """
        # Create a context dictionary that includes current state and memory for response generation
        context = {
            "conversation_memory": self.conversation_memory,
            "permanent_memory": self.permanent_memory,
            "personality": self.ocean_profile,
            "emotion": self.emotional_state,
            "actions": self.possible_actions,
        }

        # Generate a response using the provided dialogue and context
        response = generate_response(dialogue, context)

        # Add the generated response to the conversation memory
        self.conversation_memory.add_memory(
            MemoryUnit(
                timestamp=datetime.now(),  # Current timestamp
                content=response.get("response"),  # Extract response content
                importance=response.get(
                    "importance", 0.5
                ),  # Default importance if not specified
                tags=response.get("tags", []),  # Extract tags if provided
            )
        )

        return response  # Return the generated response
