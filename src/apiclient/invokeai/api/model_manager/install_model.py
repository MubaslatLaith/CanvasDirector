from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.model_install_job import ModelInstallJob
from ...models.model_record_changes import ModelRecordChanges
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ModelRecordChanges,
    source: str,
    inplace: bool | None | Unset = False,
    access_token: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["source"] = source

    json_inplace: bool | None | Unset
    if isinstance(inplace, Unset):
        json_inplace = UNSET
    else:
        json_inplace = inplace
    params["inplace"] = json_inplace

    json_access_token: None | str | Unset
    if isinstance(access_token, Unset):
        json_access_token = UNSET
    else:
        json_access_token = access_token
    params["access_token"] = json_access_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/models/install",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | ModelInstallJob | None:
    if response.status_code == 201:
        response_201 = ModelInstallJob.from_dict(response.json())

        return response_201

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 415:
        response_415 = cast(Any, None)
        return response_415

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = cast(Any, None)
        return response_424

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | ModelInstallJob]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelRecordChanges,
    source: str,
    inplace: bool | None | Unset = False,
    access_token: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | ModelInstallJob]:
    r"""Install Model

     Install a model using a string identifier.

    `source` can be any of the following.

    1. A path on the local filesystem ('C:\users\fred\model.safetensors')
    2. A Url pointing to a single downloadable model file
    3. A HuggingFace repo_id with any of the following formats:
       - model/name
       - model/name:fp16:vae
       - model/name::vae          -- use default precision
       - model/name:fp16:path/to/model.safetensors
       - model/name::path/to/model.safetensors

    `config` is a ModelRecordChanges object. Fields in this object will override
    the ones that are probed automatically. Pass an empty object to accept
    all the defaults.

    `access_token` is an optional access token for use with Urls that require
    authentication.

    Models will be downloaded, probed, configured and installed in a
    series of background threads. The return object has `status` attribute
    that can be used to monitor progress.

    See the documentation for `import_model_record` for more information on
    interpreting the job information returned by this route.

    Args:
        source (str): Model source to install, can be a local path, repo_id, or remote URL
        inplace (bool | None | Unset): Whether or not to install a local model in place Default:
            False.
        access_token (None | str | Unset): access token for the remote resource
        body (ModelRecordChanges): A set of changes to apply to a model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ModelInstallJob]
    """

    kwargs = _get_kwargs(
        body=body,
        source=source,
        inplace=inplace,
        access_token=access_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ModelRecordChanges,
    source: str,
    inplace: bool | None | Unset = False,
    access_token: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | ModelInstallJob | None:
    r"""Install Model

     Install a model using a string identifier.

    `source` can be any of the following.

    1. A path on the local filesystem ('C:\users\fred\model.safetensors')
    2. A Url pointing to a single downloadable model file
    3. A HuggingFace repo_id with any of the following formats:
       - model/name
       - model/name:fp16:vae
       - model/name::vae          -- use default precision
       - model/name:fp16:path/to/model.safetensors
       - model/name::path/to/model.safetensors

    `config` is a ModelRecordChanges object. Fields in this object will override
    the ones that are probed automatically. Pass an empty object to accept
    all the defaults.

    `access_token` is an optional access token for use with Urls that require
    authentication.

    Models will be downloaded, probed, configured and installed in a
    series of background threads. The return object has `status` attribute
    that can be used to monitor progress.

    See the documentation for `import_model_record` for more information on
    interpreting the job information returned by this route.

    Args:
        source (str): Model source to install, can be a local path, repo_id, or remote URL
        inplace (bool | None | Unset): Whether or not to install a local model in place Default:
            False.
        access_token (None | str | Unset): access token for the remote resource
        body (ModelRecordChanges): A set of changes to apply to a model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ModelInstallJob
    """

    return sync_detailed(
        client=client,
        body=body,
        source=source,
        inplace=inplace,
        access_token=access_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelRecordChanges,
    source: str,
    inplace: bool | None | Unset = False,
    access_token: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | ModelInstallJob]:
    r"""Install Model

     Install a model using a string identifier.

    `source` can be any of the following.

    1. A path on the local filesystem ('C:\users\fred\model.safetensors')
    2. A Url pointing to a single downloadable model file
    3. A HuggingFace repo_id with any of the following formats:
       - model/name
       - model/name:fp16:vae
       - model/name::vae          -- use default precision
       - model/name:fp16:path/to/model.safetensors
       - model/name::path/to/model.safetensors

    `config` is a ModelRecordChanges object. Fields in this object will override
    the ones that are probed automatically. Pass an empty object to accept
    all the defaults.

    `access_token` is an optional access token for use with Urls that require
    authentication.

    Models will be downloaded, probed, configured and installed in a
    series of background threads. The return object has `status` attribute
    that can be used to monitor progress.

    See the documentation for `import_model_record` for more information on
    interpreting the job information returned by this route.

    Args:
        source (str): Model source to install, can be a local path, repo_id, or remote URL
        inplace (bool | None | Unset): Whether or not to install a local model in place Default:
            False.
        access_token (None | str | Unset): access token for the remote resource
        body (ModelRecordChanges): A set of changes to apply to a model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ModelInstallJob]
    """

    kwargs = _get_kwargs(
        body=body,
        source=source,
        inplace=inplace,
        access_token=access_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModelRecordChanges,
    source: str,
    inplace: bool | None | Unset = False,
    access_token: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | ModelInstallJob | None:
    r"""Install Model

     Install a model using a string identifier.

    `source` can be any of the following.

    1. A path on the local filesystem ('C:\users\fred\model.safetensors')
    2. A Url pointing to a single downloadable model file
    3. A HuggingFace repo_id with any of the following formats:
       - model/name
       - model/name:fp16:vae
       - model/name::vae          -- use default precision
       - model/name:fp16:path/to/model.safetensors
       - model/name::path/to/model.safetensors

    `config` is a ModelRecordChanges object. Fields in this object will override
    the ones that are probed automatically. Pass an empty object to accept
    all the defaults.

    `access_token` is an optional access token for use with Urls that require
    authentication.

    Models will be downloaded, probed, configured and installed in a
    series of background threads. The return object has `status` attribute
    that can be used to monitor progress.

    See the documentation for `import_model_record` for more information on
    interpreting the job information returned by this route.

    Args:
        source (str): Model source to install, can be a local path, repo_id, or remote URL
        inplace (bool | None | Unset): Whether or not to install a local model in place Default:
            False.
        access_token (None | str | Unset): access token for the remote resource
        body (ModelRecordChanges): A set of changes to apply to a model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ModelInstallJob
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            source=source,
            inplace=inplace,
            access_token=access_token,
        )
    ).parsed
