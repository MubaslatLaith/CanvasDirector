from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_recall_parameters_response_get_recall_parameters import (
    GetRecallParametersResponseGetRecallParameters,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    queue_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recall/{queue_id}".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRecallParametersResponseGetRecallParameters | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GetRecallParametersResponseGetRecallParameters.from_dict(response.json())

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
) -> Response[GetRecallParametersResponseGetRecallParameters | HTTPValidationError]:
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
) -> Response[GetRecallParametersResponseGetRecallParameters | HTTPValidationError]:
    """Get Recall Parameters

     Retrieve all stored recall parameters for a given queue.

    Returns a dictionary of all recall parameters that have been set for the queue.

    Args:
        queue_id: The queue ID to retrieve parameters for

    Returns:
        A dictionary containing all stored recall parameters

    Args:
        queue_id (str): The queue id to retrieve parameters for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRecallParametersResponseGetRecallParameters | HTTPValidationError]
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
) -> GetRecallParametersResponseGetRecallParameters | HTTPValidationError | None:
    """Get Recall Parameters

     Retrieve all stored recall parameters for a given queue.

    Returns a dictionary of all recall parameters that have been set for the queue.

    Args:
        queue_id: The queue ID to retrieve parameters for

    Returns:
        A dictionary containing all stored recall parameters

    Args:
        queue_id (str): The queue id to retrieve parameters for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRecallParametersResponseGetRecallParameters | HTTPValidationError
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetRecallParametersResponseGetRecallParameters | HTTPValidationError]:
    """Get Recall Parameters

     Retrieve all stored recall parameters for a given queue.

    Returns a dictionary of all recall parameters that have been set for the queue.

    Args:
        queue_id: The queue ID to retrieve parameters for

    Returns:
        A dictionary containing all stored recall parameters

    Args:
        queue_id (str): The queue id to retrieve parameters for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRecallParametersResponseGetRecallParameters | HTTPValidationError]
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
) -> GetRecallParametersResponseGetRecallParameters | HTTPValidationError | None:
    """Get Recall Parameters

     Retrieve all stored recall parameters for a given queue.

    Returns a dictionary of all recall parameters that have been set for the queue.

    Args:
        queue_id: The queue ID to retrieve parameters for

    Returns:
        A dictionary containing all stored recall parameters

    Args:
        queue_id (str): The queue id to retrieve parameters for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRecallParametersResponseGetRecallParameters | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
        )
    ).parsed
