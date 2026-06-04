from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.image_category import ImageCategory
from ...models.offset_paginated_results_image_dto import OffsetPaginatedResultsImageDTO
from ...models.resource_origin import ResourceOrigin
from ...models.sq_lite_direction import SQLiteDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    image_origin: None | ResourceOrigin | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    is_intermediate: bool | None | Unset = UNSET,
    board_id: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    order_dir: SQLiteDirection | Unset = UNSET,
    starred_first: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_image_origin: None | str | Unset
    if isinstance(image_origin, Unset):
        json_image_origin = UNSET
    elif isinstance(image_origin, ResourceOrigin):
        json_image_origin = image_origin.value
    else:
        json_image_origin = image_origin
    params["image_origin"] = json_image_origin

    json_categories: list[str] | None | Unset
    if isinstance(categories, Unset):
        json_categories = UNSET
    elif isinstance(categories, list):
        json_categories = []
        for categories_type_0_item_data in categories:
            categories_type_0_item = categories_type_0_item_data.value
            json_categories.append(categories_type_0_item)

    else:
        json_categories = categories
    params["categories"] = json_categories

    json_is_intermediate: bool | None | Unset
    if isinstance(is_intermediate, Unset):
        json_is_intermediate = UNSET
    else:
        json_is_intermediate = is_intermediate
    params["is_intermediate"] = json_is_intermediate

    json_board_id: None | str | Unset
    if isinstance(board_id, Unset):
        json_board_id = UNSET
    else:
        json_board_id = board_id
    params["board_id"] = json_board_id

    params["offset"] = offset

    params["limit"] = limit

    json_order_dir: str | Unset = UNSET
    if not isinstance(order_dir, Unset):
        json_order_dir = order_dir.value

    params["order_dir"] = json_order_dir

    params["starred_first"] = starred_first

    json_search_term: None | str | Unset
    if isinstance(search_term, Unset):
        json_search_term = UNSET
    else:
        json_search_term = search_term
    params["search_term"] = json_search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/images/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | OffsetPaginatedResultsImageDTO | None:
    if response.status_code == 200:
        response_200 = OffsetPaginatedResultsImageDTO.from_dict(response.json())

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
) -> Response[HTTPValidationError | OffsetPaginatedResultsImageDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    image_origin: None | ResourceOrigin | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    is_intermediate: bool | None | Unset = UNSET,
    board_id: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    order_dir: SQLiteDirection | Unset = UNSET,
    starred_first: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OffsetPaginatedResultsImageDTO]:
    """List Image Dtos

     Gets a list of image DTOs for the current user

    Args:
        image_origin (None | ResourceOrigin | Unset): The origin of images to list.
        categories (list[ImageCategory] | None | Unset): The categories of image to include.
        is_intermediate (bool | None | Unset): Whether to list intermediate images.
        board_id (None | str | Unset): The board id to filter by. Use 'none' to find images
            without a board.
        offset (int | Unset): The page offset Default: 0.
        limit (int | Unset): The number of images per page Default: 10.
        order_dir (SQLiteDirection | Unset):
        starred_first (bool | Unset): Whether to sort by starred images first Default: True.
        search_term (None | str | Unset): The term to search for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OffsetPaginatedResultsImageDTO]
    """

    kwargs = _get_kwargs(
        image_origin=image_origin,
        categories=categories,
        is_intermediate=is_intermediate,
        board_id=board_id,
        offset=offset,
        limit=limit,
        order_dir=order_dir,
        starred_first=starred_first,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    image_origin: None | ResourceOrigin | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    is_intermediate: bool | None | Unset = UNSET,
    board_id: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    order_dir: SQLiteDirection | Unset = UNSET,
    starred_first: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
) -> HTTPValidationError | OffsetPaginatedResultsImageDTO | None:
    """List Image Dtos

     Gets a list of image DTOs for the current user

    Args:
        image_origin (None | ResourceOrigin | Unset): The origin of images to list.
        categories (list[ImageCategory] | None | Unset): The categories of image to include.
        is_intermediate (bool | None | Unset): Whether to list intermediate images.
        board_id (None | str | Unset): The board id to filter by. Use 'none' to find images
            without a board.
        offset (int | Unset): The page offset Default: 0.
        limit (int | Unset): The number of images per page Default: 10.
        order_dir (SQLiteDirection | Unset):
        starred_first (bool | Unset): Whether to sort by starred images first Default: True.
        search_term (None | str | Unset): The term to search for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OffsetPaginatedResultsImageDTO
    """

    return sync_detailed(
        client=client,
        image_origin=image_origin,
        categories=categories,
        is_intermediate=is_intermediate,
        board_id=board_id,
        offset=offset,
        limit=limit,
        order_dir=order_dir,
        starred_first=starred_first,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    image_origin: None | ResourceOrigin | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    is_intermediate: bool | None | Unset = UNSET,
    board_id: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    order_dir: SQLiteDirection | Unset = UNSET,
    starred_first: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OffsetPaginatedResultsImageDTO]:
    """List Image Dtos

     Gets a list of image DTOs for the current user

    Args:
        image_origin (None | ResourceOrigin | Unset): The origin of images to list.
        categories (list[ImageCategory] | None | Unset): The categories of image to include.
        is_intermediate (bool | None | Unset): Whether to list intermediate images.
        board_id (None | str | Unset): The board id to filter by. Use 'none' to find images
            without a board.
        offset (int | Unset): The page offset Default: 0.
        limit (int | Unset): The number of images per page Default: 10.
        order_dir (SQLiteDirection | Unset):
        starred_first (bool | Unset): Whether to sort by starred images first Default: True.
        search_term (None | str | Unset): The term to search for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OffsetPaginatedResultsImageDTO]
    """

    kwargs = _get_kwargs(
        image_origin=image_origin,
        categories=categories,
        is_intermediate=is_intermediate,
        board_id=board_id,
        offset=offset,
        limit=limit,
        order_dir=order_dir,
        starred_first=starred_first,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    image_origin: None | ResourceOrigin | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    is_intermediate: bool | None | Unset = UNSET,
    board_id: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    order_dir: SQLiteDirection | Unset = UNSET,
    starred_first: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
) -> HTTPValidationError | OffsetPaginatedResultsImageDTO | None:
    """List Image Dtos

     Gets a list of image DTOs for the current user

    Args:
        image_origin (None | ResourceOrigin | Unset): The origin of images to list.
        categories (list[ImageCategory] | None | Unset): The categories of image to include.
        is_intermediate (bool | None | Unset): Whether to list intermediate images.
        board_id (None | str | Unset): The board id to filter by. Use 'none' to find images
            without a board.
        offset (int | Unset): The page offset Default: 0.
        limit (int | Unset): The number of images per page Default: 10.
        order_dir (SQLiteDirection | Unset):
        starred_first (bool | Unset): Whether to sort by starred images first Default: True.
        search_term (None | str | Unset): The term to search for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OffsetPaginatedResultsImageDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            image_origin=image_origin,
            categories=categories,
            is_intermediate=is_intermediate,
            board_id=board_id,
            offset=offset,
            limit=limit,
            order_dir=order_dir,
            starred_first=starred_first,
            search_term=search_term,
        )
    ).parsed
