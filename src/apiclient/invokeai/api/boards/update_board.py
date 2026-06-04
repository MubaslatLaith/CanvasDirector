from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.board_changes import BoardChanges
from ...models.board_dto import BoardDTO
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    board_id: str,
    *,
    body: BoardChanges,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/boards/{board_id}".format(
            board_id=quote(str(board_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BoardDTO | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = BoardDTO.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BoardDTO | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    board_id: str,
    *,
    client: AuthenticatedClient,
    body: BoardChanges,
) -> Response[BoardDTO | HTTPValidationError]:
    """Update Board

     Updates a board (user must have access to it)

    Args:
        board_id (str): The id of board to update
        body (BoardChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BoardDTO | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        board_id=board_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    board_id: str,
    *,
    client: AuthenticatedClient,
    body: BoardChanges,
) -> BoardDTO | HTTPValidationError | None:
    """Update Board

     Updates a board (user must have access to it)

    Args:
        board_id (str): The id of board to update
        body (BoardChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BoardDTO | HTTPValidationError
    """

    return sync_detailed(
        board_id=board_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    board_id: str,
    *,
    client: AuthenticatedClient,
    body: BoardChanges,
) -> Response[BoardDTO | HTTPValidationError]:
    """Update Board

     Updates a board (user must have access to it)

    Args:
        board_id (str): The id of board to update
        body (BoardChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BoardDTO | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        board_id=board_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    board_id: str,
    *,
    client: AuthenticatedClient,
    body: BoardChanges,
) -> BoardDTO | HTTPValidationError | None:
    """Update Board

     Updates a board (user must have access to it)

    Args:
        board_id (str): The id of board to update
        body (BoardChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BoardDTO | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            board_id=board_id,
            client=client,
            body=body,
        )
    ).parsed
