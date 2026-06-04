from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    queue_id: str,
    *,
    body: str,
    key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/client_state/{queue_id}/set_by_key".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[HTTPValidationError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: str,
    key: str,
) -> Response[HTTPValidationError | str]:
    """Set Client State

     Sets the client state for the current user (or system user if not authenticated)

    Args:
        queue_id (str): The queue id (ignored, kept for backwards compatibility)
        key (str): Key to set
        body (str): Stringified value to set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: str,
    key: str,
) -> HTTPValidationError | str | None:
    """Set Client State

     Sets the client state for the current user (or system user if not authenticated)

    Args:
        queue_id (str): The queue id (ignored, kept for backwards compatibility)
        key (str): Key to set
        body (str): Stringified value to set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        body=body,
        key=key,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: str,
    key: str,
) -> Response[HTTPValidationError | str]:
    """Set Client State

     Sets the client state for the current user (or system user if not authenticated)

    Args:
        queue_id (str): The queue id (ignored, kept for backwards compatibility)
        key (str): Key to set
        body (str): Stringified value to set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: str,
    key: str,
) -> HTTPValidationError | str | None:
    """Set Client State

     Sets the client state for the current user (or system user if not authenticated)

    Args:
        queue_id (str): The queue id (ignored, kept for backwards compatibility)
        key (str): Key to set
        body (str): Stringified value to set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            body=body,
            key=key,
        )
    ).parsed
