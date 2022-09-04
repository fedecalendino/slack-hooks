from typing import List

from .accessory import Accessory
from .block import Block
from .text import Text


class Section(Block):
    def __init__(
        self,
        accessory: Accessory = None,
        fields: List[Text] = None,
        text: Text = None,
    ):
        super().__init__(type="section")

        self._accessory = accessory
        self._fields: List[Text] = fields or []
        self._text = text

    def serialize(self) -> dict:
        serialization = super().serialize()

        if self._accessory:
            serialization |= {
                "accessory": self._accessory.serialize(),
            }

        if self._fields:
            serialization |= {
                "fields": list(
                    map(
                        lambda field: field.serialize(),
                        self._fields,
                    )
                )
            }

        if self._text:
            serialization |= {
                "text": self._text.serialize(),
            }

        return serialization
