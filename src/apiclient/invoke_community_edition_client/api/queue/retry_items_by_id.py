from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.retry_items_result import RetryItemsResult
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    body: list[int],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/queue/{queue_id}/retry_items_by_id".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | RetryItemsResult | None:
    if response.status_code == 200:
        response_200 = RetryItemsResult.from_dict(response.json())

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
) -> Response[HTTPValidationError | RetryItemsResult]:
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
    body: list[int],
) -> Response[HTTPValidationError | RetryItemsResult]:
    """Retry Items By Id

     Retries the given queue items. Users can only retry their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (list[int]): The queue item ids to retry

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RetryItemsResult]
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
    body: list[int],
) -> HTTPValidationError | RetryItemsResult | None:
    """Retry Items By Id

     Retries the given queue items. Users can only retry their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (list[int]): The queue item ids to retry

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RetryItemsResult
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
    body: list[int],
) -> Response[HTTPValidationError | RetryItemsResult]:
    """Retry Items By Id

     Retries the given queue items. Users can only retry their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (list[int]): The queue item ids to retry

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RetryItemsResult]
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
    body: list[int],
) -> HTTPValidationError | RetryItemsResult | None:
    """Retry Items By Id

     Retries the given queue items. Users can only retry their own items unless they are an admin.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (list[int]): The queue item ids to retry

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RetryItemsResult
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            body=body,
        )
    ).parsed
