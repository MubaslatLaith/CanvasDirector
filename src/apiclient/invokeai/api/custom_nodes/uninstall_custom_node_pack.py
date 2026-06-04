from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.uninstall_node_pack_response import UninstallNodePackResponse
from ...types import Response


def _get_kwargs(
    pack_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/custom_nodes/{pack_name}".format(
            pack_name=quote(str(pack_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UninstallNodePackResponse | None:
    if response.status_code == 200:
        response_200 = UninstallNodePackResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UninstallNodePackResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pack_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | UninstallNodePackResponse]:
    """Uninstall Custom Node Pack

     Uninstalls a custom node pack by removing its directory.

    Note: A restart is required for the node removal to take full effect.
    Installed nodes from the pack will remain registered until restart.

    Args:
        pack_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UninstallNodePackResponse]
    """

    kwargs = _get_kwargs(
        pack_name=pack_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pack_name: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | UninstallNodePackResponse | None:
    """Uninstall Custom Node Pack

     Uninstalls a custom node pack by removing its directory.

    Note: A restart is required for the node removal to take full effect.
    Installed nodes from the pack will remain registered until restart.

    Args:
        pack_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UninstallNodePackResponse
    """

    return sync_detailed(
        pack_name=pack_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    pack_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | UninstallNodePackResponse]:
    """Uninstall Custom Node Pack

     Uninstalls a custom node pack by removing its directory.

    Note: A restart is required for the node removal to take full effect.
    Installed nodes from the pack will remain registered until restart.

    Args:
        pack_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UninstallNodePackResponse]
    """

    kwargs = _get_kwargs(
        pack_name=pack_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pack_name: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | UninstallNodePackResponse | None:
    """Uninstall Custom Node Pack

     Uninstalls a custom node pack by removing its directory.

    Note: A restart is required for the node removal to take full effect.
    Installed nodes from the pack will remain registered until restart.

    Args:
        pack_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UninstallNodePackResponse
    """

    return (
        await asyncio_detailed(
            pack_name=pack_name,
            client=client,
        )
    ).parsed
