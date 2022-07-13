import base64

import logging
import requests

from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)


class PhageAIConnector:
    """
    Generic PhageAI API connector
    """

    REQUEST_TIMEOUT = 30

    BASE_URL = "aHR0cHM6Ly9iYWNrZW5kLWRldi5waGFnZWFpLmNsb3VkL2FwaS8="
    # BASE_URL = "aHR0cDovLzE5Mi4xNjguMS4xMDc6ODAwMC9hcGkv"

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token
        self.result = {}

    def _make_request(self, path: str, method: str, **kwargs) -> requests.Response:
        """
        Generic PhageAI API request method
        """

        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }

        base_url = base64.b64decode(f"{self.BASE_URL}").decode("utf-8")
        url = urljoin(base_url, path)

        logging.info(
            f"[PhageAI] Method: {method}"
        )

        response = getattr(requests, method)(
            url=url,
            headers=headers,
            timeout=self.REQUEST_TIMEOUT,
            **kwargs,
        )
        response.raise_for_status()

        return response
