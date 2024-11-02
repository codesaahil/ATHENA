from dataclasses import dataclass


def _validate_emotion(value: float) -> float:
    """
    Validates that the emotion value is within the acceptable range (0.0 to 1.0).

    Args:
        value (float): The emotion value to validate.

    Raises:
        ValueError: If the value is not between 0 and 1.

    Returns:
        float: The validated emotion value.
    """
    if not 0 <= value <= 1:
        raise ValueError("Emotion values should be between 0 and 1")
    return value


@dataclass
class EmotionalState:
    """
    A class to represent the emotional state of an NPC.

    Attributes:
        _happiness (float): The happiness level, between 0.0 and 1.0.
        _sadness (float): The sadness level, between 0.0 and 1.0.
        _anger (float): The anger level, between 0.0 and 1.0.
        _disgust (float): The disgust level, between 0.0 and 1.0.
        _fear (float): The fear level, between 0.0 and 1.0.
        _surprise (float): The surprise level, between 0.0 and 1.0.
    """

    _happiness: float
    _sadness: float
    _anger: float
    _disgust: float
    _fear: float
    _surprise: float

    def __str__(self) -> str:
        """
        Returns a string representation of the EmotionalState object.

        Returns:
            str: A formatted string showing the emotional states.
        """
        return (
            f"EmotionalState("
            f"happiness={self._happiness}, "
            f"sadness={self._sadness}, "
            f"anger={self._anger}, "
            f"disgust={self._disgust}, "
            f"fear={self._fear}, "
            f"surprise={self._surprise})"
        )

    @property
    def happiness(self) -> float:
        """
        Gets the happiness level of the NPC.

        Returns:
            float: The happiness level.
        """
        return self._happiness

    @happiness.setter
    def happiness(self, value: float) -> None:
        """
        Sets the happiness level of the NPC after validating the value.

        Args:
            value (float): The new happiness level to set.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._happiness = _validate_emotion(value)

    @property
    def sadness(self) -> float:
        """
        Gets the sadness level of the NPC.

        Returns:
            float: The sadness level.
        """
        return self._sadness

    @sadness.setter
    def sadness(self, value: float) -> None:
        """
        Sets the sadness level of the NPC after validating the value.

        Args:
            value (float): The new sadness level to set.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._sadness = _validate_emotion(value)

    @property
    def anger(self) -> float:
        """
        Gets the anger level of the NPC.

        Returns:
            float: The anger level.
        """
        return self._anger

    @anger.setter
    def anger(self, value: float) -> None:
        """
        Sets the anger level of the NPC after validating the value.

        Args:
            value (float): The new anger level to set.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._anger = _validate_emotion(value)

    @property
    def disgust(self) -> float:
        """
        Gets the disgust level of the NPC.

        Returns:
            float: The disgust level.
        """
        return self._disgust

    @disgust.setter
    def disgust(self, value: float) -> None:
        """
        Sets the disgust level of the NPC after validating the value.

        Args:
            value (float): The new disgust level to set.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._disgust = _validate_emotion(value)

    @property
    def fear(self) -> float:
        """
        Gets the fear level of the NPC.

        Returns:
            float: The fear level.
        """
        return self._fear

    @fear.setter
    def fear(self, value: float) -> None:
        """
        Sets the fear level of the NPC after validating the value.

        Args:
            value (float): The new fear level to set.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._fear = _validate_emotion(value)

    @property
    def surprise(self) -> float:
        """
        Gets the surprise level of the NPC.

        Returns:
            float: The surprise level.
        """
        return self._surprise

    @surprise.setter
    def surprise(self, value: float) -> None:
        """
        Sets the surprise level of the NPC after validating the value.

        Args:
            value (float): The new surprise level to set.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._surprise = _validate_emotion(value)
