from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.hugging_face_models import HuggingFaceModels
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hugging_face_repo: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["hugging_face_repo"] = hugging_face_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/models/hugging_face",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | HuggingFaceModels | None:
    if response.status_code == 200:
        response_200 = HuggingFaceModels.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | HuggingFaceModels]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    hugging_face_repo: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | HuggingFaceModels]:
    """Get Hugging Face Models

    Args:
        hugging_face_repo (str | Unset): Hugging face repo to search for models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | HuggingFaceModels]
    """

    kwargs = _get_kwargs(
        hugging_face_repo=hugging_face_repo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    hugging_face_repo: str | Unset = UNSET,
) -> Any | HTTPValidationError | HuggingFaceModels | None:
    """Get Hugging Face Models

    Args:
        hugging_face_repo (str | Unset): Hugging face repo to search for models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | HuggingFaceModels
    """

    return sync_detailed(
        client=client,
        hugging_face_repo=hugging_face_repo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    hugging_face_repo: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | HuggingFaceModels]:
    """Get Hugging Face Models

    Args:
        hugging_face_repo (str | Unset): Hugging face repo to search for models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | HuggingFaceModels]
    """

    kwargs = _get_kwargs(
        hugging_face_repo=hugging_face_repo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    hugging_face_repo: str | Unset = UNSET,
) -> Any | HTTPValidationError | HuggingFaceModels | None:
    """Get Hugging Face Models

    Args:
        hugging_face_repo (str | Unset): Hugging face repo to search for models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | HuggingFaceModels
    """

    return (
        await asyncio_detailed(
            client=client,
            hugging_face_repo=hugging_face_repo,
        )
    ).parsed
