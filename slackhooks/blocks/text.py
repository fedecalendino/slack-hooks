PLAIN_TEXT = "plain_text"
MARKDOWN = "mrkdwn"


class Text:
    def __init__(self, text: str = None, type: str = None):
        self.text = text
        self.type = type

    def serialize(self) -> dict:
        return {
            "text": self.text,
            "type": self.type,
        }


class PlainText(Text):
    def __init__(self, text: str = None, emoji: bool = True):
        super().__init__(text=text, type=PLAIN_TEXT)
        self.emoji = emoji

    def serialize(self) -> dict:
        serialized = super().serialize()
        serialized.update(
            {
                "emoji": self.emoji,
            }
        )

        return serialized


class MarkdownText(Text):
    def __init__(self, text: str = None):
        super().__init__(text=text, type=MARKDOWN)
