from aiod.calls import calls

(
    get_list,
    counts,
    get_asset,
    get_asset_from_platform,
    get_content,
    get_assets_async,
    get_list_async,
) = calls.wrap_common_calls(asset_type="case_studies", module=__name__)
