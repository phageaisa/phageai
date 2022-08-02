import base64
import logging
import uuid
from urllib.parse import urljoin

import requests

logging.basicConfig(level=logging.INFO)


class PhageAIConnector:
    """
    Generic PhageAI API connector
    """

    REQUEST_TIMEOUT = 30

    BASE_URL = "aHR0cHM6Ly9jb3JlLnBoYWdlLmFpL2FwaS92MS9waGFnZWFpLXBhY2thZ2Uv"

    def __init__(self, access_token: str) -> None:
        if not access_token:
            raise ValueError(
                "[PhageAI] Token Error: Please provide correct access token. If you need more information, please check README."
            )
        if self._is_uuid(access_token):
            raise ValueError(
                "[PhageAI] Token Error: We have change our TOS and Policy. Please login to PhageAI Web platform (https://app.phage.ai/) and create new access token."
            )
        self.access_token = access_token
        self.result = {}

    @staticmethod
    def _is_uuid(value):
        try:
            uuid.UUID(value)
            return True
        except ValueError:
            return False

    def _create_auth_header(self) -> dict:
        return {
            "Authorization": f"Bearer {self.access_token}",
        }

    @staticmethod
    def _encode(value: str) -> str:
        return base64.b64encode(value.encode()).decode("utf-8")

    @staticmethod
    def _decode(value: str) -> str:
        return base64.b64decode(value).decode("utf-8")

    def _create_url(self, path) -> str:
        return urljoin(self._decode(self.BASE_URL), self._decode(path))

    @staticmethod
    def _check_status(response):
        http_error_msg = ""
        if isinstance(response.reason, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = response.reason.decode("utf-8")
            except UnicodeDecodeError:
                reason = response.reason.decode("iso-8859-1")
        else:
            reason = response.reason

        if 400 <= response.status_code < 500:
            http_error_msg = f"[PhageAI] Connection Client Error: Response Status Code - {response.status_code} Reason: {reason}"
        elif 500 <= response.status_code < 600:
            http_error_msg = f"[PhageAI] Connection Server Error: Response Status Code - {response.status_code} Reason: {reason}"

        if http_error_msg:
            raise requests.HTTPError(http_error_msg, response=response)

    def _make_request(self, path: str, method: str, **kwargs) -> requests.Response:
        """
        Generic PhageAI API request method
        """

        headers = self._create_auth_header()

        logging.info(f"[PhageAI] Method: {method}")

        response = getattr(requests, method)(
            url=self._create_url(path),
            headers=headers,
            timeout=self.REQUEST_TIMEOUT,
            **kwargs,
        )

        self._check_status(response)

        return response
