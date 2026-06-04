from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.metadata_field import MetadataField
from ...types import Response


def _get_kwargs(
    image_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/images/i/{image_name}/metadata".format(
            image_name=quote(str(image_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MetadataField | None | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> MetadataField | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = MetadataField.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataField | None, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[HTTPValidationError | MetadataField | None]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    image_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | MetadataField | None]:
    """Get Image Metadata

     Gets an image's metadata

    Args:
        image_name (str): The name of image to get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MetadataField | None]
    """

    kwargs = _get_kwargs(
        image_name=image_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    image_name: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | MetadataField | None | None:
    """Get Image Metadata

     Gets an image's metadata

    Args:
        image_name (str): The name of image to get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MetadataField | None
    """

    return sync_detailed(
        image_name=image_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    image_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | MetadataField | None]:
    """Get Image Metadata

     Gets an image's metadata

    Args:
        image_name (str): The name of image to get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MetadataField | None]
    """

    kwargs = _get_kwargs(
        image_name=image_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    image_name: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | MetadataField | None | None:
    """Get Image Metadata

     Gets an image's metadata

    Args:
        image_name (str): The name of image to get

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MetadataField | None
    """

    return (
        await asyncio_detailed(
            image_name=image_name,
            client=client,
        )
    ).parsed
