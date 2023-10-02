from dataclasses import dataclass, field
import uuid


@dataclass
class Book:
    title: str
    status: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
