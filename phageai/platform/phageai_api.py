import os

import requests
import logging
from http import HTTPStatus

from phageai.phageai_auth import PhageAIConnector


class PhageAIAccounts(PhageAIConnector):
    def upload(self, fasta_path: str, access: str = "private") -> dict:
        """
        Upload FASTA file as "public", "private" or "" (temporary) sample in the PhageAI repository
        - "public" means that all the users will be able to see and download the sample;
        - "private" means that only you (as user) will be able to see and download the sample;
        - "" (temporary) means that the sample will be not hosted in the platform longer than during the processing;

        Upload stage is starting the pipeline execution for phage characteristic

        Method returns Job ID value which represents phage processing ID in the platform
        """

        job_id = {}

        if os.path.exists(fasta_path):
            with open(fasta_path, "rb") as fasta:
                try:
                    response = self._make_request(
                        path="upload/",
                        method="post",
                        data={"access": access},
                        files=[("fasta", fasta)]
                    )

                    job_id = response.json()

                    # HTTP 201
                    if response.status_code == HTTPStatus.CREATED:
                        logging.info(
                            f"[PhageAI] Phage upload executed successfully"
                        )
                    else:
                        logging.warning(f'[PhageAI] Exception was raised: "{job_id}"')
                except requests.exceptions.RequestException as e:
                    logging.warning(f'[PhageAI] Exception was raised: "{e}"')
        else:
            logging.warning(
                f'[PhageAI] Exception was raised: "{fasta_path}" doesn\'t exists'
            )

        return job_id

    def processing_status(self, job_id: str):
        """
        Method returns processing status for Phage sample related with Job ID
        """

        processing_results = {}

        try:
            response = self._make_request(
                path=f"upload/{job_id}/status/",
                method="get"
            )

            processing_results = response.json()

            # HTTP 200
            if response.status_code == HTTPStatus.OK:
                logging.info(
                    f"[PhageAI] Phage processing status"
                )
            else:
                logging.warning(f'[PhageAI] Exception was raised: "{processing_results}"')
        except requests.exceptions.RequestException as e:
            logging.warning(f'[PhageAI] Exception was raised: "{e}"')

        return processing_results

    def _execute_phage_method(self, phageai_method: str, value: str, http_method: str):
        """
        Private method for generic phage method execution
        """

        results = {}

        try:
            response = self._make_request(
                path=f"phage/{value}/{phageai_method}/",
                method=http_method
            )

            results = response.json()

            # HTTP 200
            if response.status_code == HTTPStatus.OK:
                logging.info(
                    f"[PhageAI] Phage {phageai_method} method executed successfully"
                )
            else:
                logging.warning(f'[PhageAI] Exception was raised: "{results}"')
        except requests.exceptions.RequestException as e:
            logging.warning(f'[PhageAI] Exception was raised: "{e}"')

        return results

    def get_taxonomy_classification(self, job_id: str):
        """
        Method returns phage taxonomy classification results for order, family and genus
        """

        return self._execute_phage_method(
            phageai_method="taxonomy_classification",
            value=job_id,
            http_method="get",
        )

    def get_proteins_classification(self, job_id: str):
        """
        Method returns phage proteins structural classes classification results
        """

        return self._execute_phage_method(
            phageai_method="proteins_classification",
            value=job_id,
            http_method="get",
        )

    def get_top10_similarities(self, job_id: str):
        """
        Method returns TOP-10 similar phages in the PhageAI repository
        """

        return self._execute_phage_method(
            phageai_method="top10_similarities",
            value=job_id,
            http_method="get",
        )

    def get_lifecycle_classification(self, job_id: str):
        """
        Method returns lifecycle classification result
        """

        return self._execute_phage_method(
            phageai_method="lifecycle_classification",
            value=job_id,
            http_method="get",
        )

    def get_full_report(self, job_id: str):
        """
        Method returns full phage characteristics report
        """

        return self._execute_phage_method(
            phageai_method="report",
            value=job_id,
            http_method="get",
        )

    def get_phage_characteristic(self, accession_number: str):
        """
        Method returns meta-data about phage with specific accession number (with version)
        """

        return self._execute_phage_method(
            phageai_method="characteristic",
            value=accession_number,
            http_method="get",
        )
