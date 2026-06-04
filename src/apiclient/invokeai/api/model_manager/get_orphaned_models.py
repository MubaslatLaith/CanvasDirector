from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.orphaned_model_info import OrphanedModelInfo
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/models/sync/orphaned",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[OrphanedModelInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OrphanedModelInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[OrphanedModelInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[OrphanedModelInfo]]:
    """Get Orphaned Models

     Find orphaned model directories.

    Orphaned models are directories in the models folder that contain model files
    but are not referenced in the database. This can happen when models are deleted
    from the database but the files remain on disk.

    Returns:
        List of orphaned model directory information

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OrphanedModelInfo]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> list[OrphanedModelInfo] | None:
    """Get Orphaned Models

     Find orphaned model directories.

    Orphaned models are directories in the models folder that contain model files
    but are not referenced in the database. This can happen when models are deleted
    from the database but the files remain on disk.

    Returns:
        List of orphaned model directory information

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OrphanedModelInfo]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[OrphanedModelInfo]]:
    """Get Orphaned Models

     Find orphaned model directories.

    Orphaned models are directories in the models folder that contain model files
    but are not referenced in the database. This can happen when models are deleted
    from the database but the files remain on disk.

    Returns:
        List of orphaned model directory information

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OrphanedModelInfo]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> list[OrphanedModelInfo] | None:
    """Get Orphaned Models

     Find orphaned model directories.

    Orphaned models are directories in the models folder that contain model files
    but are not referenced in the database. This can happen when models are deleted
    from the database but the files remain on disk.

    Returns:
        List of orphaned model directory information

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OrphanedModelInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
