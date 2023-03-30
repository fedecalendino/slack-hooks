 # slack-hooks

[![Version](https://img.shields.io/pypi/v/slack-hooks?logo=pypi)](https://pypi.org/project/slack-hooks)
[![Quality Gate Status](https://img.shields.io/sonar/alert_status/fedecalendino_slack-hooks?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_slack-hooks)
[![CodeCoverage](https://img.shields.io/sonar/coverage/fedecalendino_slack-hooks?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_slack-hooks)

## Example usage

```python
import importlib.metadata
import logging
import os
import sys

import requests
from slackhooks.client import Message
from slackhooks.blocks.context import Context
from slackhooks.blocks.divider import Divider
from slackhooks.blocks.element import MarkdownTextElement
from slackhooks.blocks.section import Section
from slackhooks.blocks.text import MarkdownText


logging.basicConfig(level=logging.INFO)


def simple_markdown_section(mkd_text: str) -> Section:
    mkd_block = MarkdownText(mkd_text)
    message_section = Section(text=mkd_block)
    return message_section


def context_footer() -> Context:
    mk_text = MarkdownTextElement("_Sent by slackhooks example v%s_" % importlib.metadata.version(__package__))
    context = Context([mk_text])
    return context


def assemble_mkd_message(mkd_text: str) -> Message:
    blocks = [simple_markdown_section(mkd_text), Divider(), context_footer()]
    return Message(blocks=blocks)


def send_mkd_message(mkd_text: str, webhook_url: str) -> requests.Response:
    return assemble_mkd_message(mkd_text).send(webhook_url)


if __name__ == "__main__":
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", sys.argv[1] if len(sys.argv) > 1 else None)
    resp = send_mkd_message("It _looks_ like it's working!", webhook_url)
    if resp.status_code == 200:
        logging.info("Success!")
    else:
        logging.warning(f"It failed: {resp}")

```
