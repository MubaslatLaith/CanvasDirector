from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.setup_request import SetupRequest
from ...models.setup_response import SetupResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SetupRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/setup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SetupResponse | None:
    if response.status_code == 200:
        response_200 = SetupResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | SetupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetupRequest,
) -> Response[HTTPValidationError | SetupResponse]:
    """Setup Admin

     Set up initial administrator account.

    This endpoint can only be called once, when no admin user exists. It creates
    the first admin user for the system.

    Args:
        request: Admin account details (email, display_name, password)

    Returns:
        SetupResponse containing the created admin user

    Raises:
        HTTPException: 400 if admin already exists or password is weak
        HTTPException: 403 if multiuser mode is disabled

    Args:
        body (SetupRequest): Request body for initial admin setup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SetupResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SetupRequest,
) -> HTTPValidationError | SetupResponse | None:
    """Setup Admin

     Set up initial administrator account.

    This endpoint can only be called once, when no admin user exists. It creates
    the first admin user for the system.

    Args:
        request: Admin account details (email, display_name, password)

    Returns:
        SetupResponse containing the created admin user

    Raises:
        HTTPException: 400 if admin already exists or password is weak
        HTTPException: 403 if multiuser mode is disabled

    Args:
        body (SetupRequest): Request body for initial admin setup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SetupResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetupRequest,
) -> Response[HTTPValidationError | SetupResponse]:
    """Setup Admin

     Set up initial administrator account.

    This endpoint can only be called once, when no admin user exists. It creates
    the first admin user for the system.

    Args:
        request: Admin account details (email, display_name, password)

    Returns:
        SetupResponse containing the created admin user

    Raises:
        HTTPException: 400 if admin already exists or password is weak
        HTTPException: 403 if multiuser mode is disabled

    Args:
        body (SetupRequest): Request body for initial admin setup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SetupResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SetupRequest,
) -> HTTPValidationError | SetupResponse | None:
    """Setup Admin

     Set up initial administrator account.

    This endpoint can only be called once, when no admin user exists. It creates
    the first admin user for the system.

    Args:
        request: Admin account details (email, display_name, password)

    Returns:
        SetupResponse containing the created admin user

    Raises:
        HTTPException: 400 if admin already exists or password is weak
        HTTPException: 403 if multiuser mode is disabled

    Args:
        body (SetupRequest): Request body for initial admin setup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SetupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
