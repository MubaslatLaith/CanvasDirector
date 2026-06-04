from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_user_create_request import AdminUserCreateRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.user_dto import UserDTO
from ...types import Response


def _get_kwargs(
    *,
    body: AdminUserCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserDTO | None:
    if response.status_code == 201:
        response_201 = UserDTO.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | UserDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AdminUserCreateRequest,
) -> Response[HTTPValidationError | UserDTO]:
    """Create User

     Create a new user. Requires admin privileges.

    Args:
        request: New user details

    Returns:
        The created user

    Raises:
        HTTPException: 400 if email already exists or password is weak

    Args:
        body (AdminUserCreateRequest): Request body for admin to create a new user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserDTO]
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
    client: AuthenticatedClient,
    body: AdminUserCreateRequest,
) -> HTTPValidationError | UserDTO | None:
    """Create User

     Create a new user. Requires admin privileges.

    Args:
        request: New user details

    Returns:
        The created user

    Raises:
        HTTPException: 400 if email already exists or password is weak

    Args:
        body (AdminUserCreateRequest): Request body for admin to create a new user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AdminUserCreateRequest,
) -> Response[HTTPValidationError | UserDTO]:
    """Create User

     Create a new user. Requires admin privileges.

    Args:
        request: New user details

    Returns:
        The created user

    Raises:
        HTTPException: 400 if email already exists or password is weak

    Args:
        body (AdminUserCreateRequest): Request body for admin to create a new user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AdminUserCreateRequest,
) -> HTTPValidationError | UserDTO | None:
    """Create User

     Create a new user. Requires admin privileges.

    Args:
        request: New user details

    Returns:
        The created user

    Raises:
        HTTPException: 400 if email already exists or password is weak

    Args:
        body (AdminUserCreateRequest): Request body for admin to create a new user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
