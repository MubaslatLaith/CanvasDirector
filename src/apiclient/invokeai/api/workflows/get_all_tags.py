from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.workflow_category import WorkflowCategory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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

    json_is_public: bool | None | Unset
    if isinstance(is_public, Unset):
        json_is_public = UNSET
    else:
        json_is_public = is_public
    params["is_public"] = json_is_public

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workflows/tags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[str] | None:
    if response.status_code == 200:
        response_200 = cast(list[str], response.json())

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
) -> Response[HTTPValidationError | list[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[str]]:
    """Get All Tags

     Gets all unique tags from workflows

    Args:
        categories (list[WorkflowCategory] | None | Unset): The categories to include
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[str]]
    """

    kwargs = _get_kwargs(
        categories=categories,
        is_public=is_public,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> HTTPValidationError | list[str] | None:
    """Get All Tags

     Gets all unique tags from workflows

    Args:
        categories (list[WorkflowCategory] | None | Unset): The categories to include
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[str]
    """

    return sync_detailed(
        client=client,
        categories=categories,
        is_public=is_public,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[str]]:
    """Get All Tags

     Gets all unique tags from workflows

    Args:
        categories (list[WorkflowCategory] | None | Unset): The categories to include
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[str]]
    """

    kwargs = _get_kwargs(
        categories=categories,
        is_public=is_public,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> HTTPValidationError | list[str] | None:
    """Get All Tags

     Gets all unique tags from workflows

    Args:
        categories (list[WorkflowCategory] | None | Unset): The categories to include
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[str]
    """

    return (
        await asyncio_detailed(
            client=client,
            categories=categories,
            is_public=is_public,
        )
    ).parsed
