from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session_queue_item import SessionQueueItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    *,
    destination: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_destination: None | str | Unset
    if isinstance(destination, Unset):
        json_destination = UNSET
    else:
        json_destination = destination
    params["destination"] = json_destination

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/queue/{queue_id}/list_all".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[SessionQueueItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SessionQueueItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[SessionQueueItem]]:
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
    destination: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[SessionQueueItem]]:
    """List All Queue Items

     Gets all queue items

    Args:
        queue_id (str): The queue id to perform this operation on
        destination (None | str | Unset): The destination of queue items to fetch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SessionQueueItem]]
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
    destination: None | str | Unset = UNSET,
) -> HTTPValidationError | list[SessionQueueItem] | None:
    """List All Queue Items

     Gets all queue items

    Args:
        queue_id (str): The queue id to perform this operation on
        destination (None | str | Unset): The destination of queue items to fetch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SessionQueueItem]
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
    destination: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[SessionQueueItem]]:
    """List All Queue Items

     Gets all queue items

    Args:
        queue_id (str): The queue id to perform this operation on
        destination (None | str | Unset): The destination of queue items to fetch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SessionQueueItem]]
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
    destination: None | str | Unset = UNSET,
) -> HTTPValidationError | list[SessionQueueItem] | None:
    """List All Queue Items

     Gets all queue items

    Args:
        queue_id (str): The queue id to perform this operation on
        destination (None | str | Unset): The destination of queue items to fetch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SessionQueueItem]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            destination=destination,
        )
    ).parsed
