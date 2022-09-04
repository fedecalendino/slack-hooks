from .text import PlainText


class Accessory:
    def __init__(self, type: str):
        self.type = type

    def serialize(self) -> dict:
        return {
            "type": self.type,
        }


class ButtonAccessory(Accessory):
    def __init__(self, text: PlainText, action_id: str, value: str, url: str = None):
        super().__init__("button")

        self.text = text
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


class ImageAccessory(Accessory):
    def __init__(self, image_url: str, alt_text: str = ""):
        super().__init__("image")

        self.image_url: str = image_url
        self.alt_text: str = alt_text

    def serialize(self) -> dict:
        return super().serialize() | {
            "image_url": self.image_url,
            "alt_text": self.alt_text,
        }
