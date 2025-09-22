import aiohttp
from homeassistant.helpers.entity import Entity

DOMAIN = "funfacts"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    language = config.get("language", "en")
    sensor = FunFactSensor(language)
    async_add_entities([sensor], True)

    async def handle_refresh_service(call):
        await sensor.async_get_new_fact()
        sensor.async_write_ha_state()

    hass.services.async_register(DOMAIN, "funfact_refresh", handle_refresh_service)

class FunFactSensor(Entity):
    def __init__(self, language):
        self._language = language
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return "Funfact"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    async def async_update(self):
        # Kein automatisches Update mehr!
        pass

    async def async_get_new_fact(self):
        url = f"https://uselessfacts.jsph.pl/api/v2/facts/random?language={self._language}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                self._state = data.get("text")
                self._attributes = {
                    "source": data.get("source"),
                    "source_url": data.get("source_url"),
                    "permalink": data.get("permalink"),
                    "language": data.get("language")
                }
