from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_get_queue_items_by_item_ids import BodyGetQueueItemsByItemIds
from ...models.http_validation_error import HTTPValidationError
from ...models.session_queue_item import SessionQueueItem
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    body: BodyGetQueueItemsByItemIds,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/queue/{queue_id}/items_by_ids".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: BodyGetQueueItemsByItemIds,
) -> Response[HTTPValidationError | list[SessionQueueItem]]:
    """Get Queue Items By Item Ids

     Gets queue items for the specified queue item ids. Maintains order of item ids.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyGetQueueItemsByItemIds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SessionQueueItem]]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyGetQueueItemsByItemIds,
) -> HTTPValidationError | list[SessionQueueItem] | None:
    """Get Queue Items By Item Ids

     Gets queue items for the specified queue item ids. Maintains order of item ids.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyGetQueueItemsByItemIds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SessionQueueItem]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyGetQueueItemsByItemIds,
) -> Response[HTTPValidationError | list[SessionQueueItem]]:
    """Get Queue Items By Item Ids

     Gets queue items for the specified queue item ids. Maintains order of item ids.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyGetQueueItemsByItemIds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SessionQueueItem]]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyGetQueueItemsByItemIds,
) -> HTTPValidationError | list[SessionQueueItem] | None:
    """Get Queue Items By Item Ids

     Gets queue items for the specified queue item ids. Maintains order of item ids.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyGetQueueItemsByItemIds):

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
            body=body,
        )
    ).parsed
