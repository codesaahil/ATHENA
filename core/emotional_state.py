from dataclasses import dataclass


@dataclass
class EmotionalState:
    _happiness: float
    _sadness: float
    _anger: float
    _disgust: float
    _fear: float
    _surprise: float

    @property
    def happiness(self) -> float:
        return self._happiness

    @property
    def sadness(self) -> float:
        return self._sadness

    @property
    def anger(self) -> float:
        return self._anger

    @property
    def disgust(self) -> float:
        return self._disgust

    @property
    def fear(self) -> float:
        return self._fear

    @property
    def surprise(self) -> float:
        return self._surprise

    @happiness.setter
    def happiness(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Happiness should be between 0 and 1")
        self._happiness = value

    @sadness.setter
    def sadness(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Sadness should be between 0 and 1")
        self._sadness = value

    @anger.setter
    def anger(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Anger should be between 0 and 1")
        self._anger = value

    @disgust.setter
    def disgust(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Disgust should be between 0 and 1")
        self._disgust = value

    @fear.setter
    def fear(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Fear should be between 0 and 1")
        self._fear = value

    @surprise.setter
    def surprise(self, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError("Surprise should be between 0 and 1")
        self._surprise = value
