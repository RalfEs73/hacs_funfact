# 🧠 Funfacts – Home Assistant Integration

This custom Home Assistant integration displays random fun facts right in your dashboard—in German or English!  
Facts are fetched from the public API: https://uselessfacts.jsph.pl.

---

## 🔧 Features

- Fetch a random fun fact via the service (`funfacts.funfact_refresh`)
- Language configurable (`en` or `de`)
- No automatic updates – you decide when to get a new fact
- Displays source, permalink, and language as sensor attributes

---

## 📦 Installation

1. Copy the `funfacts` folder into your Home Assistant directory:  
   `custom_components/funfacts/`
2. Add the following to your `configuration.yaml`:
```yaml
sensor:
  - platform: funfacts
    language: en  # or "de"
```
