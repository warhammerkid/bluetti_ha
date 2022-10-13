"""The Bluetti integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ADDRESS, Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__package__)



"""


So basically I need a config flow for device discover and "adding"

and in __init__ I need to use homeassistant.helpers.update_coordinator.DataUpdateCoordinator to run updates on a specific interval

They have specific home-assistant wrappers around bluetooth devices, so I need to build one of my own and inline it to wrap around bluetti_mqtt

"""


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    address: str = entry.data[CONF_ADDRESS]
    _LOGGER.info(f"Device address: {address}")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return True
