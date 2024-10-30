from dataclasses import dataclass

from core.emotional_state import EmotionalState
from core.ocean_profile import OceanProfile


@dataclass
class Personality:
    emotionalState: EmotionalState
    oceanProfile: OceanProfile
