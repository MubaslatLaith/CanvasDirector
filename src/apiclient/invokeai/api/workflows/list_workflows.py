from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paginated_results_workflow_record_list_item_with_thumbnail_dto import (
    PaginatedResultsWorkflowRecordListItemWithThumbnailDTO,
)
from ...models.sq_lite_direction import SQLiteDirection
from ...models.workflow_category import WorkflowCategory
from ...models.workflow_record_order_by import WorkflowRecordOrderBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    per_page: int | None | Unset = UNSET,
    order_by: WorkflowRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    json_per_page: int | None | Unset
    if isinstance(per_page, Unset):
        json_per_page = UNSET
    else:
        json_per_page = per_page
    params["per_page"] = json_per_page

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

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

    json_tags: list[str] | None | Unset
    if isinstance(tags, Unset):
        json_tags = UNSET
    elif isinstance(tags, list):
        json_tags = tags

    else:
        json_tags = tags
    params["tags"] = json_tags

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

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
        "url": "/api/v1/workflows/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO | None:
    if response.status_code == 200:
        response_200 = PaginatedResultsWorkflowRecordListItemWithThumbnailDTO.from_dict(response.json())

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
) -> Response[HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    per_page: int | None | Unset = UNSET,
    order_by: WorkflowRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO]:
    """List Workflows

     Gets a page of workflows

    Args:
        page (int | Unset): The page to get Default: 0.
        per_page (int | None | Unset): The number of workflows per page
        order_by (WorkflowRecordOrderBy | Unset): The order by options for workflow records
        direction (SQLiteDirection | Unset):
        categories (list[WorkflowCategory] | None | Unset): The categories of workflow to get
        tags (list[str] | None | Unset): The tags of workflow to get
        query (None | str | Unset): The text to query by (matches name and description)
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        order_by=order_by,
        direction=direction,
        categories=categories,
        tags=tags,
        query=query,
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
    page: int | Unset = 0,
    per_page: int | None | Unset = UNSET,
    order_by: WorkflowRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO | None:
    """List Workflows

     Gets a page of workflows

    Args:
        page (int | Unset): The page to get Default: 0.
        per_page (int | None | Unset): The number of workflows per page
        order_by (WorkflowRecordOrderBy | Unset): The order by options for workflow records
        direction (SQLiteDirection | Unset):
        categories (list[WorkflowCategory] | None | Unset): The categories of workflow to get
        tags (list[str] | None | Unset): The tags of workflow to get
        query (None | str | Unset): The text to query by (matches name and description)
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        order_by=order_by,
        direction=direction,
        categories=categories,
        tags=tags,
        query=query,
        has_been_opened=has_been_opened,
        is_public=is_public,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    per_page: int | None | Unset = UNSET,
    order_by: WorkflowRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO]:
    """List Workflows

     Gets a page of workflows

    Args:
        page (int | Unset): The page to get Default: 0.
        per_page (int | None | Unset): The number of workflows per page
        order_by (WorkflowRecordOrderBy | Unset): The order by options for workflow records
        direction (SQLiteDirection | Unset):
        categories (list[WorkflowCategory] | None | Unset): The categories of workflow to get
        tags (list[str] | None | Unset): The tags of workflow to get
        query (None | str | Unset): The text to query by (matches name and description)
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        order_by=order_by,
        direction=direction,
        categories=categories,
        tags=tags,
        query=query,
        has_been_opened=has_been_opened,
        is_public=is_public,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    per_page: int | None | Unset = UNSET,
    order_by: WorkflowRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    categories: list[WorkflowCategory] | None | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    has_been_opened: bool | None | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
) -> HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO | None:
    """List Workflows

     Gets a page of workflows

    Args:
        page (int | Unset): The page to get Default: 0.
        per_page (int | None | Unset): The number of workflows per page
        order_by (WorkflowRecordOrderBy | Unset): The order by options for workflow records
        direction (SQLiteDirection | Unset):
        categories (list[WorkflowCategory] | None | Unset): The categories of workflow to get
        tags (list[str] | None | Unset): The tags of workflow to get
        query (None | str | Unset): The text to query by (matches name and description)
        has_been_opened (bool | None | Unset): Whether to include/exclude recent workflows
        is_public (bool | None | Unset): Filter by public/shared status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PaginatedResultsWorkflowRecordListItemWithThumbnailDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            order_by=order_by,
            direction=direction,
            categories=categories,
            tags=tags,
            query=query,
            has_been_opened=has_been_opened,
            is_public=is_public,
        )
    ).parsed
