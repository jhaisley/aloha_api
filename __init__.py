"""
Aloha API Client

A Python package for interacting with the Aloha ABA Practice Management Software API.
"""

__version__ = "0.1.0"

from .api import (
    get_access_token,
    refresh_access_token,
    list_appointments,
    list_clients,
    list_authorizations,
    list_billing_ledger,
    list_authorizations_without_appointments,
    BASE_URL,
    CLIENT_ID,
    # Export exception classes
    AlohaApiError,
    AuthenticationError,
    ConfigurationError,
    ApiRequestError,
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
    # Exception classes
    "AlohaApiError",
    "AuthenticationError",
    "ConfigurationError",
    "ApiRequestError",
]
