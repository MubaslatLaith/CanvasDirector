from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.logout_response import LogoutResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/logout",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LogoutResponse | None:
    if response.status_code == 200:
        response_200 = LogoutResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[LogoutResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[LogoutResponse]:
    """Logout

     Logout current user.

    Currently a no-op since we use stateless JWT tokens. For token invalidation in
    future implementations, consider:
    - Token blacklist: Store invalidated tokens in Redis/database with expiration
    - Token versioning: Add version field to user record, increment on logout
    - Short-lived tokens: Use refresh token pattern with token rotation
    - Session storage: Track active sessions server-side for revocation

    Args:
        current_user: The authenticated user (validates token)

    Returns:
        LogoutResponse indicating success

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogoutResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> LogoutResponse | None:
    """Logout

     Logout current user.

    Currently a no-op since we use stateless JWT tokens. For token invalidation in
    future implementations, consider:
    - Token blacklist: Store invalidated tokens in Redis/database with expiration
    - Token versioning: Add version field to user record, increment on logout
    - Short-lived tokens: Use refresh token pattern with token rotation
    - Session storage: Track active sessions server-side for revocation

    Args:
        current_user: The authenticated user (validates token)

    Returns:
        LogoutResponse indicating success

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogoutResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[LogoutResponse]:
    """Logout

     Logout current user.

    Currently a no-op since we use stateless JWT tokens. For token invalidation in
    future implementations, consider:
    - Token blacklist: Store invalidated tokens in Redis/database with expiration
    - Token versioning: Add version field to user record, increment on logout
    - Short-lived tokens: Use refresh token pattern with token rotation
    - Session storage: Track active sessions server-side for revocation

    Args:
        current_user: The authenticated user (validates token)

    Returns:
        LogoutResponse indicating success

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogoutResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> LogoutResponse | None:
    """Logout

     Logout current user.

    Currently a no-op since we use stateless JWT tokens. For token invalidation in
    future implementations, consider:
    - Token blacklist: Store invalidated tokens in Redis/database with expiration
    - Token versioning: Add version field to user record, increment on logout
    - Short-lived tokens: Use refresh token pattern with token rotation
    - Session storage: Track active sessions server-side for revocation

    Args:
        current_user: The authenticated user (validates token)

    Returns:
        LogoutResponse indicating success

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogoutResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
