from datetime import datetime
from typing import Optional
from src.npc import IntelligentNPC
from src.emotional_state import EmotionalState
from src.ocean_profile import OceanProfile
from src.memory import Memory, MemoryUnit


class IntelligentNPCFactory:
    """
    A factory class for creating IntelligentNPC instances.

    Attributes:
        DEFAULT_MEMORY_CAPACITY (int): Default capacity for the NPC's memory.
        DEFAULT_DECAY_RATE (float): Default decay rate for the NPC's memory.
        DEFAULT_ACTIONS (dict): Default actions the NPC can perform based on emotional context.
    """

    DEFAULT_MEMORY_CAPACITY = 100
    DEFAULT_DECAY_RATE = 0.01
    DEFAULT_ACTIONS = {
        "laugh": "if something is funny",
        "smile": "if the conversation is normal",
    }

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
        Creates and returns an instance of IntelligentNPC with specified traits and memory.

        Args:
            memory (Optional[Memory]): An optional Memory instance to be associated with the NPC.
                If not provided, a default Memory instance is created.
            openness (float): The openness trait of the NPC (0 to 1). Default is 0.5.
            conscientiousness (float): The conscientiousness trait of the NPC (0 to 1). Default is 0.5.
            extraversion (float): The extraversion trait of the NPC (0 to 1). Default is 0.5.
            agreeableness (float): The agreeableness trait of the NPC (0 to 1). Default is 0.5.
            neuroticism (float): The neuroticism trait of the NPC (0 to 1). Default is 0.5.
            happiness (float): The happiness level of the NPC (0 to 1). Default is 0.5.
            sadness (float): The sadness level of the NPC (0 to 1). Default is 0.5.
            anger (float): The anger level of the NPC (0 to 1). Default is 0.5.
            disgust (float): The disgust level of the NPC (0 to 1). Default is 0.5.
            fear (float): The fear level of the NPC (0 to 1). Default is 0.5.
            surprise (float): The surprise level of the NPC (0 to 1). Default is 0.5.

        Returns:
            IntelligentNPC: A newly created IntelligentNPC instance.

        Example:
            npc = IntelligentNPCFactory.create_npc(openness=0.8, extraversion=0.7, happiness=0.9)
        """
        memory = memory or Memory(
            [
                MemoryUnit(
                    datetime.now(),
                    "My name is Ethan. I am a castle blacksmith. I sell weapons and armor.",
                    1.0,
                    [],
                )
            ],
            IntelligentNPCFactory.DEFAULT_MEMORY_CAPACITY,
            IntelligentNPCFactory.DEFAULT_DECAY_RATE,
        )
        conversation_memory = Memory(
            [],
            IntelligentNPCFactory.DEFAULT_MEMORY_CAPACITY,
            IntelligentNPCFactory.DEFAULT_DECAY_RATE,
        )

        ocean_profile = OceanProfile(
            openness, conscientiousness, extraversion, agreeableness, neuroticism
        )
        emotional_state = EmotionalState(
            happiness, sadness, anger, disgust, fear, surprise
        )

        return IntelligentNPC(
            conversation_memory,
            memory,
            ocean_profile,
            emotional_state,
            IntelligentNPCFactory.DEFAULT_ACTIONS,
        )


# Example usage of the IntelligentNPCFactory
npc = IntelligentNPCFactory.create_npc(openness=0.8, extraversion=0.7, happiness=0.9)
