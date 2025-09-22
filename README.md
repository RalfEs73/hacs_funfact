# 🧠 Funfacts – Home Assistant Integration

This custom Home Assistant integration displays random fun facts right in your dashboard - in English or German!  
Facts are fetched from the public API: https://uselessfacts.jsph.pl.

---

## 🔧 Features

- Fetch a random fun fact via the service (`funfacts.funfact_refresh`)
- Language configurable (`en` or `de`)
- No automatic updates – you decide when to get a new fact
- Displays source, permalink, and language as sensor attributes

---

## 📦 Installation

The recommended way is to install via HACS

[![Open your Home Assistant instance and open the Funfacts custom component repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ralfes73&repository=hacs_funfacts)

Then restart HA and add the the following to your `configuration.yaml`:
```yaml
sensor:
  - platform: funfacts
    language: en  # or "de"
```
