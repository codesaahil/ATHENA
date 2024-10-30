from dataclasses import dataclass

from src.emotional_state import EmotionalState
from src.ocean_profile import OceanProfile


@dataclass
class Personality:
    emotionalState: EmotionalState
    oceanProfile: OceanProfile
