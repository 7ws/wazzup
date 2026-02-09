import requests


class WhatsAppAbstractDriver:
    """Base class for WhatsApp API drivers."""

    BASE_URL = 'https://graph.facebook.com/v23.0/'

    def __init__(self, *, enabled: bool = True) -> None:
        self.enabled = enabled

    def _get_common_headers(self) -> dict[str, str]:
        """
        Get standard headers for json response
        """
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }

        return headers

    def _make_request(
        self,
        method: str,
        url: str,
        data: dict[str, str],
    ) -> requests.Response:
        if not self.enabled:
            response = requests.Response()
            response.status_code = 200
            return response

        headers = self._get_common_headers()
        response = requests.request(method, url, json=data, headers=headers)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        except Exception as e:
            print(e)

        return response
