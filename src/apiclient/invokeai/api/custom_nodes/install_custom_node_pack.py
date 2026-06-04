from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.install_node_pack_request import InstallNodePackRequest
from ...models.install_node_pack_response import InstallNodePackResponse
from ...types import Response


def _get_kwargs(
    *,
    body: InstallNodePackRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/custom_nodes/install",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InstallNodePackResponse | None:
    if response.status_code == 200:
        response_200 = InstallNodePackResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | InstallNodePackResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InstallNodePackRequest,
) -> Response[HTTPValidationError | InstallNodePackResponse]:
    """Install Custom Node Pack

     Installs a custom node pack from a git URL by cloning it into the nodes directory.

    Args:
        body (InstallNodePackRequest): Request to install a node pack from a git URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InstallNodePackResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InstallNodePackRequest,
) -> HTTPValidationError | InstallNodePackResponse | None:
    """Install Custom Node Pack

     Installs a custom node pack from a git URL by cloning it into the nodes directory.

    Args:
        body (InstallNodePackRequest): Request to install a node pack from a git URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InstallNodePackResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InstallNodePackRequest,
) -> Response[HTTPValidationError | InstallNodePackResponse]:
    """Install Custom Node Pack

     Installs a custom node pack from a git URL by cloning it into the nodes directory.

    Args:
        body (InstallNodePackRequest): Request to install a node pack from a git URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InstallNodePackResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InstallNodePackRequest,
) -> HTTPValidationError | InstallNodePackResponse | None:
    """Install Custom Node Pack

     Installs a custom node pack from a git URL by cloning it into the nodes directory.

    Args:
        body (InstallNodePackRequest): Request to install a node pack from a git URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InstallNodePackResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
