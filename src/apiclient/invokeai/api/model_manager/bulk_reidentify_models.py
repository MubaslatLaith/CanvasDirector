from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_reidentify_models_request import BulkReidentifyModelsRequest
from ...models.bulk_reidentify_models_response import BulkReidentifyModelsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BulkReidentifyModelsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/models/i/bulk_reidentify",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkReidentifyModelsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkReidentifyModelsResponse.from_dict(response.json())

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
) -> Response[BulkReidentifyModelsResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkReidentifyModelsRequest,
) -> Response[BulkReidentifyModelsResponse | HTTPValidationError]:
    """Bulk Reidentify Models

     Reidentify multiple models by re-probing their weights files.

    Returns a list of successfully reidentified keys and failed reidentifications with error messages.

    Args:
        body (BulkReidentifyModelsRequest): Request body for bulk model reidentification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkReidentifyModelsResponse | HTTPValidationError]
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
    body: BulkReidentifyModelsRequest,
) -> BulkReidentifyModelsResponse | HTTPValidationError | None:
    """Bulk Reidentify Models

     Reidentify multiple models by re-probing their weights files.

    Returns a list of successfully reidentified keys and failed reidentifications with error messages.

    Args:
        body (BulkReidentifyModelsRequest): Request body for bulk model reidentification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkReidentifyModelsResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkReidentifyModelsRequest,
) -> Response[BulkReidentifyModelsResponse | HTTPValidationError]:
    """Bulk Reidentify Models

     Reidentify multiple models by re-probing their weights files.

    Returns a list of successfully reidentified keys and failed reidentifications with error messages.

    Args:
        body (BulkReidentifyModelsRequest): Request body for bulk model reidentification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkReidentifyModelsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkReidentifyModelsRequest,
) -> BulkReidentifyModelsResponse | HTTPValidationError | None:
    """Bulk Reidentify Models

     Reidentify multiple models by re-probing their weights files.

    Returns a list of successfully reidentified keys and failed reidentifications with error messages.

    Args:
        body (BulkReidentifyModelsRequest): Request body for bulk model reidentification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkReidentifyModelsResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
