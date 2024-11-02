from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class MemoryUnit:
    """
    A class to represent a unit of memory for an NPC.

    Attributes:
        timestamp (datetime): The time when the memory was created.
        content (str): The content of the memory.
        importance (float): The importance of the memory, between 0.0 and 1.0.
    """
    timestamp: datetime
    content: str
    importance: float

    def __str__(self) -> str:
        """
        Returns a string representation of the MemoryUnit object.

        Returns:
            str: A formatted string showing the memory details.
        """
        return (
            f"MemoryUnit("
            f"timestamp={self.timestamp}, "
            f"content='{self.content}', "
            f"importance={self.importance}, "
        )


@dataclass
class Memory:
    """
    A class to represent a collection of memories for an NPC.

    Attributes:
        memories (List[MemoryUnit]): A list of MemoryUnit objects.
        capacity (int): The maximum number of memories that can be stored.
        decay_rate (float): The rate at which memory importance decays over time.
    """
    memories: List[MemoryUnit]
    capacity: int
    decay_rate: float

    def __str__(self) -> str:
        """
        Returns a string representation of all memories in the Memory object.

        Returns:
            str: A formatted string showing all memories.
        """
        return "\n".join(str(memory) for memory in self.memories)

    def add_memory(self, memory_unit: MemoryUnit) -> None:
        """
        Adds a new memory unit to the memory collection.

        If the memory collection exceeds its capacity, the least important memory is removed.

        Args:
            memory_unit (MemoryUnit): The memory unit to add.
        """
        if len(self.memories) >= self.capacity:
            self.clean_memories()  # Clean up memories if at capacity
        self.memories.append(memory_unit)  # Append the new memory unit

    def clean_memories(self) -> None:
        """
        Cleans up the memory collection by removing the least important memory unit.
        """
        least_important_memory = min(
            self.memories, key=lambda mem: (mem.importance, mem.timestamp)
        )
        self.memories.remove(
            least_important_memory
        )  # Remove the least important memory

    def decay_memory(self) -> None:
        """
        Decays the importance of each memory unit based on the elapsed time since it was created.

        If a memory's importance drops to zero or below, it is removed from the collection.
        """
        current_time = datetime.now()
        memories_to_remove = []

        for memory in self.memories:
            # Calculate time passed in hours since the memory was created
            time_passed = (current_time - memory.timestamp).total_seconds() / 3600.0
            memory.importance -= self.decay_rate * time_passed  # Apply decay

            if memory.importance <= 0:
                memories_to_remove.append(
                    memory
                )  # Mark memory for removal if importance is zero or less

        for memory in memories_to_remove:
            self.memories.remove(memory)  # Remove decayed memories from the collection
