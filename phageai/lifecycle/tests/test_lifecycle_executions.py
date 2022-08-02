import json
import uuid
from unittest import mock

import pytest

from phageai.lifecycle.classifier import LifeCycleClassifier


def test_invalid_access_token_and_fasta_file():
    """
    Test API reaction on invalid access token and FASTA file
    """

    lcc = LifeCycleClassifier(access_token="INVALID_TOKEN")

    result = lcc.predict(fasta_path="INVALID_FASTA_FILE")

    assert result == {}


def test_old_access_token():
    """
    Test API reaction on invalid access token and FASTA file
    """

    with pytest.raises(ValueError) as exc_info:
        LifeCycleClassifier(access_token=str(uuid.uuid4()))
    assert "[PhageAI] Token Error: We have change our TOS and Policy." in str(
        exc_info.value
    )


def test_empty_access_token():
    """
    Test API reaction on empty access token
    """

    with pytest.raises(ValueError) as exc_info:
        LifeCycleClassifier(access_token="")
    assert "[PhageAI] Token Error: Please provide correct access token." in str(
        exc_info.value
    )


def test_null_access_token():
    """
    Test API reaction on null access token
    """

    with pytest.raises(ValueError) as exc_info:
        LifeCycleClassifier(access_token=None)
    assert "[PhageAI] Token Error: Please provide correct access token." in str(
        exc_info.value
    )


def test_correct_fasta_file():
    """
    Test API reaction on valid FASTA file
    """

    response_example = {
        "hash": "4b0b12e3e4af0d79ba172240fa20bf2f912e2297e3ab1c3b7207200877e7ceab",
        "predicted_lifecycle": "Virulent",
        "gc": "41.45",
        "prediction_accuracy": "100.00",
        "sequence_length": 171599,
    }

    with mock.patch(
        "phageai.lifecycle.classifier.LifeCycleClassifier._make_request"
    ) as mock_connector:
        mock_connector.return_value.json.return_value = response_example

        lcc = LifeCycleClassifier(access_token="GOOD_TOKEN")
        result = lcc.predict(fasta_path="phageai/lifecycle/tests/NC_055712.fasta")

        assert result == response_example


def test_incorrect_fasta_file():
    """
    Test API reaction on invalid FASTA file
    """

    response_example = {}

    with mock.patch(
        "phageai.lifecycle.classifier.LifeCycleClassifier._make_request"
    ) as mock_connector:
        mock_connector.return_value.json.return_value = response_example

        lcc = LifeCycleClassifier(access_token="GOOD_TOKEN")
        result = lcc.predict(fasta_path="BAD_FILE.fasta")

        assert result == response_example
