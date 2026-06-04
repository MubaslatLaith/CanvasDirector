from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_dto import UserDTO
from ...models.user_profile_update_request import UserProfileUpdateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: UserProfileUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/auth/me",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserDTO | None:
    if response.status_code == 200:
        response_200 = UserDTO.from_dict(response.json())

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
    body: UserProfileUpdateRequest,
) -> Response[HTTPValidationError | UserDTO]:
    """Update Current User

     Update the current user's own profile.

    To change the password, both ``current_password`` and ``new_password`` must
    be provided. The current password is verified before the change is applied.

    Args:
        request: Profile fields to update
        current_user: The authenticated user

    Returns:
        The updated user

    Raises:
        HTTPException: 400 if current password is incorrect or new password is weak
        HTTPException: 404 if user not found

    Args:
        body (UserProfileUpdateRequest): Request body for a user to update their own profile.

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
    body: UserProfileUpdateRequest,
) -> HTTPValidationError | UserDTO | None:
    """Update Current User

     Update the current user's own profile.

    To change the password, both ``current_password`` and ``new_password`` must
    be provided. The current password is verified before the change is applied.

    Args:
        request: Profile fields to update
        current_user: The authenticated user

    Returns:
        The updated user

    Raises:
        HTTPException: 400 if current password is incorrect or new password is weak
        HTTPException: 404 if user not found

    Args:
        body (UserProfileUpdateRequest): Request body for a user to update their own profile.

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
    body: UserProfileUpdateRequest,
) -> Response[HTTPValidationError | UserDTO]:
    """Update Current User

     Update the current user's own profile.

    To change the password, both ``current_password`` and ``new_password`` must
    be provided. The current password is verified before the change is applied.

    Args:
        request: Profile fields to update
        current_user: The authenticated user

    Returns:
        The updated user

    Raises:
        HTTPException: 400 if current password is incorrect or new password is weak
        HTTPException: 404 if user not found

    Args:
        body (UserProfileUpdateRequest): Request body for a user to update their own profile.

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
    body: UserProfileUpdateRequest,
) -> HTTPValidationError | UserDTO | None:
    """Update Current User

     Update the current user's own profile.

    To change the password, both ``current_password`` and ``new_password`` must
    be provided. The current password is verified before the change is applied.

    Args:
        request: Profile fields to update
        current_user: The authenticated user

    Returns:
        The updated user

    Raises:
        HTTPException: 400 if current password is incorrect or new password is weak
        HTTPException: 404 if user not found

    Args:
        body (UserProfileUpdateRequest): Request body for a user to update their own profile.

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
