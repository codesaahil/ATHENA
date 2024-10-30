from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class MemoryUnit:
    timestamp: datetime
    content: str
    importance: float
    tags: List[str]


@dataclass
class Memory:
    memories: List[MemoryUnit]
    capacity: int
    decay_rate: float

    def add_memory(self, memory_unit: MemoryUnit) -> None:
        if len(self.memories) >= self.capacity:
            self.clean_memories()
        self.memories.append(memory_unit)

    def clean_memories(self) -> None:
        min_importance: float = float(
            "inf"
        )  # Initialize minimum importance as infinity
        earliest_memory: MemoryUnit = self.memories[0]  # Start with the first memory

        for memory in self.memories:
            if memory.importance < min_importance:
                min_importance = memory.importance  # Update minimum importance found
                earliest_memory = (
                    memory  # Reset to current memory if a new minimum is found
                )
            elif memory.importance == min_importance:
                # Compare timestamps if importance is the same
                if (
                    earliest_memory is None
                    or memory.timestamp < earliest_memory.timestamp
                ):
                    earliest_memory = memory  # Update to earlier timestamp if necessary

        self.memories.remove(
            earliest_memory
        )  # Remove the least important or oldest memory

    def decay_memory(self) -> None:
        current_time = datetime.now()  # Get current time

        memories_to_remove = []  # List to track memories that need removal

        for memory in self.memories:
            time_passed = (current_time - memory.timestamp).total_seconds() / 3600.0
            decay_rate = 1.0 / (
                memory.importance + 1e-5
            )  # Calculate decay rate based on importance

            # Decrease importance based on time passed and calculated decay rate
            memory.importance -= decay_rate * time_passed

            if memory.importance <= 0:
                memories_to_remove.append(
                    memory
                )  # Mark for removal if importance drops below zero

        for memory in memories_to_remove:
            self.memories.remove(memory)  # Remove decayed memories from the list
