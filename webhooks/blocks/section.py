from .base import Block
from .text import Text, PlainText, MarkdownText
from .accessory import Accessory


class Section(Block):
    def __init__(
        self,
        accessory: Accessory = None,
        fields: list[Text] = None,
        text: Text = None,
    ):
        super().__init__(type="section")

        self._accessory = accessory
        self._fields: list[Text] = fields or []
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
