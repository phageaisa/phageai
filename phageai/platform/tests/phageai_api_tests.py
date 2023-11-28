import uuid
from unittest import mock

import pytest

from phageai.platform import PhageAIAccounts


def test_invalid_access_token_and_fasta_file():
    """
    Test API reaction on invalid access token and FASTA file
    """

    phageai_api = PhageAIAccounts(access_token="INVALID_TOKEN")

    result = phageai_api.upload(fasta_path="INVALID_FASTA_FILE")

    assert result == {}


def test_old_access_token():
    """
    Test API reaction on invalid access token and FASTA file
    """

    with pytest.raises(ValueError) as exc_info:
        PhageAIAccounts(access_token=str(uuid.uuid4()))
    assert "[PhageAI] Token Error: We have change our TOS and Policy." in str(
        exc_info.value
    )


def test_empty_access_token():
    """
    Test API reaction on empty access token
    """

    with pytest.raises(ValueError) as exc_info:
        PhageAIAccounts(access_token="")
    assert "[PhageAI] Token Error: Please provide correct access token." in str(
        exc_info.value
    )


def test_null_access_token():
    """
    Test API reaction on null access token
    """

    with pytest.raises(ValueError) as exc_info:
        PhageAIAccounts(access_token=None)
    assert "[PhageAI] Token Error: Please provide correct access token." in str(
        exc_info.value
    )


def test_correct_fasta_file():
    """
    Test API reaction on valid FASTA file
    """

    response_example = {
        "lifecycle": {"value": "Virulent", 'probability': 100.0},
        "gc": "41.45",
        "length": 171598
    }

    with mock.patch(
        "phageai.platform.PhageAIAccounts._make_request"
    ) as mock_connector:
        mock_connector.return_value.json.return_value = response_example

        phageai_api = PhageAIAccounts(access_token="GOOD_TOKEN")
        result = phageai_api.upload(fasta_path="phageai/platform/tests/NC_055712.fasta")

        assert result == response_example


def test_incorrect_fasta_file():
    """
    Test API reaction on invalid FASTA file
    """

    response_example = {}

    with mock.patch(
        "phageai.platform.PhageAIAccounts._make_request"
    ) as mock_connector:
        mock_connector.return_value.json.return_value = response_example

        phageai_api = PhageAIAccounts(access_token="GOOD_TOKEN")
        result = phageai_api.upload(fasta_path="BAD_FILE.fasta")

        assert result == response_example
