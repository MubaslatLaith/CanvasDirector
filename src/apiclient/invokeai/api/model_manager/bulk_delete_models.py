from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_delete_models_request import BulkDeleteModelsRequest
from ...models.bulk_delete_models_response import BulkDeleteModelsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BulkDeleteModelsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/models/i/bulk_delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkDeleteModelsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkDeleteModelsResponse.from_dict(response.json())

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
) -> Response[BulkDeleteModelsResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDeleteModelsRequest,
) -> Response[BulkDeleteModelsResponse | HTTPValidationError]:
    r"""Bulk Delete Models

     Delete multiple model records from database.

    The configuration records will be removed. The corresponding weights files will be
    deleted as well if they reside within the InvokeAI \"models\" directory.
    Returns a list of successfully deleted keys and failed deletions with error messages.

    Args:
        body (BulkDeleteModelsRequest): Request body for bulk model deletion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDeleteModelsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BulkDeleteModelsRequest,
) -> BulkDeleteModelsResponse | HTTPValidationError | None:
    r"""Bulk Delete Models

     Delete multiple model records from database.

    The configuration records will be removed. The corresponding weights files will be
    deleted as well if they reside within the InvokeAI \"models\" directory.
    Returns a list of successfully deleted keys and failed deletions with error messages.

    Args:
        body (BulkDeleteModelsRequest): Request body for bulk model deletion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDeleteModelsResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDeleteModelsRequest,
) -> Response[BulkDeleteModelsResponse | HTTPValidationError]:
    r"""Bulk Delete Models

     Delete multiple model records from database.

    The configuration records will be removed. The corresponding weights files will be
    deleted as well if they reside within the InvokeAI \"models\" directory.
    Returns a list of successfully deleted keys and failed deletions with error messages.

    Args:
        body (BulkDeleteModelsRequest): Request body for bulk model deletion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDeleteModelsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkDeleteModelsRequest,
) -> BulkDeleteModelsResponse | HTTPValidationError | None:
    r"""Bulk Delete Models

     Delete multiple model records from database.

    The configuration records will be removed. The corresponding weights files will be
    deleted as well if they reside within the InvokeAI \"models\" directory.
    Returns a list of successfully deleted keys and failed deletions with error messages.

    Args:
        body (BulkDeleteModelsRequest): Request body for bulk model deletion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDeleteModelsResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
