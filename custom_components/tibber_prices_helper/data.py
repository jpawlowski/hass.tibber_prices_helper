"""Custom types for tibber_prices_helper."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import TibberPricesHelperApiClient
    from .coordinator import TibberPricesHelperDataUpdateCoordinator


type TibberPricesHelperConfigEntry = ConfigEntry[TibberPricesHelperData]


@dataclass
class TibberPricesHelperData:
    """Data for tibber_prices_helper."""

    client: TibberPricesHelperApiClient
    coordinator: TibberPricesHelperDataUpdateCoordinator
    integration: Integration
