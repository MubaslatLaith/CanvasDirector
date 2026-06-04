from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_all_except_current_result import CancelAllExceptCurrentResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    queue_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/queue/{queue_id}/cancel_all_except_current".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelAllExceptCurrentResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CancelAllExceptCurrentResult.from_dict(response.json())

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
) -> Response[CancelAllExceptCurrentResult | HTTPValidationError]:
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
) -> Response[CancelAllExceptCurrentResult | HTTPValidationError]:
    """Cancel All Except Current

     Immediately cancels all queue items except in-processing items. Non-admin users can only cancel
    their own items.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelAllExceptCurrentResult | HTTPValidationError]
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
) -> CancelAllExceptCurrentResult | HTTPValidationError | None:
    """Cancel All Except Current

     Immediately cancels all queue items except in-processing items. Non-admin users can only cancel
    their own items.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelAllExceptCurrentResult | HTTPValidationError
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CancelAllExceptCurrentResult | HTTPValidationError]:
    """Cancel All Except Current

     Immediately cancels all queue items except in-processing items. Non-admin users can only cancel
    their own items.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelAllExceptCurrentResult | HTTPValidationError]
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
) -> CancelAllExceptCurrentResult | HTTPValidationError | None:
    """Cancel All Except Current

     Immediately cancels all queue items except in-processing items. Non-admin users can only cancel
    their own items.

    Args:
        queue_id (str): The queue id to perform this operation on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelAllExceptCurrentResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
        )
    ).parsed
