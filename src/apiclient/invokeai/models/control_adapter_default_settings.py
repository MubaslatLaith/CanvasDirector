from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlAdapterDefaultSettings")


@_attrs_define
class ControlAdapterDefaultSettings:
    """
    Attributes:
        preprocessor (None | str):
        fp8_storage (bool | None | Unset): Store weights in FP8 to reduce VRAM usage (~50% savings). Weights are cast to
            compute dtype during inference.
    """

    preprocessor: None | str
    fp8_storage: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        preprocessor: None | str
        preprocessor = self.preprocessor

        fp8_storage: bool | None | Unset
        if isinstance(self.fp8_storage, Unset):
            fp8_storage = UNSET
        else:
            fp8_storage = self.fp8_storage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "preprocessor": preprocessor,
            }
        )
        if fp8_storage is not UNSET:
            field_dict["fp8_storage"] = fp8_storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_preprocessor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        preprocessor = _parse_preprocessor(d.pop("preprocessor"))

        def _parse_fp8_storage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fp8_storage = _parse_fp8_storage(d.pop("fp8_storage", UNSET))

        control_adapter_default_settings = cls(
            preprocessor=preprocessor,
            fp8_storage=fp8_storage,
        )

        return control_adapter_default_settings
