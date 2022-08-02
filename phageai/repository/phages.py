import logging
from typing import List

import requests

from phageai.phageai_auth import PhageAIConnector


class BacteriophageRepository(PhageAIConnector):
    EXPECTED_HTTP_STATUS = 200
    PATH = "YmFjdGVyaW9waGFnZS8="

    def get_record(self, value: str) -> List[dict]:
        """
        Return dict with bacteriophage meta-data
        """

        result = []

        try:
            response = self._make_request(
                path=self._encode(f"{self._decode(self.PATH)}{value}/"), method="get"
            )

            result = response.json()

            if response.status_code == self.EXPECTED_HTTP_STATUS:
                logging.info(f"[PhageAI] Phage get record executed successfully")
            else:
                logging.warning(f'[PhageAI] Exception was raised: "{result}"')
        except requests.exceptions.RequestException as e:
            logging.warning(f'[PhageAI] Exception was raised: "{e}"')

        return result

    def get_top10_similar_phages(self, value: str) -> List[dict]:
        """
        Return list of dicts contained top-10 most similar bacteriophages
        """

        result = []

        try:
            response = self._make_request(
                path=self._encode(
                    f"{self._decode(self.PATH)}{value}{self._decode('L3RvcC0xMC8=')}"
                ),
                method="get",
            )

            result = response.json()

            if response.status_code == self.EXPECTED_HTTP_STATUS:
                logging.info(
                    f"[PhageAI] Phage top-10 similar phages executed successfully"
                )
            else:
                logging.warning(f'[PhageAI] Exception was raised: "{result}"')
        except requests.exceptions.RequestException as e:
            logging.warning(f'[PhageAI] Exception was raised: "{e}"')

        return result
