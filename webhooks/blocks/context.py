from typing import List

from .block import Block
from .text import Text


class Context(Block):
    def __init__(self, elements: List[Text] = None):
        super().__init__(type="context")

        self.elements: List[Text] = elements or []

    def serialize(self) -> dict:
        return super().serialize() | {
            "elements": list(
                map(
                    lambda element: element.serialize(),
                    self.elements,
                )
            )
        }
