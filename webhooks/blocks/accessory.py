from .text import PlainText


class Accessory:
    def __init__(self, type: str):
        self.type = type

    def serialize(self) -> dict:
        return {
            "type": self.type,
        }


class Button(Accessory):
    def __init__(self, text: PlainText, action_id: str, value: str, url: str = None):
        super().__init__("button")

        self.text: PlainText = text
        self.value: str = value
        self.action_id: str = action_id
        self.url: str = url

    def serialize(self) -> dict:
        serialization = super().serialize()

        serialization |= {
            "text": self.text.serialize(),
            "url": self.url,
            "action_id": self.action_id,
            "value": self.value,
        }

        return serialization
