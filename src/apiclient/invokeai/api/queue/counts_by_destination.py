from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session_queue_counts_by_destination import SessionQueueCountsByDestination
from ...types import UNSET, Response


def _get_kwargs(
    queue_id: str,
    *,
    destination: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["destination"] = destination

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/queue/{queue_id}/counts_by_destination".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SessionQueueCountsByDestination | None:
    if response.status_code == 200:
        response_200 = SessionQueueCountsByDestination.from_dict(response.json())

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
) -> Response[HTTPValidationError | SessionQueueCountsByDestination]:
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
    destination: str,
) -> Response[HTTPValidationError | SessionQueueCountsByDestination]:
    """Counts By Destination

     Gets the counts of queue items by destination. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionQueueCountsByDestination]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        destination=destination,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    destination: str,
) -> HTTPValidationError | SessionQueueCountsByDestination | None:
    """Counts By Destination

     Gets the counts of queue items by destination. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionQueueCountsByDestination
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        destination=destination,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    destination: str,
) -> Response[HTTPValidationError | SessionQueueCountsByDestination]:
    """Counts By Destination

     Gets the counts of queue items by destination. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionQueueCountsByDestination]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        destination=destination,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    destination: str,
) -> HTTPValidationError | SessionQueueCountsByDestination | None:
    """Counts By Destination

     Gets the counts of queue items by destination. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionQueueCountsByDestination
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            destination=destination,
        )
    ).parsed
