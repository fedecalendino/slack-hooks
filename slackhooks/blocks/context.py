from typing import List

from .block import Block
from .element import Element


class Context(Block):
    def __init__(self, elements: List[Element] = None):
        super().__init__(type="context")

        self.elements: List[Element] = elements or []

    def serialize(self) -> dict:
        return super().serialize() | {
            "elements": list(
                map(
                    lambda element: element.serialize(),
                    self.elements,
                )
            )
        }
