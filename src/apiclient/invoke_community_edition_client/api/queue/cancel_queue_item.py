from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session_queue_item import SessionQueueItem
from ...types import Response


def _get_kwargs(
    queue_id: str,
    item_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/queue/{queue_id}/i/{item_id}/cancel".format(
            queue_id=quote(str(queue_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SessionQueueItem | None:
    if response.status_code == 200:
        response_200 = SessionQueueItem.from_dict(response.json())

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
) -> Response[HTTPValidationError | SessionQueueItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_id: str,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SessionQueueItem]:
    """Cancel Queue Item

     Cancels a queue item. Users can only cancel their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        item_id (int): The queue item to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionQueueItem]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SessionQueueItem | None:
    """Cancel Queue Item

     Cancels a queue item. Users can only cancel their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        item_id (int): The queue item to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionQueueItem
    """

    return sync_detailed(
        queue_id=queue_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SessionQueueItem]:
    """Cancel Queue Item

     Cancels a queue item. Users can only cancel their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        item_id (int): The queue item to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionQueueItem]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SessionQueueItem | None:
    """Cancel Queue Item

     Cancels a queue item. Users can only cancel their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        item_id (int): The queue item to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionQueueItem
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
