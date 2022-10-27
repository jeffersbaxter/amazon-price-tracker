import os
import requests

ACCEPT_LANG = os.environ.get("ACCEPT_LANG")
USER_AGENT = os.environ.get("USER_AGENT")
AMAZON_URL = os.environ.get("AMAZON_URL")

headers = {
    "Accept-Language": ACCEPT_LANG,
    "User-Agent": USER_AGENT
}


def make_request():
    response = requests.get(
        url=AMAZON_URL,
        headers=headers
    )

    response.raise_for_status()

    return response
