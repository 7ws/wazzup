import json

import requests
from requests import HTTPError

from wazzup.drivers import WhatsAppBusinessDriver
from wazzup.drivers import business_driver as business_driver_module


class Test_list_templates:
    def test_calls_whatsapp_with_expected_request(self, mocker):
        # Given
        mock_requests = mocker.patch.object(
            business_driver_module,
            'requests',
            spec=requests,
        )
        mock_requests.HTTPError = HTTPError
        mock_response = mocker.MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'data': [
                {
                    'name': 'bem_vinda',
                    'previous_category': 'UTILITY',
                    'parameter_format': 'POSITIONAL',
                    'components': [
                        {
                            'type': 'BODY',
                            'text': 'Bem vinda ao Redativo!',
                        }
                    ],
                    'language': 'pt_BR',
                    'status': 'APPROVED',
                    'category': 'MARKETING',
                    'id': '1232765995653702',
                }
            ],
            'paging': {
                'cursors': {
                    'before': 'QVFI...',
                    'after': 'QVFI...',
                }
            },
        }
        mock_requests.get.return_value = mock_response

        access_token = 'my_access_token'
        waba_id = '123456789'
        driver = WhatsAppBusinessDriver(access_token, waba_id)

        # When
        response = driver.list_templates()

        # Then
        assert response.status_code == 200
        assert response.json()['data'][0]['name'] == 'bem_vinda'
        assert response.json()['data'][0]['id'] == '1232765995653702'
        assert response.json()['data'][0]['status'] == 'APPROVED'

        mock_requests.get.assert_called_once_with(
            f'https://graph.facebook.com/v24.0/{waba_id}/message_templates',
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
        )

    def test_returns_empty_data_when_disabled(self):
        # Given
        access_token = 'my_access_token'
        waba_id = '123456789'
        driver = WhatsAppBusinessDriver(access_token, waba_id, enabled=False)

        # When
        response = driver.list_templates()

        # Then
        assert response.status_code == 200
        assert json.loads(response.content) == {'data': []}

    def test_uses_custom_api_version(self, mocker):
        # Given
        mock_requests = mocker.patch.object(
            business_driver_module,
            'requests',
            spec=requests,
        )
        mock_requests.HTTPError = HTTPError
        mock_response = mocker.MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': []}
        mock_requests.get.return_value = mock_response

        access_token = 'my_access_token'
        waba_id = '123456789'
        driver = WhatsAppBusinessDriver(
            access_token, waba_id, api_version='v23.0'
        )

        # When
        driver.list_templates()

        # Then
        mock_requests.get.assert_called_once_with(
            f'https://graph.facebook.com/v23.0/{waba_id}/message_templates',
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}',
            },
        )
