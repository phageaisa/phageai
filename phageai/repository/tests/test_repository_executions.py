import uuid
from unittest import mock

import pytest

from phageai.repository.phages import BacteriophageRepository


def test_invalid_access_token_and_fasta_file_1():
    """
    Test API reaction on invalid access token and FASTA file
    """

    lcc = BacteriophageRepository(access_token="INVALID_TOKEN")

    result = lcc.get_record(value="NC_000866")

    assert result == []


def test_invalid_access_token_and_fasta_file_2():
    """
    Test API reaction on invalid access token and FASTA file
    """

    lcc = BacteriophageRepository(access_token="INVALID_TOKEN")

    result = lcc.get_top10_similar_phages(value="NC_000866")

    assert result == []


def test_old_access_token():
    """
    Test API reaction on invalid access token and FASTA file
    """

    with pytest.raises(ValueError) as exc_info:
        BacteriophageRepository(access_token=str(uuid.uuid4()))
    assert "[PhageAI] Token Error: We have change our TOS and Policy." in str(
        exc_info.value
    )


def test_empty_access_token():
    """
    Test API reaction on empty access token
    """

    with pytest.raises(ValueError) as exc_info:
        BacteriophageRepository(access_token="")
    assert "[PhageAI] Token Error: Please provide correct access token." in str(
        exc_info.value
    )


def test_null_access_token():
    """
    Test API reaction on null access token
    """

    with pytest.raises(ValueError) as exc_info:
        BacteriophageRepository(access_token=None)
    assert "[PhageAI] Token Error: Please provide correct access token." in str(
        exc_info.value
    )


def test_correct_accession_number():
    """
    Test API reaction on valid accession number
    """

    response_example = [
        {
            "hash": "edab9a1ed79c0436490cb569449b8ecbd03e591f45510c169df5076226e81b66",
            "accession_no": "MZ375324",
            "name": "Salmonella phage seszw",
            "description": "Mutant salmonella phage seszw clone seszw_150s, complete genome",
            "host": "Salmonella",
            "host_full": "Salmonella",
            "origin_lifecycle": "Unknown",
            "origin_order": "",
            "origin_family": "",
            "origin_genus": "",
            "predicted_lifecycle": {"name": "Temperate", "accuracy": "93.50"},
            "predicted_order": {"name": "Caudovirales", "accuracy": "99.85"},
            "predicted_family": {"name": "Siphoviridae", "accuracy": "98.59"},
            "predicted_genus": {"name": "Roufvirus", "accuracy": "99.20"},
            "sequence_length": 40462,
            "gc": "46.16",
            "genome_coverage_label": "Complete genome",
            "genome_composition_label": "Unknown",
            "is_refseq": "No",
        }
    ]

    with mock.patch(
        "phageai.repository.phages.BacteriophageRepository._make_request"
    ) as mock_connector:
        mock_connector.return_value.json.return_value = response_example

        lcc = BacteriophageRepository(access_token="GOOD_TOKEN")
        result = lcc.get_record(value="MZ375324")

        assert result == response_example


def test_incorrect_accession_number():
    """
    Test API reaction on invalid accession number
    """

    response_example = []

    with mock.patch(
        "phageai.repository.phages.BacteriophageRepository._make_request"
    ) as mock_connector:
        mock_connector.return_value.json.return_value = response_example

        lcc = BacteriophageRepository(access_token="GOOD_TOKEN")
        result = lcc.get_record(value="BAD_ACCNO")

        assert result == response_example
