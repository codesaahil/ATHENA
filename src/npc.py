from dataclasses import dataclass
from src.memory import Memory
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

    conversation_memory: list
    permanent_memory: Memory
    ocean_profile: OceanProfile
    emotional_state: EmotionalState
    possible_actions: dict

    def _update_emotion(self, emotion: dict):
        self.emotional_state.happiness = emotion["happiness"]
        self.emotional_state.fear = emotion["fear"]
        self.emotional_state.anger = emotion["anger"]
        self.emotional_state.disgust = emotion["disgust"]
        self.emotional_state.sadness = emotion["sadness"]
        self.emotional_state.surprise = emotion["surprise"]

    def talk(self, dialogue: str) -> dict:
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
            "permanent_memory": str(self.permanent_memory),
            "personality": str(self.ocean_profile),
            "emotion": str(self.emotional_state),
            "actions": self.possible_actions,
        }

        # Add the PC dialogue to the conversation memory
        self.conversation_memory.append(f"pc: {dialogue}")

        # Generate a response using the provided dialogue and context
        response = generate_response(dialogue, context)

        # Add the generated response to the conversation memory
        self.conversation_memory.append(f"npc: {response["dialogue"]}")

        # Update emotion of the NPC.
        self._update_emotion(response["emotion"])

        return response  # Return the generated response
