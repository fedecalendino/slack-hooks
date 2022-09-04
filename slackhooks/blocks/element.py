PLAIN_TEXT = "plain_text"
MARKDOWN = "mrkdwn"


class Element:
    def __init__(self, type: str):
        self.type = type

    def serialize(self) -> dict:
        return {
            "type": self.type,
        }


class TextElement(Element):
    def __init__(self, type: str, text: str):
        super().__init__(type)
        self.text = text

    def serialize(self) -> dict:
        return super().serialize() | {
            "text": self.text,
        }


class PlainTextElement(TextElement):
    def __init__(self, text: str = None, emoji: bool = True):
        super().__init__(
            type=PLAIN_TEXT,
            text=text,
        )
        self.emoji = emoji

    def serialize(self) -> dict:
        return super().serialize() | {
            "emoji": self.emoji,
        }


class MarkdownTextElement(TextElement):
    def __init__(self, text: str):
        super().__init__(
            type=MARKDOWN,
            text=text,
        )


class ImageElement(Element):
    def __init__(self, image_url: str, alt_text: str = ""):
        super().__init__(type="image")

        self.image_url: str = image_url
        self.alt_text: str = alt_text

    def serialize(self) -> dict:
        return super().serialize() | {
            "image_url": self.image_url,
            "alt_text": self.alt_text,
        }
