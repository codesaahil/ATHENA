from typing import Optional
from src.npc import IntelligentNPC
from src.emotional_state import EmotionalState
from src.ocean_profile import OceanProfile
from src.memory import Memory


class IntelligentNPCFactory:
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
        memory = memory or Memory(
            [],
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


npc = IntelligentNPCFactory.create_npc(openness=0.8, extraversion=0.7, happiness=0.9)

while True:
    inp = input("Enter your response: ")
    print(npc.respond(inp))
