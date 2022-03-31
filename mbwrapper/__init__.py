"""Malware Bazaar API Wrapper Library."""

import json

import requests


def get_info(sample_hash: str = None) -> dict:
    """Get information about a hash."""
    if sample_hash:
        response = requests.post(
            "https://mb-api.abuse.ch/api/v1/",
            data={
                "query": "get_info",
                "hash": sample_hash,
            },
        )
        return json.loads(response.content)
    return {}
