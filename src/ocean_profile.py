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

    @property
    def openness(self) -> float:
        return self._openness

    @property
    def conscientiousness(self) -> float:
        return self._conscientiousness

    @property
    def extraversion(self) -> float:
        return self._extraversion

    @property
    def agreeableness(self) -> float:
        return self._agreeableness

    @property
    def neuroticism(self) -> float:
        return self._neuroticism

    @openness.setter
    def openness(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Openness should be between 0 and 1")
        self._openness = value

    @conscientiousness.setter
    def conscientiousness(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Conscientiousness should be between 0 and 1")
        self._conscientiousness = value

    @extraversion.setter
    def extraversion(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Extraversion should be between 0 and 1")
        self._extraversion = value

    @agreeableness.setter
    def agreeableness(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Agreeableness should be between 0 and 1")
        self._agreeableness = value

    @neuroticism.setter
    def neuroticism(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Neuroticism should be between 0 and 1")
        self._neuroticism = value
