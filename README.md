# WaZZup

![WaZZup](https://media1.tenor.com/m/5XNfYyBGDNgAAAAd/wazappp.gif)

Python client library for the WhatsApp Cloud API.

## Installation

```bash
pip install wazzup
```

## Requirements

- Python >= 3.11

## Drivers

| Driver | Purpose |
|---|---|
| `WhatsAppMessagingDriver` | Send text, image, location, and reaction messages |
| `WhatsAppTemplateDriver` | Send template messages and list templates |
| `WhatsAppBusinessDriver` | Manage WhatsApp Business account settings |

```python
from wazzup.drivers import WhatsAppMessagingDriver
from wazzup.drivers import WhatsAppTemplateDriver
from wazzup.drivers import WhatsAppBusinessDriver
```

## Message Models

Available under `wazzup.models.messages`:

- `TextMessage`
- `ImageMessage`
- `LocationMessage`
- `MessageReaction`
- `TemplateMessage`

## Template Models

Available under `wazzup.models.templates`:

- `Template`
- Template components (header, body, footer, buttons)

## License

MIT
