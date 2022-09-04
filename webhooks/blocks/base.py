class Block:
    def __init__(self, type: str):
        self.type = type

    def serialize(self) -> dict:
        return {
            "type": self.type,
        }
