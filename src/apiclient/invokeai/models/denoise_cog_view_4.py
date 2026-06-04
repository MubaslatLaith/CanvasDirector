from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_field import BoardField
    from ..models.cog_view_4_conditioning_field import CogView4ConditioningField
    from ..models.denoise_mask_field import DenoiseMaskField
    from ..models.latents_field import LatentsField
    from ..models.metadata_field import MetadataField
    from ..models.transformer_field import TransformerField


T = TypeVar("T", bound="DenoiseCogView4")


@_attrs_define
class DenoiseCogView4:
    """Run the denoising process with a CogView4 model.

    Attributes:
        id (str): The id of this instance of an invocation. Must be unique among all instances of invocations.
        type_ (Literal['cogview4_denoise']):  Default: 'cogview4_denoise'.
        board (BoardField | None | Unset): The board to save the image to
        metadata (MetadataField | None | Unset): Optional metadata to be saved with the image
        is_intermediate (bool | Unset): Whether or not this is an intermediate invocation. Default: False.
        use_cache (bool | Unset): Whether or not to use the cache Default: True.
        latents (LatentsField | None | Unset): Latents tensor
        noise (LatentsField | None | Unset): Noise tensor
        denoise_mask (DenoiseMaskField | None | Unset): A mask of the region to apply the denoising process to. Values
            of 0.0 represent the regions to be fully denoised, and 1.0 represent the regions to be preserved.
        denoising_start (float | Unset): When to start denoising, expressed a percentage of total steps Default: 0.0.
        denoising_end (float | Unset): When to stop denoising, expressed a percentage of total steps Default: 1.0.
        transformer (None | TransformerField | Unset): CogView4 model (Transformer) to load
        positive_conditioning (CogView4ConditioningField | None | Unset): Positive conditioning tensor
        negative_conditioning (CogView4ConditioningField | None | Unset): Negative conditioning tensor
        cfg_scale (float | list[float] | Unset): Classifier-Free Guidance scale Default: 3.5.
        width (int | Unset): Width of the generated image. Default: 1024.
        height (int | Unset): Height of the generated image. Default: 1024.
        steps (int | Unset): Number of steps to run Default: 25.
        seed (int | Unset): Randomness seed for reproducibility. Default: 0.
    """

    id: str
    type_: Literal["cogview4_denoise"] = "cogview4_denoise"
    board: BoardField | None | Unset = UNSET
    metadata: MetadataField | None | Unset = UNSET
    is_intermediate: bool | Unset = False
    use_cache: bool | Unset = True
    latents: LatentsField | None | Unset = UNSET
    noise: LatentsField | None | Unset = UNSET
    denoise_mask: DenoiseMaskField | None | Unset = UNSET
    denoising_start: float | Unset = 0.0
    denoising_end: float | Unset = 1.0
    transformer: None | TransformerField | Unset = UNSET
    positive_conditioning: CogView4ConditioningField | None | Unset = UNSET
    negative_conditioning: CogView4ConditioningField | None | Unset = UNSET
    cfg_scale: float | list[float] | Unset = 3.5
    width: int | Unset = 1024
    height: int | Unset = 1024
    steps: int | Unset = 25
    seed: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.board_field import BoardField
        from ..models.cog_view_4_conditioning_field import CogView4ConditioningField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.latents_field import LatentsField
        from ..models.metadata_field import MetadataField
        from ..models.transformer_field import TransformerField

        id = self.id

        type_ = self.type_

        board: dict[str, Any] | None | Unset
        if isinstance(self.board, Unset):
            board = UNSET
        elif isinstance(self.board, BoardField):
            board = self.board.to_dict()
        else:
            board = self.board

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, MetadataField):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        is_intermediate = self.is_intermediate

        use_cache = self.use_cache

        latents: dict[str, Any] | None | Unset
        if isinstance(self.latents, Unset):
            latents = UNSET
        elif isinstance(self.latents, LatentsField):
            latents = self.latents.to_dict()
        else:
            latents = self.latents

        noise: dict[str, Any] | None | Unset
        if isinstance(self.noise, Unset):
            noise = UNSET
        elif isinstance(self.noise, LatentsField):
            noise = self.noise.to_dict()
        else:
            noise = self.noise

        denoise_mask: dict[str, Any] | None | Unset
        if isinstance(self.denoise_mask, Unset):
            denoise_mask = UNSET
        elif isinstance(self.denoise_mask, DenoiseMaskField):
            denoise_mask = self.denoise_mask.to_dict()
        else:
            denoise_mask = self.denoise_mask

        denoising_start = self.denoising_start

        denoising_end = self.denoising_end

        transformer: dict[str, Any] | None | Unset
        if isinstance(self.transformer, Unset):
            transformer = UNSET
        elif isinstance(self.transformer, TransformerField):
            transformer = self.transformer.to_dict()
        else:
            transformer = self.transformer

        positive_conditioning: dict[str, Any] | None | Unset
        if isinstance(self.positive_conditioning, Unset):
            positive_conditioning = UNSET
        elif isinstance(self.positive_conditioning, CogView4ConditioningField):
            positive_conditioning = self.positive_conditioning.to_dict()
        else:
            positive_conditioning = self.positive_conditioning

        negative_conditioning: dict[str, Any] | None | Unset
        if isinstance(self.negative_conditioning, Unset):
            negative_conditioning = UNSET
        elif isinstance(self.negative_conditioning, CogView4ConditioningField):
            negative_conditioning = self.negative_conditioning.to_dict()
        else:
            negative_conditioning = self.negative_conditioning

        cfg_scale: float | list[float] | Unset
        if isinstance(self.cfg_scale, Unset):
            cfg_scale = UNSET
        elif isinstance(self.cfg_scale, list):
            cfg_scale = self.cfg_scale

        else:
            cfg_scale = self.cfg_scale

        width = self.width

        height = self.height

        steps = self.steps

        seed = self.seed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if board is not UNSET:
            field_dict["board"] = board
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if is_intermediate is not UNSET:
            field_dict["is_intermediate"] = is_intermediate
        if use_cache is not UNSET:
            field_dict["use_cache"] = use_cache
        if latents is not UNSET:
            field_dict["latents"] = latents
        if noise is not UNSET:
            field_dict["noise"] = noise
        if denoise_mask is not UNSET:
            field_dict["denoise_mask"] = denoise_mask
        if denoising_start is not UNSET:
            field_dict["denoising_start"] = denoising_start
        if denoising_end is not UNSET:
            field_dict["denoising_end"] = denoising_end
        if transformer is not UNSET:
            field_dict["transformer"] = transformer
        if positive_conditioning is not UNSET:
            field_dict["positive_conditioning"] = positive_conditioning
        if negative_conditioning is not UNSET:
            field_dict["negative_conditioning"] = negative_conditioning
        if cfg_scale is not UNSET:
            field_dict["cfg_scale"] = cfg_scale
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if steps is not UNSET:
            field_dict["steps"] = steps
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_field import BoardField
        from ..models.cog_view_4_conditioning_field import CogView4ConditioningField
        from ..models.denoise_mask_field import DenoiseMaskField
        from ..models.latents_field import LatentsField
        from ..models.metadata_field import MetadataField
        from ..models.transformer_field import TransformerField

        d = dict(src_dict)
        id = d.pop("id")

        type_ = cast(Literal["cogview4_denoise"], d.pop("type"))
        if type_ != "cogview4_denoise":
            raise ValueError(f"type must match const 'cogview4_denoise', got '{type_}'")

        def _parse_board(data: object) -> BoardField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                board_type_0 = BoardField.from_dict(data)

                return board_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BoardField | None | Unset, data)

        board = _parse_board(d.pop("board", UNSET))

        def _parse_metadata(data: object) -> MetadataField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MetadataField.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataField | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        is_intermediate = d.pop("is_intermediate", UNSET)

        use_cache = d.pop("use_cache", UNSET)

        def _parse_latents(data: object) -> LatentsField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latents_type_0 = LatentsField.from_dict(data)

                return latents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LatentsField | None | Unset, data)

        latents = _parse_latents(d.pop("latents", UNSET))

        def _parse_noise(data: object) -> LatentsField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                noise_type_0 = LatentsField.from_dict(data)

                return noise_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LatentsField | None | Unset, data)

        noise = _parse_noise(d.pop("noise", UNSET))

        def _parse_denoise_mask(data: object) -> DenoiseMaskField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                denoise_mask_type_0 = DenoiseMaskField.from_dict(data)

                return denoise_mask_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DenoiseMaskField | None | Unset, data)

        denoise_mask = _parse_denoise_mask(d.pop("denoise_mask", UNSET))

        denoising_start = d.pop("denoising_start", UNSET)

        denoising_end = d.pop("denoising_end", UNSET)

        def _parse_transformer(data: object) -> None | TransformerField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transformer_type_0 = TransformerField.from_dict(data)

                return transformer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransformerField | Unset, data)

        transformer = _parse_transformer(d.pop("transformer", UNSET))

        def _parse_positive_conditioning(data: object) -> CogView4ConditioningField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                positive_conditioning_type_0 = CogView4ConditioningField.from_dict(data)

                return positive_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CogView4ConditioningField | None | Unset, data)

        positive_conditioning = _parse_positive_conditioning(d.pop("positive_conditioning", UNSET))

        def _parse_negative_conditioning(data: object) -> CogView4ConditioningField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                negative_conditioning_type_0 = CogView4ConditioningField.from_dict(data)

                return negative_conditioning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CogView4ConditioningField | None | Unset, data)

        negative_conditioning = _parse_negative_conditioning(d.pop("negative_conditioning", UNSET))

        def _parse_cfg_scale(data: object) -> float | list[float] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cfg_scale_type_1 = cast(list[float], data)

                return cfg_scale_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | list[float] | Unset, data)

        cfg_scale = _parse_cfg_scale(d.pop("cfg_scale", UNSET))

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        steps = d.pop("steps", UNSET)

        seed = d.pop("seed", UNSET)

        denoise_cog_view_4 = cls(
            id=id,
            type_=type_,
            board=board,
            metadata=metadata,
            is_intermediate=is_intermediate,
            use_cache=use_cache,
            latents=latents,
            noise=noise,
            denoise_mask=denoise_mask,
            denoising_start=denoising_start,
            denoising_end=denoising_end,
            transformer=transformer,
            positive_conditioning=positive_conditioning,
            negative_conditioning=negative_conditioning,
            cfg_scale=cfg_scale,
            width=width,
            height=height,
            steps=steps,
            seed=seed,
        )

        denoise_cog_view_4.additional_properties = d
        return denoise_cog_view_4

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
