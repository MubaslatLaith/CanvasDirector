from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_images_result import DeleteImagesResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    image_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/images/i/{image_name}".format(
            image_name=quote(str(image_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteImagesResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeleteImagesResult.from_dict(response.json())

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
) -> Response[DeleteImagesResult | HTTPValidationError]:
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
) -> Response[DeleteImagesResult | HTTPValidationError]:
    """Delete Image

     Deletes an image

    Args:
        image_name (str): The name of the image to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteImagesResult | HTTPValidationError]
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
) -> DeleteImagesResult | HTTPValidationError | None:
    """Delete Image

     Deletes an image

    Args:
        image_name (str): The name of the image to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteImagesResult | HTTPValidationError
    """

    return sync_detailed(
        image_name=image_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    image_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteImagesResult | HTTPValidationError]:
    """Delete Image

     Deletes an image

    Args:
        image_name (str): The name of the image to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteImagesResult | HTTPValidationError]
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
) -> DeleteImagesResult | HTTPValidationError | None:
    """Delete Image

     Deletes an image

    Args:
        image_name (str): The name of the image to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteImagesResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            image_name=image_name,
            client=client,
        )
    ).parsed
