"""Select platform for tibber_prices_helper."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.tibber_prices_helper.const import PARALLEL_UPDATES as PARALLEL_UPDATES
from homeassistant.components.select import SelectEntityDescription

from .fan_speed import ENTITY_DESCRIPTIONS as FAN_SPEED_DESCRIPTIONS, TibberPricesHelperFanSpeedSelect

if TYPE_CHECKING:
    from custom_components.tibber_prices_helper.data import TibberPricesHelperConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

# Combine all entity descriptions from different modules
ENTITY_DESCRIPTIONS: tuple[SelectEntityDescription, ...] = (*FAN_SPEED_DESCRIPTIONS,)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: TibberPricesHelperConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the select platform."""
    async_add_entities(
        TibberPricesHelperFanSpeedSelect(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in FAN_SPEED_DESCRIPTIONS
    )
