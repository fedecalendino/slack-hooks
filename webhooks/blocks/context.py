from .block import Block
from .text import Text


class Context(Block):
    def __init__(self, elements: list[Text] = None):
        super().__init__(type="context")

        self.elements: list[Text] = elements or []

    def serialize(self) -> dict:
        return super().serialize() | {
            "elements": list(
                map(
                    lambda element: element.serialize(),
                    self.elements,
                )
            )
        }
