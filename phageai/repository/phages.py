import os
import base64

import logging
import requests

logging.basicConfig(level=logging.INFO)


class BacteriophageRepository:
    EXPECTED_HTTP_STATUS = 200

    def __init__(self, access_token: str) -> None:
        """
        Setup for PhageAI account (accession token) and value as identifier
        (RefSeq/GenBank accession number or unique hash)
        """

        # Access token is associated with the PhageAI active user account
        # You can find it in the "My profile" subpage ("API access" section)
        self.access_token = access_token
        self.result = {}

    def _make_request(self, api_url: str, value: str, postfix: str = "/") -> dict:
        """
        Generic request method (HTTP GET)
        """

        try:
            response = requests.get(
                f'{api_url}{value}{postfix}',
                data={
                    "access_token": self.access_token,
                },
            )

            self.result = response.json()

            if response.status_code == self.EXPECTED_HTTP_STATUS:
                logging.info(
                    f"[PhageAI] Repository executed successfully"
                )
            else:
                logging.warning(
                    f'[PhageAI] Exception was raised: "{self.result}"'
                )
        except requests.exceptions.RequestException as e:
            logging.warning(f'[PhageAI] Exception was raised: "{e}"')

        return self.result

    def get_record(self, value: str) -> dict:
        """
        Return dict with bacteriophage meta-data
        """

        api_url = base64.b64decode("aHR0cHM6Ly9hcHAucGhhZ2UuYWkvYXBpL2JhY3RlcmlvcGhhZ2Uv").decode('utf-8')

        return self._make_request(
            api_url=api_url,
            value=value
        )

    def get_top10_similar_phages(self, value: str) -> dict:
        """
        Return list of dicts contained top-10 most similar bacteriophages
        """

        api_url = base64.b64decode("aHR0cHM6Ly9hcHAucGhhZ2UuYWkvYXBpL2JhY3RlcmlvcGhhZ2Uv").decode('utf-8')
        postfix = base64.b64decode("L3RvcF8xMC8=").decode('utf-8')

        return self._make_request(
            api_url=api_url,
            value=value,
            postfix=postfix
        )
