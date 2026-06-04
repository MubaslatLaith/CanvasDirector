from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.image_dto import ImageDTO
from ...models.image_record_changes import ImageRecordChanges
from ...types import Response


def _get_kwargs(
    image_name: str,
    *,
    body: ImageRecordChanges,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/images/i/{image_name}".format(
            image_name=quote(str(image_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ImageDTO | None:
    if response.status_code == 200:
        response_200 = ImageDTO.from_dict(response.json())

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
) -> Response[HTTPValidationError | ImageDTO]:
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
    body: ImageRecordChanges,
) -> Response[HTTPValidationError | ImageDTO]:
    """Update Image

     Updates an image

    Args:
        image_name (str): The name of the image to update
        body (ImageRecordChanges): A set of changes to apply to an image record.

            Only limited changes are valid:
              - `image_category`: change the category of an image
              - `session_id`: change the session associated with an image
              - `is_intermediate`: change the image's `is_intermediate` flag
              - `starred`: change whether the image is starred

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ImageDTO]
    """

    kwargs = _get_kwargs(
        image_name=image_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    image_name: str,
    *,
    client: AuthenticatedClient,
    body: ImageRecordChanges,
) -> HTTPValidationError | ImageDTO | None:
    """Update Image

     Updates an image

    Args:
        image_name (str): The name of the image to update
        body (ImageRecordChanges): A set of changes to apply to an image record.

            Only limited changes are valid:
              - `image_category`: change the category of an image
              - `session_id`: change the session associated with an image
              - `is_intermediate`: change the image's `is_intermediate` flag
              - `starred`: change whether the image is starred

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ImageDTO
    """

    return sync_detailed(
        image_name=image_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    image_name: str,
    *,
    client: AuthenticatedClient,
    body: ImageRecordChanges,
) -> Response[HTTPValidationError | ImageDTO]:
    """Update Image

     Updates an image

    Args:
        image_name (str): The name of the image to update
        body (ImageRecordChanges): A set of changes to apply to an image record.

            Only limited changes are valid:
              - `image_category`: change the category of an image
              - `session_id`: change the session associated with an image
              - `is_intermediate`: change the image's `is_intermediate` flag
              - `starred`: change whether the image is starred

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ImageDTO]
    """

    kwargs = _get_kwargs(
        image_name=image_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    image_name: str,
    *,
    client: AuthenticatedClient,
    body: ImageRecordChanges,
) -> HTTPValidationError | ImageDTO | None:
    """Update Image

     Updates an image

    Args:
        image_name (str): The name of the image to update
        body (ImageRecordChanges): A set of changes to apply to an image record.

            Only limited changes are valid:
              - `image_category`: change the category of an image
              - `session_id`: change the session associated with an image
              - `is_intermediate`: change the image's `is_intermediate` flag
              - `starred`: change whether the image is starred

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ImageDTO
    """

    return (
        await asyncio_detailed(
            image_name=image_name,
            client=client,
            body=body,
        )
    ).parsed
