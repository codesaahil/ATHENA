from dataclasses import dataclass


@dataclass
class EmotionalState:
    _happiness: float
    _sadness: float
    _anger: float
    _disgust: float
    _fear: float
    _surprise: float

    def __str__(self) -> str:
        return (
            f"EmotionalState("
            f"happiness={self._happiness}, "
            f"sadness={self._sadness}, "
            f"anger={self._anger}, "
            f"disgust={self._disgust}, "
            f"fear={self._fear}, "
            f"surprise={self._surprise})"
        )

    def _validate_emotion(self, value: float) -> float:
        if not 0 <= value <= 1:
            raise ValueError("Emotion values should be between 0 and 1")
        return value

    @property
    def happiness(self) -> float:
        return self._happiness

    @happiness.setter
    def happiness(self, value: float) -> None:
        self._happiness = self._validate_emotion(value)

    @property
    def sadness(self) -> float:
        return self._sadness

    @sadness.setter
    def sadness(self, value: float) -> None:
        self._sadness = self._validate_emotion(value)

    @property
    def anger(self) -> float:
        return self._anger

    @anger.setter
    def anger(self, value: float) -> None:
        self._anger = self._validate_emotion(value)

    @property
    def disgust(self) -> float:
        return self._disgust

    @disgust.setter
    def disgust(self, value: float) -> None:
        self._disgust = self._validate_emotion(value)

    @property
    def fear(self) -> float:
        return self._fear

    @fear.setter
    def fear(self, value: float) -> None:
        self._fear = self._validate_emotion(value)

    @property
    def surprise(self) -> float:
        return self._surprise

    @surprise.setter
    def surprise(self, value: float) -> None:
        self._surprise = self._validate_emotion(value)
