from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.image_category import ImageCategory
from ...models.image_names_result import ImageNamesResult
from ...models.sq_lite_direction import SQLiteDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    date: str,
    *,
    starred_first: bool | Unset = True,
    order_dir: SQLiteDirection | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    search_term: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["starred_first"] = starred_first

    json_order_dir: str | Unset = UNSET
    if not isinstance(order_dir, Unset):
        json_order_dir = order_dir.value

    params["order_dir"] = json_order_dir

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

    json_search_term: None | str | Unset
    if isinstance(search_term, Unset):
        json_search_term = UNSET
    else:
        json_search_term = search_term
    params["search_term"] = json_search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/virtual_boards/by_date/{date}/image_names".format(
            date=quote(str(date), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ImageNamesResult | None:
    if response.status_code == 200:
        response_200 = ImageNamesResult.from_dict(response.json())

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
) -> Response[HTTPValidationError | ImageNamesResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    date: str,
    *,
    client: AuthenticatedClient,
    starred_first: bool | Unset = True,
    order_dir: SQLiteDirection | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    search_term: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ImageNamesResult]:
    """List Virtual Board Image Names By Date

     Gets ordered image names for a specific date.

    Args:
        date (str): The ISO date string, e.g. '2026-03-18'
        starred_first (bool | Unset): Whether to sort starred images first Default: True.
        order_dir (SQLiteDirection | Unset):
        categories (list[ImageCategory] | None | Unset): The categories of images to include
        search_term (None | str | Unset): Search term to filter images

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ImageNamesResult]
    """

    kwargs = _get_kwargs(
        date=date,
        starred_first=starred_first,
        order_dir=order_dir,
        categories=categories,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    date: str,
    *,
    client: AuthenticatedClient,
    starred_first: bool | Unset = True,
    order_dir: SQLiteDirection | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    search_term: None | str | Unset = UNSET,
) -> HTTPValidationError | ImageNamesResult | None:
    """List Virtual Board Image Names By Date

     Gets ordered image names for a specific date.

    Args:
        date (str): The ISO date string, e.g. '2026-03-18'
        starred_first (bool | Unset): Whether to sort starred images first Default: True.
        order_dir (SQLiteDirection | Unset):
        categories (list[ImageCategory] | None | Unset): The categories of images to include
        search_term (None | str | Unset): Search term to filter images

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ImageNamesResult
    """

    return sync_detailed(
        date=date,
        client=client,
        starred_first=starred_first,
        order_dir=order_dir,
        categories=categories,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    date: str,
    *,
    client: AuthenticatedClient,
    starred_first: bool | Unset = True,
    order_dir: SQLiteDirection | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    search_term: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ImageNamesResult]:
    """List Virtual Board Image Names By Date

     Gets ordered image names for a specific date.

    Args:
        date (str): The ISO date string, e.g. '2026-03-18'
        starred_first (bool | Unset): Whether to sort starred images first Default: True.
        order_dir (SQLiteDirection | Unset):
        categories (list[ImageCategory] | None | Unset): The categories of images to include
        search_term (None | str | Unset): Search term to filter images

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ImageNamesResult]
    """

    kwargs = _get_kwargs(
        date=date,
        starred_first=starred_first,
        order_dir=order_dir,
        categories=categories,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    date: str,
    *,
    client: AuthenticatedClient,
    starred_first: bool | Unset = True,
    order_dir: SQLiteDirection | Unset = UNSET,
    categories: list[ImageCategory] | None | Unset = UNSET,
    search_term: None | str | Unset = UNSET,
) -> HTTPValidationError | ImageNamesResult | None:
    """List Virtual Board Image Names By Date

     Gets ordered image names for a specific date.

    Args:
        date (str): The ISO date string, e.g. '2026-03-18'
        starred_first (bool | Unset): Whether to sort starred images first Default: True.
        order_dir (SQLiteDirection | Unset):
        categories (list[ImageCategory] | None | Unset): The categories of images to include
        search_term (None | str | Unset): Search term to filter images

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ImageNamesResult
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
            starred_first=starred_first,
            order_dir=order_dir,
            categories=categories,
            search_term=search_term,
        )
    ).parsed
