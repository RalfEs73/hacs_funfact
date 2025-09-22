import requests
from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_entities, discovery_info=None):
    language = config.get("language", "de")
    add_entities([FunFactSensor(language)], True)

class FunFactSensor(Entity):
    def __init__(self, language):
        self._language = language
        self._state = None
        self._attributes = {}

    def update(self):
        url = f"https://uselessfacts.jsph.pl/api/v2/facts/random?language={self._language}"
        try:
            response = requests.get(url)
            data = response.json()
            self._state = data.get("text")
            self._attributes = {
                "source": data.get("source"),
                "source_url": data.get("source_url"),
                "permalink": data.get("permalink"),
                "language": data.get("language")
            }
        except Exception as e:
            self._state = "Fehler beim Abrufen"

    @property
    def name(self):
        return "Funfact"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes
