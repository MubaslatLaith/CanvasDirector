from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_install_job import ModelInstallJob
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/models/install",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[ModelInstallJob] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelInstallJob.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ModelInstallJob]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[ModelInstallJob]]:
    r"""List Model Installs

     Return the list of model install jobs.

    Install jobs have a numeric `id`, a `status`, and other fields that provide information on
    the nature of the job and its progress. The `status` is one of:

    * \"waiting\" -- Job is waiting in the queue to run
    * \"downloading\" -- Model file(s) are downloading
    * \"running\" -- Model has downloaded and the model probing and registration process is running
    * \"paused\" -- Job is paused and can be resumed
    * \"completed\" -- Installation completed successfully
    * \"error\" -- An error occurred. Details will be in the \"error_type\" and \"error\" fields.
    * \"cancelled\" -- Job was cancelled before completion.

    Once completed, information about the model such as its size, base
    model and type can be retrieved from the `config_out` field. For multi-file models such as
    diffusers,
    information on individual files can be retrieved from `download_parts`.

    See the example and schema below for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ModelInstallJob]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> list[ModelInstallJob] | None:
    r"""List Model Installs

     Return the list of model install jobs.

    Install jobs have a numeric `id`, a `status`, and other fields that provide information on
    the nature of the job and its progress. The `status` is one of:

    * \"waiting\" -- Job is waiting in the queue to run
    * \"downloading\" -- Model file(s) are downloading
    * \"running\" -- Model has downloaded and the model probing and registration process is running
    * \"paused\" -- Job is paused and can be resumed
    * \"completed\" -- Installation completed successfully
    * \"error\" -- An error occurred. Details will be in the \"error_type\" and \"error\" fields.
    * \"cancelled\" -- Job was cancelled before completion.

    Once completed, information about the model such as its size, base
    model and type can be retrieved from the `config_out` field. For multi-file models such as
    diffusers,
    information on individual files can be retrieved from `download_parts`.

    See the example and schema below for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ModelInstallJob]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[ModelInstallJob]]:
    r"""List Model Installs

     Return the list of model install jobs.

    Install jobs have a numeric `id`, a `status`, and other fields that provide information on
    the nature of the job and its progress. The `status` is one of:

    * \"waiting\" -- Job is waiting in the queue to run
    * \"downloading\" -- Model file(s) are downloading
    * \"running\" -- Model has downloaded and the model probing and registration process is running
    * \"paused\" -- Job is paused and can be resumed
    * \"completed\" -- Installation completed successfully
    * \"error\" -- An error occurred. Details will be in the \"error_type\" and \"error\" fields.
    * \"cancelled\" -- Job was cancelled before completion.

    Once completed, information about the model such as its size, base
    model and type can be retrieved from the `config_out` field. For multi-file models such as
    diffusers,
    information on individual files can be retrieved from `download_parts`.

    See the example and schema below for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ModelInstallJob]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> list[ModelInstallJob] | None:
    r"""List Model Installs

     Return the list of model install jobs.

    Install jobs have a numeric `id`, a `status`, and other fields that provide information on
    the nature of the job and its progress. The `status` is one of:

    * \"waiting\" -- Job is waiting in the queue to run
    * \"downloading\" -- Model file(s) are downloading
    * \"running\" -- Model has downloaded and the model probing and registration process is running
    * \"paused\" -- Job is paused and can be resumed
    * \"completed\" -- Installation completed successfully
    * \"error\" -- An error occurred. Details will be in the \"error_type\" and \"error\" fields.
    * \"cancelled\" -- Job was cancelled before completion.

    Once completed, information about the model such as its size, base
    model and type can be retrieved from the `config_out` field. For multi-file models such as
    diffusers,
    information on individual files can be retrieved from `download_parts`.

    See the example and schema below for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ModelInstallJob]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
