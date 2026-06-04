from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_style_preset import BodyUpdateStylePreset
from ...models.http_validation_error import HTTPValidationError
from ...models.style_preset_record_with_image import StylePresetRecordWithImage
from ...types import Response


def _get_kwargs(
    style_preset_id: str,
    *,
    body: BodyUpdateStylePreset,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/style_presets/i/{style_preset_id}".format(
            style_preset_id=quote(str(style_preset_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | StylePresetRecordWithImage | None:
    if response.status_code == 200:
        response_200 = StylePresetRecordWithImage.from_dict(response.json())

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
) -> Response[HTTPValidationError | StylePresetRecordWithImage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    style_preset_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateStylePreset,
) -> Response[HTTPValidationError | StylePresetRecordWithImage]:
    """Update Style Preset

     Updates a style preset

    Args:
        style_preset_id (str): The id of the style preset to update
        body (BodyUpdateStylePreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StylePresetRecordWithImage]
    """

    kwargs = _get_kwargs(
        style_preset_id=style_preset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    style_preset_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateStylePreset,
) -> HTTPValidationError | StylePresetRecordWithImage | None:
    """Update Style Preset

     Updates a style preset

    Args:
        style_preset_id (str): The id of the style preset to update
        body (BodyUpdateStylePreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StylePresetRecordWithImage
    """

    return sync_detailed(
        style_preset_id=style_preset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    style_preset_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateStylePreset,
) -> Response[HTTPValidationError | StylePresetRecordWithImage]:
    """Update Style Preset

     Updates a style preset

    Args:
        style_preset_id (str): The id of the style preset to update
        body (BodyUpdateStylePreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StylePresetRecordWithImage]
    """

    kwargs = _get_kwargs(
        style_preset_id=style_preset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    style_preset_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateStylePreset,
) -> HTTPValidationError | StylePresetRecordWithImage | None:
    """Update Style Preset

     Updates a style preset

    Args:
        style_preset_id (str): The id of the style preset to update
        body (BodyUpdateStylePreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StylePresetRecordWithImage
    """

    return (
        await asyncio_detailed(
            style_preset_id=style_preset_id,
            client=client,
            body=body,
        )
    ).parsed
