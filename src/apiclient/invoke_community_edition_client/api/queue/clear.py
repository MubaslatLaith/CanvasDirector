from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_result import ClearResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    queue_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/queue/{queue_id}/clear".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClearResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ClearResult.from_dict(response.json())

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
) -> Response[ClearResult | HTTPValidationError]:
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
) -> Response[ClearResult | HTTPValidationError]:
    """Clear

     Clears the queue entirely. Admin users clear all items; non-admin users only clear their own items.
    If there's a currently-executing item, users can only cancel it if they own it or are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> ClearResult | HTTPValidationError | None:
    """Clear

     Clears the queue entirely. Admin users clear all items; non-admin users only clear their own items.
    If there's a currently-executing item, users can only cancel it if they own it or are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearResult | HTTPValidationError
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ClearResult | HTTPValidationError]:
    """Clear

     Clears the queue entirely. Admin users clear all items; non-admin users only clear their own items.
    If there's a currently-executing item, users can only cancel it if they own it or are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClearResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> ClearResult | HTTPValidationError | None:
    """Clear

     Clears the queue entirely. Admin users clear all items; non-admin users only clear their own items.
    If there's a currently-executing item, users can only cancel it if they own it or are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClearResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
        )
    ).parsed
