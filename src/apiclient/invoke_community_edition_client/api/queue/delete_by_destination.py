from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_by_destination_result import DeleteByDestinationResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    queue_id: str,
    destination: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/queue/{queue_id}/d/{destination}".format(
            queue_id=quote(str(queue_id), safe=""),
            destination=quote(str(destination), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteByDestinationResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeleteByDestinationResult.from_dict(response.json())

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
) -> Response[DeleteByDestinationResult | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_id: str,
    destination: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteByDestinationResult | HTTPValidationError]:
    """Delete By Destination

     Deletes all items with the given destination. Non-admin users can only delete their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByDestinationResult | HTTPValidationError]
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
    destination: str,
    *,
    client: AuthenticatedClient,
) -> DeleteByDestinationResult | HTTPValidationError | None:
    """Delete By Destination

     Deletes all items with the given destination. Non-admin users can only delete their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByDestinationResult | HTTPValidationError
    """

    return sync_detailed(
        queue_id=queue_id,
        destination=destination,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    destination: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteByDestinationResult | HTTPValidationError]:
    """Delete By Destination

     Deletes all items with the given destination. Non-admin users can only delete their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByDestinationResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        destination=destination,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    destination: str,
    *,
    client: AuthenticatedClient,
) -> DeleteByDestinationResult | HTTPValidationError | None:
    """Delete By Destination

     Deletes all items with the given destination. Non-admin users can only delete their own items.

    Args:
        queue_id (str): The queue id to query
        destination (str): The destination to query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByDestinationResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            destination=destination,
            client=client,
        )
    ).parsed
