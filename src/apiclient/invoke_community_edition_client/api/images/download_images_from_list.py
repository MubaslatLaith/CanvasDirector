from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_download_images_from_list import BodyDownloadImagesFromList
from ...models.http_validation_error import HTTPValidationError
from ...models.images_downloaded import ImagesDownloaded
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyDownloadImagesFromList | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/images/download",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ImagesDownloaded | None:
    if response.status_code == 202:
        response_202 = ImagesDownloaded.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | ImagesDownloaded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyDownloadImagesFromList | Unset = UNSET,
) -> Response[HTTPValidationError | ImagesDownloaded]:
    """Download Images From List

    Args:
        body (BodyDownloadImagesFromList | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ImagesDownloaded]
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
    body: BodyDownloadImagesFromList | Unset = UNSET,
) -> HTTPValidationError | ImagesDownloaded | None:
    """Download Images From List

    Args:
        body (BodyDownloadImagesFromList | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ImagesDownloaded
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyDownloadImagesFromList | Unset = UNSET,
) -> Response[HTTPValidationError | ImagesDownloaded]:
    """Download Images From List

    Args:
        body (BodyDownloadImagesFromList | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ImagesDownloaded]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyDownloadImagesFromList | Unset = UNSET,
) -> HTTPValidationError | ImagesDownloaded | None:
    """Download Images From List

    Args:
        body (BodyDownloadImagesFromList | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ImagesDownloaded
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
