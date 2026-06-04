from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.recall_parameter import RecallParameter
from ...models.update_recall_parameters_response_update_recall_parameters import (
    UpdateRecallParametersResponseUpdateRecallParameters,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    *,
    body: RecallParameter,
    strict: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["strict"] = strict

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/recall/{queue_id}".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters | None:
    if response.status_code == 200:
        response_200 = UpdateRecallParametersResponseUpdateRecallParameters.from_dict(response.json())

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
) -> Response[HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: RecallParameter,
    strict: bool | Unset = False,
) -> Response[HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters]:
    r"""Update Recall Parameters

     Update recallable parameters that can be recalled on the frontend.

    This endpoint allows updating parameters such as prompt, model, steps, and other
    generation settings. These parameters are stored in client state and can be
    accessed by the frontend to populate UI elements.

    Args:
        queue_id: The queue ID to associate these parameters with
        parameters: The RecallParameter object containing the parameters to update
        strict: When true, parameters not included in the request body are reset
            to their defaults (cleared on the frontend).  Defaults to false,
            which preserves the existing behaviour of only updating the
            parameters that are explicitly provided.

    Returns:
        A dictionary containing the updated parameters and status

    Example:
        POST /api/v1/recall/{queue_id}?strict=true
        {
            \"positive_prompt\": \"a beautiful landscape\",
            \"model\": \"sd-1.5\",
            \"steps\": 20
        }
        # In strict mode, all other parameters (reference_images, loras, etc.)
        # are cleared.  In non-strict mode (default) they would be left as-is.

    Args:
        queue_id (str): The queue id to perform this operation on
        strict (bool | Unset): When true, parameters not included in the request are reset to
            their defaults (cleared). Default: False.
        body (RecallParameter): Request model for updating recallable parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
        strict=strict,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: RecallParameter,
    strict: bool | Unset = False,
) -> HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters | None:
    r"""Update Recall Parameters

     Update recallable parameters that can be recalled on the frontend.

    This endpoint allows updating parameters such as prompt, model, steps, and other
    generation settings. These parameters are stored in client state and can be
    accessed by the frontend to populate UI elements.

    Args:
        queue_id: The queue ID to associate these parameters with
        parameters: The RecallParameter object containing the parameters to update
        strict: When true, parameters not included in the request body are reset
            to their defaults (cleared on the frontend).  Defaults to false,
            which preserves the existing behaviour of only updating the
            parameters that are explicitly provided.

    Returns:
        A dictionary containing the updated parameters and status

    Example:
        POST /api/v1/recall/{queue_id}?strict=true
        {
            \"positive_prompt\": \"a beautiful landscape\",
            \"model\": \"sd-1.5\",
            \"steps\": 20
        }
        # In strict mode, all other parameters (reference_images, loras, etc.)
        # are cleared.  In non-strict mode (default) they would be left as-is.

    Args:
        queue_id (str): The queue id to perform this operation on
        strict (bool | Unset): When true, parameters not included in the request are reset to
            their defaults (cleared). Default: False.
        body (RecallParameter): Request model for updating recallable parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        body=body,
        strict=strict,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: RecallParameter,
    strict: bool | Unset = False,
) -> Response[HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters]:
    r"""Update Recall Parameters

     Update recallable parameters that can be recalled on the frontend.

    This endpoint allows updating parameters such as prompt, model, steps, and other
    generation settings. These parameters are stored in client state and can be
    accessed by the frontend to populate UI elements.

    Args:
        queue_id: The queue ID to associate these parameters with
        parameters: The RecallParameter object containing the parameters to update
        strict: When true, parameters not included in the request body are reset
            to their defaults (cleared on the frontend).  Defaults to false,
            which preserves the existing behaviour of only updating the
            parameters that are explicitly provided.

    Returns:
        A dictionary containing the updated parameters and status

    Example:
        POST /api/v1/recall/{queue_id}?strict=true
        {
            \"positive_prompt\": \"a beautiful landscape\",
            \"model\": \"sd-1.5\",
            \"steps\": 20
        }
        # In strict mode, all other parameters (reference_images, loras, etc.)
        # are cleared.  In non-strict mode (default) they would be left as-is.

    Args:
        queue_id (str): The queue id to perform this operation on
        strict (bool | Unset): When true, parameters not included in the request are reset to
            their defaults (cleared). Default: False.
        body (RecallParameter): Request model for updating recallable parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        body=body,
        strict=strict,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: RecallParameter,
    strict: bool | Unset = False,
) -> HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters | None:
    r"""Update Recall Parameters

     Update recallable parameters that can be recalled on the frontend.

    This endpoint allows updating parameters such as prompt, model, steps, and other
    generation settings. These parameters are stored in client state and can be
    accessed by the frontend to populate UI elements.

    Args:
        queue_id: The queue ID to associate these parameters with
        parameters: The RecallParameter object containing the parameters to update
        strict: When true, parameters not included in the request body are reset
            to their defaults (cleared on the frontend).  Defaults to false,
            which preserves the existing behaviour of only updating the
            parameters that are explicitly provided.

    Returns:
        A dictionary containing the updated parameters and status

    Example:
        POST /api/v1/recall/{queue_id}?strict=true
        {
            \"positive_prompt\": \"a beautiful landscape\",
            \"model\": \"sd-1.5\",
            \"steps\": 20
        }
        # In strict mode, all other parameters (reference_images, loras, etc.)
        # are cleared.  In non-strict mode (default) they would be left as-is.

    Args:
        queue_id (str): The queue id to perform this operation on
        strict (bool | Unset): When true, parameters not included in the request are reset to
            their defaults (cleared). Default: False.
        body (RecallParameter): Request model for updating recallable parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateRecallParametersResponseUpdateRecallParameters
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            body=body,
            strict=strict,
        )
    ).parsed
