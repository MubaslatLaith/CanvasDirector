from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reload_custom_nodes_response_reload_custom_nodes import ReloadCustomNodesResponseReloadCustomNodes
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/custom_nodes/reload",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReloadCustomNodesResponseReloadCustomNodes | None:
    if response.status_code == 200:
        response_200 = ReloadCustomNodesResponseReloadCustomNodes.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReloadCustomNodesResponseReloadCustomNodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ReloadCustomNodesResponseReloadCustomNodes]:
    """Reload Custom Nodes

     Triggers a reload of all custom nodes.

    This re-scans the nodes directory and loads any new node packs.
    Already loaded packs are skipped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReloadCustomNodesResponseReloadCustomNodes]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ReloadCustomNodesResponseReloadCustomNodes | None:
    """Reload Custom Nodes

     Triggers a reload of all custom nodes.

    This re-scans the nodes directory and loads any new node packs.
    Already loaded packs are skipped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReloadCustomNodesResponseReloadCustomNodes
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ReloadCustomNodesResponseReloadCustomNodes]:
    """Reload Custom Nodes

     Triggers a reload of all custom nodes.

    This re-scans the nodes directory and loads any new node packs.
    Already loaded packs are skipped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReloadCustomNodesResponseReloadCustomNodes]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ReloadCustomNodesResponseReloadCustomNodes | None:
    """Reload Custom Nodes

     Triggers a reload of all custom nodes.

    This re-scans the nodes directory and loads any new node packs.
    Already loaded packs are skipped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReloadCustomNodesResponseReloadCustomNodes
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
