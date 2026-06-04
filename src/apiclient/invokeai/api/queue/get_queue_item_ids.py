from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.item_ids_result import ItemIdsResult
from ...models.sq_lite_direction import SQLiteDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    *,
    order_dir: SQLiteDirection | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_order_dir: str | Unset = UNSET
    if not isinstance(order_dir, Unset):
        json_order_dir = order_dir.value

    params["order_dir"] = json_order_dir

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/queue/{queue_id}/item_ids".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ItemIdsResult | None:
    if response.status_code == 200:
        response_200 = ItemIdsResult.from_dict(response.json())

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
) -> Response[HTTPValidationError | ItemIdsResult]:
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
    order_dir: SQLiteDirection | Unset = UNSET,
) -> Response[HTTPValidationError | ItemIdsResult]:
    """Get Queue Item Ids

     Gets all queue item ids that match the given parameters. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        order_dir (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ItemIdsResult]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        order_dir=order_dir,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    order_dir: SQLiteDirection | Unset = UNSET,
) -> HTTPValidationError | ItemIdsResult | None:
    """Get Queue Item Ids

     Gets all queue item ids that match the given parameters. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        order_dir (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ItemIdsResult
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        order_dir=order_dir,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    order_dir: SQLiteDirection | Unset = UNSET,
) -> Response[HTTPValidationError | ItemIdsResult]:
    """Get Queue Item Ids

     Gets all queue item ids that match the given parameters. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        order_dir (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ItemIdsResult]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        order_dir=order_dir,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    order_dir: SQLiteDirection | Unset = UNSET,
) -> HTTPValidationError | ItemIdsResult | None:
    """Get Queue Item Ids

     Gets all queue item ids that match the given parameters. Non-admin users only see their own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        order_dir (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ItemIdsResult
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            order_dir=order_dir,
        )
    ).parsed
