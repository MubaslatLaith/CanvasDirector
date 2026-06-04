from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_image import BodyUploadImage
from ...models.http_validation_error import HTTPValidationError
from ...models.image_category import ImageCategory
from ...models.image_dto import ImageDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyUploadImage,
    image_category: ImageCategory,
    is_intermediate: bool,
    board_id: None | str | Unset = UNSET,
    session_id: None | str | Unset = UNSET,
    crop_visible: bool | None | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_image_category = image_category.value
    params["image_category"] = json_image_category

    params["is_intermediate"] = is_intermediate

    json_board_id: None | str | Unset
    if isinstance(board_id, Unset):
        json_board_id = UNSET
    else:
        json_board_id = board_id
    params["board_id"] = json_board_id

    json_session_id: None | str | Unset
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_crop_visible: bool | None | Unset
    if isinstance(crop_visible, Unset):
        json_crop_visible = UNSET
    else:
        json_crop_visible = crop_visible
    params["crop_visible"] = json_crop_visible

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/images/upload",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | ImageDTO | None:
    if response.status_code == 201:
        response_201 = ImageDTO.from_dict(response.json())

        return response_201

    if response.status_code == 415:
        response_415 = cast(Any, None)
        return response_415

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | ImageDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadImage,
    image_category: ImageCategory,
    is_intermediate: bool,
    board_id: None | str | Unset = UNSET,
    session_id: None | str | Unset = UNSET,
    crop_visible: bool | None | Unset = False,
) -> Response[Any | HTTPValidationError | ImageDTO]:
    """Upload Image

     Uploads an image for the current user

    Args:
        image_category (ImageCategory): The category of an image.

            - GENERAL: The image is an output, init image, or otherwise an image without a specialized
            purpose.
            - MASK: The image is a mask image.
            - CONTROL: The image is a ControlNet control image.
            - USER: The image is a user-provide image.
            - OTHER: The image is some other type of image with a specialized purpose. To be used by
            external nodes.
        is_intermediate (bool): Whether this is an intermediate image
        board_id (None | str | Unset): The board to add this image to, if any
        session_id (None | str | Unset): The session ID associated with this upload, if any
        crop_visible (bool | None | Unset): Whether to crop the image Default: False.
        body (BodyUploadImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ImageDTO]
    """

    kwargs = _get_kwargs(
        body=body,
        image_category=image_category,
        is_intermediate=is_intermediate,
        board_id=board_id,
        session_id=session_id,
        crop_visible=crop_visible,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyUploadImage,
    image_category: ImageCategory,
    is_intermediate: bool,
    board_id: None | str | Unset = UNSET,
    session_id: None | str | Unset = UNSET,
    crop_visible: bool | None | Unset = False,
) -> Any | HTTPValidationError | ImageDTO | None:
    """Upload Image

     Uploads an image for the current user

    Args:
        image_category (ImageCategory): The category of an image.

            - GENERAL: The image is an output, init image, or otherwise an image without a specialized
            purpose.
            - MASK: The image is a mask image.
            - CONTROL: The image is a ControlNet control image.
            - USER: The image is a user-provide image.
            - OTHER: The image is some other type of image with a specialized purpose. To be used by
            external nodes.
        is_intermediate (bool): Whether this is an intermediate image
        board_id (None | str | Unset): The board to add this image to, if any
        session_id (None | str | Unset): The session ID associated with this upload, if any
        crop_visible (bool | None | Unset): Whether to crop the image Default: False.
        body (BodyUploadImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ImageDTO
    """

    return sync_detailed(
        client=client,
        body=body,
        image_category=image_category,
        is_intermediate=is_intermediate,
        board_id=board_id,
        session_id=session_id,
        crop_visible=crop_visible,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadImage,
    image_category: ImageCategory,
    is_intermediate: bool,
    board_id: None | str | Unset = UNSET,
    session_id: None | str | Unset = UNSET,
    crop_visible: bool | None | Unset = False,
) -> Response[Any | HTTPValidationError | ImageDTO]:
    """Upload Image

     Uploads an image for the current user

    Args:
        image_category (ImageCategory): The category of an image.

            - GENERAL: The image is an output, init image, or otherwise an image without a specialized
            purpose.
            - MASK: The image is a mask image.
            - CONTROL: The image is a ControlNet control image.
            - USER: The image is a user-provide image.
            - OTHER: The image is some other type of image with a specialized purpose. To be used by
            external nodes.
        is_intermediate (bool): Whether this is an intermediate image
        board_id (None | str | Unset): The board to add this image to, if any
        session_id (None | str | Unset): The session ID associated with this upload, if any
        crop_visible (bool | None | Unset): Whether to crop the image Default: False.
        body (BodyUploadImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ImageDTO]
    """

    kwargs = _get_kwargs(
        body=body,
        image_category=image_category,
        is_intermediate=is_intermediate,
        board_id=board_id,
        session_id=session_id,
        crop_visible=crop_visible,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyUploadImage,
    image_category: ImageCategory,
    is_intermediate: bool,
    board_id: None | str | Unset = UNSET,
    session_id: None | str | Unset = UNSET,
    crop_visible: bool | None | Unset = False,
) -> Any | HTTPValidationError | ImageDTO | None:
    """Upload Image

     Uploads an image for the current user

    Args:
        image_category (ImageCategory): The category of an image.

            - GENERAL: The image is an output, init image, or otherwise an image without a specialized
            purpose.
            - MASK: The image is a mask image.
            - CONTROL: The image is a ControlNet control image.
            - USER: The image is a user-provide image.
            - OTHER: The image is some other type of image with a specialized purpose. To be used by
            external nodes.
        is_intermediate (bool): Whether this is an intermediate image
        board_id (None | str | Unset): The board to add this image to, if any
        session_id (None | str | Unset): The session ID associated with this upload, if any
        crop_visible (bool | None | Unset): Whether to crop the image Default: False.
        body (BodyUploadImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ImageDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            image_category=image_category,
            is_intermediate=is_intermediate,
            board_id=board_id,
            session_id=session_id,
            crop_visible=crop_visible,
        )
    ).parsed
