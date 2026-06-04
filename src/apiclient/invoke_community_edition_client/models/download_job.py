from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.download_job_status import DownloadJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadJob")


@_attrs_define
class DownloadJob:
    """Class to monitor and control a model download request.

    Attributes:
        dest (str): Initial destination of downloaded model on local disk; a directory or file path
        source (str): Where to download from. Specific types specified in child classes.
        id (int | Unset): Numeric ID of this job Default: -1.
        download_path (None | str | Unset): Final location of downloaded file or directory
        status (DownloadJobStatus | Unset): State of a download job.
        bytes_ (int | Unset): Bytes downloaded so far Default: 0.
        total_bytes (int | Unset): Total file size (bytes) Default: 0.
        error_type (None | str | Unset): Name of exception that caused an error
        error (None | str | Unset): Traceback of the exception that caused an error
        access_token (None | str | Unset): authorization token for protected resources
        priority (int | Unset): Queue priority; lower values are higher priority Default: 10.
        job_started (None | str | Unset): Timestamp for when the download job started
        job_ended (None | str | Unset): Timestamp for when the download job ende1d (completed or errored)
        content_type (None | str | Unset): Content type of downloaded file
        canonical_url (None | str | Unset): Canonical URL to request on resume
        etag (None | str | Unset): ETag from the remote server, if available
        last_modified (None | str | Unset): Last-Modified from the remote server, if available
        final_url (None | str | Unset): Final resolved URL after redirects, if available
        expected_total_bytes (int | None | Unset): Expected total size of the download
        resume_required (bool | Unset): True if server refused resume; restart required Default: False.
        resume_message (None | str | Unset): Message explaining why resume is required
        resume_from_scratch (bool | Unset): True if resume metadata existed but the partial file was missing and the
            download restarted from the beginning Default: False.
    """

    dest: str
    source: str
    id: int | Unset = -1
    download_path: None | str | Unset = UNSET
    status: DownloadJobStatus | Unset = UNSET
    bytes_: int | Unset = 0
    total_bytes: int | Unset = 0
    error_type: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    access_token: None | str | Unset = UNSET
    priority: int | Unset = 10
    job_started: None | str | Unset = UNSET
    job_ended: None | str | Unset = UNSET
    content_type: None | str | Unset = UNSET
    canonical_url: None | str | Unset = UNSET
    etag: None | str | Unset = UNSET
    last_modified: None | str | Unset = UNSET
    final_url: None | str | Unset = UNSET
    expected_total_bytes: int | None | Unset = UNSET
    resume_required: bool | Unset = False
    resume_message: None | str | Unset = UNSET
    resume_from_scratch: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dest = self.dest

        source = self.source

        id = self.id

        download_path: None | str | Unset
        if isinstance(self.download_path, Unset):
            download_path = UNSET
        else:
            download_path = self.download_path

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        bytes_ = self.bytes_

        total_bytes = self.total_bytes

        error_type: None | str | Unset
        if isinstance(self.error_type, Unset):
            error_type = UNSET
        else:
            error_type = self.error_type

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        priority = self.priority

        job_started: None | str | Unset
        if isinstance(self.job_started, Unset):
            job_started = UNSET
        else:
            job_started = self.job_started

        job_ended: None | str | Unset
        if isinstance(self.job_ended, Unset):
            job_ended = UNSET
        else:
            job_ended = self.job_ended

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        canonical_url: None | str | Unset
        if isinstance(self.canonical_url, Unset):
            canonical_url = UNSET
        else:
            canonical_url = self.canonical_url

        etag: None | str | Unset
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        last_modified: None | str | Unset
        if isinstance(self.last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = self.last_modified

        final_url: None | str | Unset
        if isinstance(self.final_url, Unset):
            final_url = UNSET
        else:
            final_url = self.final_url

        expected_total_bytes: int | None | Unset
        if isinstance(self.expected_total_bytes, Unset):
            expected_total_bytes = UNSET
        else:
            expected_total_bytes = self.expected_total_bytes

        resume_required = self.resume_required

        resume_message: None | str | Unset
        if isinstance(self.resume_message, Unset):
            resume_message = UNSET
        else:
            resume_message = self.resume_message

        resume_from_scratch = self.resume_from_scratch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dest": dest,
                "source": source,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if download_path is not UNSET:
            field_dict["download_path"] = download_path
        if status is not UNSET:
            field_dict["status"] = status
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if total_bytes is not UNSET:
            field_dict["total_bytes"] = total_bytes
        if error_type is not UNSET:
            field_dict["error_type"] = error_type
        if error is not UNSET:
            field_dict["error"] = error
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if priority is not UNSET:
            field_dict["priority"] = priority
        if job_started is not UNSET:
            field_dict["job_started"] = job_started
        if job_ended is not UNSET:
            field_dict["job_ended"] = job_ended
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if canonical_url is not UNSET:
            field_dict["canonical_url"] = canonical_url
        if etag is not UNSET:
            field_dict["etag"] = etag
        if last_modified is not UNSET:
            field_dict["last_modified"] = last_modified
        if final_url is not UNSET:
            field_dict["final_url"] = final_url
        if expected_total_bytes is not UNSET:
            field_dict["expected_total_bytes"] = expected_total_bytes
        if resume_required is not UNSET:
            field_dict["resume_required"] = resume_required
        if resume_message is not UNSET:
            field_dict["resume_message"] = resume_message
        if resume_from_scratch is not UNSET:
            field_dict["resume_from_scratch"] = resume_from_scratch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dest = d.pop("dest")

        source = d.pop("source")

        id = d.pop("id", UNSET)

        def _parse_download_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        download_path = _parse_download_path(d.pop("download_path", UNSET))

        _status = d.pop("status", UNSET)
        status: DownloadJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DownloadJobStatus(_status)

        bytes_ = d.pop("bytes", UNSET)

        total_bytes = d.pop("total_bytes", UNSET)

        def _parse_error_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_type = _parse_error_type(d.pop("error_type", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("access_token", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_job_started(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_started = _parse_job_started(d.pop("job_started", UNSET))

        def _parse_job_ended(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_ended = _parse_job_ended(d.pop("job_ended", UNSET))

        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

        def _parse_canonical_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        canonical_url = _parse_canonical_url(d.pop("canonical_url", UNSET))

        def _parse_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_last_modified(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_modified = _parse_last_modified(d.pop("last_modified", UNSET))

        def _parse_final_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        final_url = _parse_final_url(d.pop("final_url", UNSET))

        def _parse_expected_total_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_total_bytes = _parse_expected_total_bytes(d.pop("expected_total_bytes", UNSET))

        resume_required = d.pop("resume_required", UNSET)

        def _parse_resume_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resume_message = _parse_resume_message(d.pop("resume_message", UNSET))

        resume_from_scratch = d.pop("resume_from_scratch", UNSET)

        download_job = cls(
            dest=dest,
            source=source,
            id=id,
            download_path=download_path,
            status=status,
            bytes_=bytes_,
            total_bytes=total_bytes,
            error_type=error_type,
            error=error,
            access_token=access_token,
            priority=priority,
            job_started=job_started,
            job_ended=job_ended,
            content_type=content_type,
            canonical_url=canonical_url,
            etag=etag,
            last_modified=last_modified,
            final_url=final_url,
            expected_total_bytes=expected_total_bytes,
            resume_required=resume_required,
            resume_message=resume_message,
            resume_from_scratch=resume_from_scratch,
        )

        download_job.additional_properties = d
        return download_job

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
