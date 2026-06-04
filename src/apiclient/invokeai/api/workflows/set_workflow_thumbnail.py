from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_set_workflow_thumbnail import BodySetWorkflowThumbnail
from ...models.http_validation_error import HTTPValidationError
from ...models.workflow_record_dto import WorkflowRecordDTO
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: BodySetWorkflowThumbnail,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/workflows/i/{workflow_id}/thumbnail".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WorkflowRecordDTO | None:
    if response.status_code == 200:
        response_200 = WorkflowRecordDTO.from_dict(response.json())

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
) -> Response[HTTPValidationError | WorkflowRecordDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: BodySetWorkflowThumbnail,
) -> Response[HTTPValidationError | WorkflowRecordDTO]:
    """Set Workflow Thumbnail

     Sets a workflow's thumbnail image

    Args:
        workflow_id (str): The workflow to update
        body (BodySetWorkflowThumbnail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkflowRecordDTO]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: BodySetWorkflowThumbnail,
) -> HTTPValidationError | WorkflowRecordDTO | None:
    """Set Workflow Thumbnail

     Sets a workflow's thumbnail image

    Args:
        workflow_id (str): The workflow to update
        body (BodySetWorkflowThumbnail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorkflowRecordDTO
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: BodySetWorkflowThumbnail,
) -> Response[HTTPValidationError | WorkflowRecordDTO]:
    """Set Workflow Thumbnail

     Sets a workflow's thumbnail image

    Args:
        workflow_id (str): The workflow to update
        body (BodySetWorkflowThumbnail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkflowRecordDTO]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: BodySetWorkflowThumbnail,
) -> HTTPValidationError | WorkflowRecordDTO | None:
    """Set Workflow Thumbnail

     Sets a workflow's thumbnail image

    Args:
        workflow_id (str): The workflow to update
        body (BodySetWorkflowThumbnail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorkflowRecordDTO
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
