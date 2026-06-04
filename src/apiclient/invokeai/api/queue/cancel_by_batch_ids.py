from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_cancel_by_batch_ids import BodyCancelByBatchIds
from ...models.cancel_by_batch_i_ds_result import CancelByBatchIDsResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    body: BodyCancelByBatchIds,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/queue/{queue_id}/cancel_by_batch_ids".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelByBatchIDsResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CancelByBatchIDsResult.from_dict(response.json())

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
) -> Response[CancelByBatchIDsResult | HTTPValidationError]:
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
    body: BodyCancelByBatchIds,
) -> Response[CancelByBatchIDsResult | HTTPValidationError]:
    """Cancel By Batch Ids

     Immediately cancels all queue items from the given batch ids. Non-admin users can only cancel their
    own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyCancelByBatchIds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelByBatchIDsResult | HTTPValidationError]
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
    body: BodyCancelByBatchIds,
) -> CancelByBatchIDsResult | HTTPValidationError | None:
    """Cancel By Batch Ids

     Immediately cancels all queue items from the given batch ids. Non-admin users can only cancel their
    own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyCancelByBatchIds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelByBatchIDsResult | HTTPValidationError
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
    body: BodyCancelByBatchIds,
) -> Response[CancelByBatchIDsResult | HTTPValidationError]:
    """Cancel By Batch Ids

     Immediately cancels all queue items from the given batch ids. Non-admin users can only cancel their
    own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyCancelByBatchIds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelByBatchIDsResult | HTTPValidationError]
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
    body: BodyCancelByBatchIds,
) -> CancelByBatchIDsResult | HTTPValidationError | None:
    """Cancel By Batch Ids

     Immediately cancels all queue items from the given batch ids. Non-admin users can only cancel their
    own items.

    Args:
        queue_id (str): The queue id to perform this operation on
        body (BodyCancelByBatchIds):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelByBatchIDsResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            body=body,
        )
    ).parsed
