from dataclasses import dataclass


@dataclass
class OceanProfile:
    _openness: float
    _conscientiousness: float
    _extraversion: float
    _agreeableness: float
    _neuroticism: float

    def __str__(self) -> str:
        return (
            f"OceanProfile("
            f"openness={self._openness}, "
            f"conscientiousness={self._conscientiousness}, "
            f"extraversion={self._extraversion}, "
            f"agreeableness={self._agreeableness}, "
            f"neuroticism={self._neuroticism})"
        )

    def _validate_trait(self, value: float) -> float:
        if not 0 <= value <= 1:
            raise ValueError("Trait values should be between 0 and 1")
        return value

    @property
    def openness(self) -> float:
        return self._openness

    @openness.setter
    def openness(self, value: float) -> None:
        self._openness = self._validate_trait(value)

    @property
    def conscientiousness(self) -> float:
        return self._conscientiousness

    @conscientiousness.setter
    def conscientiousness(self, value: float) -> None:
        self._conscientiousness = self._validate_trait(value)

    @property
    def extraversion(self) -> float:
        return self._extraversion

    @extraversion.setter
    def extraversion(self, value: float) -> None:
        self._extraversion = self._validate_trait(value)

    @property
    def agreeableness(self) -> float:
        return self._agreeableness

    @agreeableness.setter
    def agreeableness(self, value: float) -> None:
        self._agreeableness = self._validate_trait(value)

    @property
    def neuroticism(self) -> float:
        return self._neuroticism

    @neuroticism.setter
    def neuroticism(self, value: float) -> None:
        self._neuroticism = self._validate_trait(value)
