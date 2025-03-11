"""
Aloha API Client

A Python package for interacting with the Aloha ABA Practice Management Software API.
"""

__version__ = "0.1.0"

from .api import (  # isort: skip
    AlohaApiError,
    ApiRequestError,
    AuthenticationError,
    BASE_URL,
    CLIENT_ID,
    ConfigurationError,
    get_access_token,
    list_appointments,
    list_authorizations,
    list_authorizations_without_appointments,
    list_billing_ledger,
    list_clients,
    refresh_access_token,
)

__all__ = [
    "get_access_token",
    "refresh_access_token",
    "list_appointments",
    "list_clients",
    "list_authorizations",
    "list_billing_ledger",
    "list_authorizations_without_appointments",
    "BASE_URL",
    "CLIENT_ID",
    "AlohaApiError",
    "AuthenticationError",
    "ConfigurationError",
    "ApiRequestError",
]
