from dataclasses import dataclass, field
from typing import Literal
import uuid


@dataclass
class Book:
    title: str
    status: Literal["to-read", "in-progress", "completed"] = "to-read"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
