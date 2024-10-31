from dataclasses import dataclass


@dataclass
class OceanProfile:
    """
    A class to represent the Big Five personality traits (OCEAN) of an NPC.

    Attributes:
        _openness (float): A trait reflecting imagination and insight.
        _conscientiousness (float): A trait reflecting organization and dependability.
        _extraversion (float): A trait reflecting sociability and assertiveness.
        _agreeableness (float): A trait reflecting kindness and cooperativeness.
        _neuroticism (float): A trait reflecting emotional stability and moodiness.
    """

    _openness: float
    _conscientiousness: float
    _extraversion: float
    _agreeableness: float
    _neuroticism: float

    def __str__(self) -> str:
        """
        Returns a string representation of the OceanProfile instance.

        Returns:
            str: A formatted string showing the values of the OCEAN traits.
        """
        return (
            f"OceanProfile("
            f"openness={self._openness}, "
            f"conscientiousness={self._conscientiousness}, "
            f"extraversion={self._extraversion}, "
            f"agreeableness={self._agreeableness}, "
            f"neuroticism={self._neuroticism})"
        )

    def _validate_trait(self, value: float) -> float:
        """
        Validates that the trait value is between 0 and 1.

        Args:
            value (float): The value to validate.

        Raises:
            ValueError: If the value is not between 0 and 1.

        Returns:
            float: The validated value.
        """
        if not 0 <= value <= 1:
            raise ValueError("Trait values should be between 0 and 1")
        return value

    @property
    def openness(self) -> float:
        """
        Gets the openness trait value.

        Returns:
            float: The openness trait value.
        """
        return self._openness

    @openness.setter
    def openness(self, value: float) -> None:
        """
        Sets the openness trait value after validation.

        Args:
            value (float): The value to set for openness.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._openness = self._validate_trait(value)

    @property
    def conscientiousness(self) -> float:
        """
        Gets the conscientiousness trait value.

        Returns:
            float: The conscientiousness trait value.
        """
        return self._conscientiousness

    @conscientiousness.setter
    def conscientiousness(self, value: float) -> None:
        """
        Sets the conscientiousness trait value after validation.

        Args:
            value (float): The value to set for conscientiousness.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._conscientiousness = self._validate_trait(value)

    @property
    def extraversion(self) -> float:
        """
        Gets the extraversion trait value.

        Returns:
            float: The extraversion trait value.
        """
        return self._extraversion

    @extraversion.setter
    def extraversion(self, value: float) -> None:
        """
        Sets the extraversion trait value after validation.

        Args:
            value (float): The value to set for extraversion.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._extraversion = self._validate_trait(value)

    @property
    def agreeableness(self) -> float:
        """
        Gets the agreeableness trait value.

        Returns:
            float: The agreeableness trait value.
        """
        return self._agreeableness

    @agreeableness.setter
    def agreeableness(self, value: float) -> None:
        """
        Sets the agreeableness trait value after validation.

        Args:
            value (float): The value to set for agreeableness.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._agreeableness = self._validate_trait(value)

    @property
    def neuroticism(self) -> float:
        """
        Gets the neuroticism trait value.

        Returns:
            float: The neuroticism trait value.
        """
        return self._neuroticism

    @neuroticism.setter
    def neuroticism(self, value: float) -> None:
        """
        Sets the neuroticism trait value after validation.

        Args:
            value (float): The value to set for neuroticism.

        Raises:
            ValueError: If the value is not between 0 and 1.
        """
        self._neuroticism = self._validate_trait(value)
