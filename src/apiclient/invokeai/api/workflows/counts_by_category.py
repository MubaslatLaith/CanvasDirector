from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.counts_by_category_response_counts_by_category import CountsByCategoryResponseCountsByCategory
from ...models.http_validation_error import HTTPValidationError
from ...models.workflow_category import WorkflowCategory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    categories: list[WorkflowCategory],
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_categories = []
    for categories_item_data in categories:
        categories_item = categories_item_data.value
        json_categories.append(categories_item)

    params["categories"] = json_categories

    json_has_been_opened: bool | None | Unset
    if isinstance(has_been_opened, Unset):
        json_has_been_opened = UNSET
    else:
        json_has_been_opened = has_been_opened
    params["has_been_opened"] = json_has_been_opened

    json_is_public: bool | None | Unset
    if isinstance(is_public, Unset):
        json_is_public = UNSET
    else:
        json_is_public = is_public
    params["is_public"] = json_is_public

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workflows/counts_by_category",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CountsByCategoryResponseCountsByCategory | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CountsByCategoryResponseCountsByCategory.from_dict(response.json())

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
) -> Response[CountsByCategoryResponseCountsByCategory | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory],
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> Response[CountsByCategoryResponseCountsByCategory | HTTPValidationError]:
    """Counts By Category

     Counts workflows by category

    Args:
        categories (list[WorkflowCategory]): The categories to include
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CountsByCategoryResponseCountsByCategory | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        categories=categories,
        has_been_opened=has_been_opened,
        is_public=is_public,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory],
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> CountsByCategoryResponseCountsByCategory | HTTPValidationError | None:
    """Counts By Category

     Counts workflows by category

    Args:
        categories (list[WorkflowCategory]): The categories to include
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CountsByCategoryResponseCountsByCategory | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        categories=categories,
        has_been_opened=has_been_opened,
        is_public=is_public,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory],
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> Response[CountsByCategoryResponseCountsByCategory | HTTPValidationError]:
    """Counts By Category

     Counts workflows by category

    Args:
        categories (list[WorkflowCategory]): The categories to include
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CountsByCategoryResponseCountsByCategory | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        categories=categories,
        has_been_opened=has_been_opened,
        is_public=is_public,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory],
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> CountsByCategoryResponseCountsByCategory | HTTPValidationError | None:
    """Counts By Category

     Counts workflows by category

    Args:
        categories (list[WorkflowCategory]): The categories to include
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CountsByCategoryResponseCountsByCategory | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            categories=categories,
            has_been_opened=has_been_opened,
            is_public=is_public,
        )
    ).parsed
