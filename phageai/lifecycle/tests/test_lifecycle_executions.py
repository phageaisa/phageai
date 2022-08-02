import uuid

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
