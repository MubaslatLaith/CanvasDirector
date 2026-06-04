from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.board_dto import BoardDTO
from ...models.board_record_order_by import BoardRecordOrderBy
from ...models.http_validation_error import HTTPValidationError
from ...models.offset_paginated_results_board_dto import OffsetPaginatedResultsBoardDTO
from ...models.sq_lite_direction import SQLiteDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_by: BoardRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    all_: bool | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    include_archived: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    json_all_: bool | None | Unset
    if isinstance(all_, Unset):
        json_all_ = UNSET
    else:
        json_all_ = all_
    params["all"] = json_all_

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params["include_archived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/boards/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> list[BoardDTO] | OffsetPaginatedResultsBoardDTO:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = OffsetPaginatedResultsBoardDTO.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = []
            _response_200_type_1 = data
            for response_200_type_1_item_data in _response_200_type_1:
                response_200_type_1_item = BoardDTO.from_dict(response_200_type_1_item_data)

                response_200_type_1.append(response_200_type_1_item)

            return response_200_type_1

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
) -> Response[HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    order_by: BoardRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    all_: bool | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    include_archived: bool | Unset = False,
) -> Response[HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO]:
    """List Boards

     Gets a list of boards for the current user, including shared boards. Admin users see all boards.

    Args:
        order_by (BoardRecordOrderBy | Unset): The order by options for board records
        direction (SQLiteDirection | Unset):
        all_ (bool | None | Unset): Whether to list all boards
        offset (int | None | Unset): The page offset
        limit (int | None | Unset): The number of boards per page
        include_archived (bool | Unset): Whether or not to include archived boards in list
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        direction=direction,
        all_=all_,
        offset=offset,
        limit=limit,
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    order_by: BoardRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    all_: bool | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    include_archived: bool | Unset = False,
) -> HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO | None:
    """List Boards

     Gets a list of boards for the current user, including shared boards. Admin users see all boards.

    Args:
        order_by (BoardRecordOrderBy | Unset): The order by options for board records
        direction (SQLiteDirection | Unset):
        all_ (bool | None | Unset): Whether to list all boards
        offset (int | None | Unset): The page offset
        limit (int | None | Unset): The number of boards per page
        include_archived (bool | Unset): Whether or not to include archived boards in list
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO
    """

    return sync_detailed(
        client=client,
        order_by=order_by,
        direction=direction,
        all_=all_,
        offset=offset,
        limit=limit,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    order_by: BoardRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    all_: bool | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    include_archived: bool | Unset = False,
) -> Response[HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO]:
    """List Boards

     Gets a list of boards for the current user, including shared boards. Admin users see all boards.

    Args:
        order_by (BoardRecordOrderBy | Unset): The order by options for board records
        direction (SQLiteDirection | Unset):
        all_ (bool | None | Unset): Whether to list all boards
        offset (int | None | Unset): The page offset
        limit (int | None | Unset): The number of boards per page
        include_archived (bool | Unset): Whether or not to include archived boards in list
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        direction=direction,
        all_=all_,
        offset=offset,
        limit=limit,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    order_by: BoardRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
    all_: bool | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    include_archived: bool | Unset = False,
) -> HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO | None:
    """List Boards

     Gets a list of boards for the current user, including shared boards. Admin users see all boards.

    Args:
        order_by (BoardRecordOrderBy | Unset): The order by options for board records
        direction (SQLiteDirection | Unset):
        all_ (bool | None | Unset): Whether to list all boards
        offset (int | None | Unset): The page offset
        limit (int | None | Unset): The number of boards per page
        include_archived (bool | Unset): Whether or not to include archived boards in list
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[BoardDTO] | OffsetPaginatedResultsBoardDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            order_by=order_by,
            direction=direction,
            all_=all_,
            offset=offset,
            limit=limit,
            include_archived=include_archived,
        )
    ).parsed
