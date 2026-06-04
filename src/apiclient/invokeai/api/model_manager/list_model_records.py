from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_model_type import BaseModelType
from ...models.http_validation_error import HTTPValidationError
from ...models.model_format import ModelFormat
from ...models.model_record_order_by import ModelRecordOrderBy
from ...models.model_type import ModelType
from ...models.models_list import ModelsList
from ...models.sq_lite_direction import SQLiteDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    base_models: list[BaseModelType] | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_name: None | str | Unset = UNSET,
    model_format: ModelFormat | None | Unset = UNSET,
    order_by: ModelRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_base_models: list[str] | None | Unset
    if isinstance(base_models, Unset):
        json_base_models = UNSET
    elif isinstance(base_models, list):
        json_base_models = []
        for base_models_type_0_item_data in base_models:
            base_models_type_0_item = base_models_type_0_item_data.value
            json_base_models.append(base_models_type_0_item)

    else:
        json_base_models = base_models
    params["base_models"] = json_base_models

    json_model_type: None | str | Unset
    if isinstance(model_type, Unset):
        json_model_type = UNSET
    elif isinstance(model_type, ModelType):
        json_model_type = model_type.value
    else:
        json_model_type = model_type
    params["model_type"] = json_model_type

    json_model_name: None | str | Unset
    if isinstance(model_name, Unset):
        json_model_name = UNSET
    else:
        json_model_name = model_name
    params["model_name"] = json_model_name

    json_model_format: None | str | Unset
    if isinstance(model_format, Unset):
        json_model_format = UNSET
    elif isinstance(model_format, ModelFormat):
        json_model_format = model_format.value
    else:
        json_model_format = model_format
    params["model_format"] = json_model_format

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/models/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ModelsList | None:
    if response.status_code == 200:
        response_200 = ModelsList.from_dict(response.json())

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
) -> Response[HTTPValidationError | ModelsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_models: list[BaseModelType] | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_name: None | str | Unset = UNSET,
    model_format: ModelFormat | None | Unset = UNSET,
    order_by: ModelRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
) -> Response[HTTPValidationError | ModelsList]:
    """List Model Records

     Get a list of models.

    Args:
        base_models (list[BaseModelType] | None | Unset): Base models to include
        model_type (ModelType | None | Unset): The type of model to get
        model_name (None | str | Unset): Exact match on the name of the model
        model_format (ModelFormat | None | Unset): Exact match on the format of the model (e.g.
            'diffusers')
        order_by (ModelRecordOrderBy | Unset): The order in which to return model summaries.
        direction (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ModelsList]
    """

    kwargs = _get_kwargs(
        base_models=base_models,
        model_type=model_type,
        model_name=model_name,
        model_format=model_format,
        order_by=order_by,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    base_models: list[BaseModelType] | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_name: None | str | Unset = UNSET,
    model_format: ModelFormat | None | Unset = UNSET,
    order_by: ModelRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
) -> HTTPValidationError | ModelsList | None:
    """List Model Records

     Get a list of models.

    Args:
        base_models (list[BaseModelType] | None | Unset): Base models to include
        model_type (ModelType | None | Unset): The type of model to get
        model_name (None | str | Unset): Exact match on the name of the model
        model_format (ModelFormat | None | Unset): Exact match on the format of the model (e.g.
            'diffusers')
        order_by (ModelRecordOrderBy | Unset): The order in which to return model summaries.
        direction (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ModelsList
    """

    return sync_detailed(
        client=client,
        base_models=base_models,
        model_type=model_type,
        model_name=model_name,
        model_format=model_format,
        order_by=order_by,
        direction=direction,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_models: list[BaseModelType] | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_name: None | str | Unset = UNSET,
    model_format: ModelFormat | None | Unset = UNSET,
    order_by: ModelRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
) -> Response[HTTPValidationError | ModelsList]:
    """List Model Records

     Get a list of models.

    Args:
        base_models (list[BaseModelType] | None | Unset): Base models to include
        model_type (ModelType | None | Unset): The type of model to get
        model_name (None | str | Unset): Exact match on the name of the model
        model_format (ModelFormat | None | Unset): Exact match on the format of the model (e.g.
            'diffusers')
        order_by (ModelRecordOrderBy | Unset): The order in which to return model summaries.
        direction (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ModelsList]
    """

    kwargs = _get_kwargs(
        base_models=base_models,
        model_type=model_type,
        model_name=model_name,
        model_format=model_format,
        order_by=order_by,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    base_models: list[BaseModelType] | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_name: None | str | Unset = UNSET,
    model_format: ModelFormat | None | Unset = UNSET,
    order_by: ModelRecordOrderBy | Unset = UNSET,
    direction: SQLiteDirection | Unset = UNSET,
) -> HTTPValidationError | ModelsList | None:
    """List Model Records

     Get a list of models.

    Args:
        base_models (list[BaseModelType] | None | Unset): Base models to include
        model_type (ModelType | None | Unset): The type of model to get
        model_name (None | str | Unset): Exact match on the name of the model
        model_format (ModelFormat | None | Unset): Exact match on the format of the model (e.g.
            'diffusers')
        order_by (ModelRecordOrderBy | Unset): The order in which to return model summaries.
        direction (SQLiteDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ModelsList
    """

    return (
        await asyncio_detailed(
            client=client,
            base_models=base_models,
            model_type=model_type,
            model_name=model_name,
            model_format=model_format,
            order_by=order_by,
            direction=direction,
        )
    ).parsed
