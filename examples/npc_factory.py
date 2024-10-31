from typing import Optional

from src.npc import IntelligentNPC
from src.emotional_state import EmotionalState
from src.ocean_profile import OceanProfile
from src.memory import Memory


class IntelligentNPCFactory:
    @staticmethod
    def create_npc(
        memory: Optional[Memory] = None,
        openness: float = 0.5,
        conscientiousness: float = 0.5,
        extraversion: float = 0.5,
        agreeableness: float = 0.5,
        neuroticism: float = 0.5,
        happiness: float = 0.5,
        sadness: float = 0.5,
        anger: float = 0.5,
        disgust: float = 0.5,
        fear: float = 0.5,
        surprise: float = 0.5,
    ) -> IntelligentNPC:
        """
        Factory method to create an IntelligentNPC with given parameters.
        Default values are set to 0.5 for all attributes if not provided.
        """
        # Create default memory if not provided
        if memory is None:
            memory = Memory([], 100, 0.01)  # Assuming Memory has a default initializer

        # Create OceanProfile and EmotionalState objects
        ocean_profile = OceanProfile(
            openness, conscientiousness, extraversion, agreeableness, neuroticism
        )
        emotional_state = EmotionalState(
            happiness, sadness, anger, disgust, fear, surprise
        )

        # Create and return the IntelligentNPC
        return IntelligentNPC(memory, ocean_profile, emotional_state)

npc = IntelligentNPCFactory.create_npc(openness=0.8, extraversion=0.7, happiness=0.9)

while True:
    inp = input("Enter your response")
    print(npc.respond(inp))
