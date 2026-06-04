from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_dto import UserDTO
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/me",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UserDTO | None:
    if response.status_code == 200:
        response_200 = UserDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UserDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[UserDTO]:
    """Get Current User Info

     Get current authenticated user's information.

    Args:
        current_user: The authenticated user's token data

    Returns:
        UserDTO containing user information

    Raises:
        HTTPException: 404 if user is not found (should not happen normally)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserDTO]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> UserDTO | None:
    """Get Current User Info

     Get current authenticated user's information.

    Args:
        current_user: The authenticated user's token data

    Returns:
        UserDTO containing user information

    Raises:
        HTTPException: 404 if user is not found (should not happen normally)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserDTO
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[UserDTO]:
    """Get Current User Info

     Get current authenticated user's information.

    Args:
        current_user: The authenticated user's token data

    Returns:
        UserDTO containing user information

    Raises:
        HTTPException: 404 if user is not found (should not happen normally)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserDTO]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> UserDTO | None:
    """Get Current User Info

     Get current authenticated user's information.

    Args:
        current_user: The authenticated user's token data

    Returns:
        UserDTO containing user information

    Raises:
        HTTPException: 404 if user is not found (should not happen normally)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserDTO
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
