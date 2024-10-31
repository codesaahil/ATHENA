from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class MemoryUnit:
    timestamp: datetime
    content: str
    importance: float
    tags: List[str]

    def __str__(self) -> str:
        tags_str = ", ".join(self.tags)
        return (
            f"MemoryUnit("
            f"timestamp={self.timestamp}, "
            f"content='{self.content}', "
            f"importance={self.importance}, "
            f"tags=[{tags_str}])"
        )


@dataclass
class Memory:
    memories: List[MemoryUnit]
    capacity: int
    decay_rate: float

    def __str__(self) -> str:
        return "\n".join(str(memory) for memory in self.memories)

    def add_memory(self, memory_unit: MemoryUnit) -> None:
        if len(self.memories) >= self.capacity:
            self.clean_memories()
        self.memories.append(memory_unit)

    def clean_memories(self) -> None:
        least_important_memory = min(
            self.memories, key=lambda mem: (mem.importance, mem.timestamp)
        )
        self.memories.remove(least_important_memory)

    def decay_memory(self) -> None:
        current_time = datetime.now()
        memories_to_remove = []

        for memory in self.memories:
            time_passed = (current_time - memory.timestamp).total_seconds() / 3600.0
            memory.importance -= self.decay_rate * time_passed

            if memory.importance <= 0:
                memories_to_remove.append(memory)

        for memory in memories_to_remove:
            self.memories.remove(memory)
