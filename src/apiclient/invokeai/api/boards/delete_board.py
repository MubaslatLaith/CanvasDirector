from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_board_result import DeleteBoardResult
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    board_id: str,
    *,
    include_images: bool | None | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_images: bool | None | Unset
    if isinstance(include_images, Unset):
        json_include_images = UNSET
    else:
        json_include_images = include_images
    params["include_images"] = json_include_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/boards/{board_id}".format(
            board_id=quote(str(board_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteBoardResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeleteBoardResult.from_dict(response.json())

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
) -> Response[DeleteBoardResult | HTTPValidationError]:
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
    include_images: bool | None | Unset = False,
) -> Response[DeleteBoardResult | HTTPValidationError]:
    """Delete Board

     Deletes a board (user must have access to it)

    Args:
        board_id (str): The id of board to delete
        include_images (bool | None | Unset): Permanently delete all images on the board Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteBoardResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        board_id=board_id,
        include_images=include_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    board_id: str,
    *,
    client: AuthenticatedClient,
    include_images: bool | None | Unset = False,
) -> DeleteBoardResult | HTTPValidationError | None:
    """Delete Board

     Deletes a board (user must have access to it)

    Args:
        board_id (str): The id of board to delete
        include_images (bool | None | Unset): Permanently delete all images on the board Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteBoardResult | HTTPValidationError
    """

    return sync_detailed(
        board_id=board_id,
        client=client,
        include_images=include_images,
    ).parsed


async def asyncio_detailed(
    board_id: str,
    *,
    client: AuthenticatedClient,
    include_images: bool | None | Unset = False,
) -> Response[DeleteBoardResult | HTTPValidationError]:
    """Delete Board

     Deletes a board (user must have access to it)

    Args:
        board_id (str): The id of board to delete
        include_images (bool | None | Unset): Permanently delete all images on the board Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteBoardResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        board_id=board_id,
        include_images=include_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    board_id: str,
    *,
    client: AuthenticatedClient,
    include_images: bool | None | Unset = False,
) -> DeleteBoardResult | HTTPValidationError | None:
    """Delete Board

     Deletes a board (user must have access to it)

    Args:
        board_id (str): The id of board to delete
        include_images (bool | None | Unset): Permanently delete all images on the board Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteBoardResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            board_id=board_id,
            client=client,
            include_images=include_images,
        )
    ).parsed
