import logging
import uuid

import requests

from urllib.parse import urljoin

from . import PHAGEAI_BASE_URL

logging.basicConfig(level=logging.INFO)


class PhageAIConnector:
    """
    Generic PhageAI API connector
    """

    REQUEST_TIMEOUT = 30

    API_URL = urljoin(PHAGEAI_BASE_URL, "/api/v1/phageai-package/")

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
            "Authorization": f"Bearer {self.access_token}"
        }

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

        response = getattr(requests, method)(
            url=urljoin(self.API_URL, path),
            headers=headers,
            timeout=self.REQUEST_TIMEOUT,
            **kwargs
        )

        self._check_status(response)

        return response
