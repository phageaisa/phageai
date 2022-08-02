import os

import requests
import logging

from phageai.phageai_auth import PhageAIConnector


class LifeCycleClassifier(PhageAIConnector):
    """
    Bacteriophage life cycle classifier

    All the research and scientific details were published in the paper:
    DOI: 10.1101/2020.07.11.198606
    """

    PATH = "bGlmZWN5Y2xlX3ByZWRpY3Rpb24v"
    EXPECTED_HTTP_STATUS = 201

    def predict(self, fasta_path: str) -> dict:
        """
        Return dict structure with predicted class (label), prediction accuracy, GC% and sequence length
        for passed bacteriophage FASTA file
        """

        result = {}

        if os.path.exists(fasta_path):
            with open(fasta_path, "rb") as fasta:
                try:
                    response = self._make_request(
                        path=self.PATH,
                        method="post",
                        files=[("file", fasta)],
                    )

                    result = response.json()

                    if response.status_code == self.EXPECTED_HTTP_STATUS:
                        logging.info(
                            f"[PhageAI] Life cycle classifier executed successfully"
                        )
                    else:
                        logging.warning(f'[PhageAI] Exception was raised: "{result}"')
                except requests.exceptions.RequestException as e:
                    logging.warning(f'[PhageAI] Exception was raised: "{e}"')
        else:
            logging.warning(
                f'[PhageAI] Exception was raised: "{fasta_path}" doesn\'t exists'
            )

        return result
