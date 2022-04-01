"""Malware Bazaar API Wrapper Library Unit Tests."""

import json
from unittest import mock

import requests

import mbwrapper as mb


@mock.patch("mbwrapper.requests.post", create=True)
def test_get_info(mock_post) -> None:
    """Test the mb.get_info function."""
    test_hash = "0123456789ABCDEF0123456789ABCDEF"
    expected_response = {
        "query_status": "ok",
        "data": [{"md5_hash": test_hash, "signature": "RevengeRAT"}],
    }
    response = requests.Response()
    response._content = json.dumps(expected_response).encode("utf-8")
    response.status_code = 200
    mock_post.return_value = response
    actual_response = mb.get_info(sample_hash=test_hash)
    mock_post.assert_called_with(
        "https://mb-api.abuse.ch/api/v1/",
        data={
            "query": "get_info",
            "hash": test_hash,
        },
    )
    assert actual_response == expected_response


@mock.patch("mbwrapper.requests.post", create=True)
def test_get_file(mock_post) -> None:
    """Test the mb.get_file function."""
    test_hash = (
        "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
    )
    response = requests.Response()
    response.status_code = 200
    expected_response = b"PK\x03\x043\x00\x03\x00c\x00\x17\x7f\x81T\x1e\x1e"
    response._content = expected_response
    mock_post.return_value = response
    actual_response = mb.get_file(sample_hash=test_hash)
    mock_post.assert_called_with(
        "https://mb-api.abuse.ch/api/v1/",
        data={
            "query": "get_file",
            "sha256_hash": test_hash,
        },
    )
    assert actual_response == expected_response
