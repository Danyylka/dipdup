import demo_big_maps.models as models
from demo_big_maps.types.name_registry.big_map.store_expiry_map_key import StoreExpiryMapKey
from demo_big_maps.types.name_registry.big_map.store_expiry_map_value import StoreExpiryMapValue
from dipdup.context import HandlerContext
from dipdup.models import BigMapDiff


async def on_update_expiry_map(
    ctx: HandlerContext,
    store_expiry_map: BigMapDiff[StoreExpiryMapKey, StoreExpiryMapValue],
) -> None:
    if not store_expiry_map.action.has_value:
        return
    assert store_expiry_map.key
    assert store_expiry_map.value

    timestamp = store_expiry_map.value.__root__
    record_name = bytes.fromhex(store_expiry_map.key.__root__).decode()
    await models.Expiry.update_or_create(
        id=record_name,
        defaults={'timestamp': timestamp},
    )