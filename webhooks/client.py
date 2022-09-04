from typing import List

import requests

from webhooks.blocks.block import Block


class Message:
    def __init__(self, text: str = None, blocks: List[Block] = None):
        self.text: str = text
        self.blocks: List[Block] = blocks or []

    def serialize(self):
        return {
            "text": self.text,
            "blocks": list(
                map(
                    lambda block: block.serialize(),
                    self.blocks,
                )
            ),
        }

    def send(self, webhook_url: str):
        return requests.post(
            url=webhook_url,
            json=self.serialize(),
        )
