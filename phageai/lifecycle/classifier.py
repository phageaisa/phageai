import os
import base64

import logging
import requests

logging.basicConfig(level=logging.INFO)


class LifeCycleClassifier:
    """
    Bacteriophage life cycle classifier

    All the research and scientific details were published in the paper:
    DOI: 10.1101/2020.07.11.198606
    """

    API_URL = "aHR0cHM6Ly9hcHAucGhhZ2UuYWkvYXBpL2xpZmVjeWNsZV9wcmVkaWN0aW9uLw=="
    EXPECTED_HTTP_STATUS = 201

    def __init__(self, access_token: str) -> None:
        """
        Setup for PhageAI account (accession token) and result structure
        """

        # Access token is associated with the PhageAI active user account
        # You can find it in the "My profile" subpage ("API access" section)
        self.access_token = access_token
        self.result = {}

    def predict(self, fasta_path: str) -> dict:
        """
        Return dict structure with predicted class (label), prediction accuracy, GC% and sequence length
        for passed bacteriophage FASTA file
        """

        if os.path.exists(fasta_path):
            with open(fasta_path, "rb") as fasta:
                try:
                    response = requests.post(
                        base64.b64decode(self.API_URL),
                        data={
                            "access_token": self.access_token,
                        },
                        files=[("file", fasta)],
                    )

                    self.result = response.json()

                    if response.status_code == self.EXPECTED_HTTP_STATUS:
                        logging.info(
                            f"[PhageAI] Life cycle classifier executed successfully"
                        )
                    else:
                        logging.warning(
                            f'[PhageAI] Exception was raised: "{self.result}"'
                        )
                except requests.exceptions.RequestException as e:
                    logging.warning(f'[PhageAI] Exception was raised: "{e}"')
        else:
            logging.warning(
                f'[PhageAI] Exception was raised: "{fasta_path}" doesn\'t exists'
            )

        return self.result
