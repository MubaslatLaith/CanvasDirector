from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    bulk_download_item_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/images/download/{bulk_download_item_name}".format(
            bulk_download_item_name=quote(str(bulk_download_item_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bulk_download_item_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
    """Get Bulk Download Item

     Gets a bulk download zip file.

    Requires authentication.  The caller must be the user who initiated the
    download (tracked by the bulk download service) or an admin.

    Args:
        bulk_download_item_name (str): The bulk_download_item_name of the bulk download item to
            get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bulk_download_item_name=bulk_download_item_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bulk_download_item_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
    """Get Bulk Download Item

     Gets a bulk download zip file.

    Requires authentication.  The caller must be the user who initiated the
    download (tracked by the bulk download service) or an admin.

    Args:
        bulk_download_item_name (str): The bulk_download_item_name of the bulk download item to
            get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        bulk_download_item_name=bulk_download_item_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    bulk_download_item_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
    """Get Bulk Download Item

     Gets a bulk download zip file.

    Requires authentication.  The caller must be the user who initiated the
    download (tracked by the bulk download service) or an admin.

    Args:
        bulk_download_item_name (str): The bulk_download_item_name of the bulk download item to
            get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bulk_download_item_name=bulk_download_item_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bulk_download_item_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
    """Get Bulk Download Item

     Gets a bulk download zip file.

    Requires authentication.  The caller must be the user who initiated the
    download (tracked by the bulk download service) or an admin.

    Args:
        bulk_download_item_name (str): The bulk_download_item_name of the bulk download item to
            get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bulk_download_item_name=bulk_download_item_name,
            client=client,
        )
    ).parsed
