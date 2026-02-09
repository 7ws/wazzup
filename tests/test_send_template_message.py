from wazzup.drivers import WhatsAppMessagingDriver
from wazzup.models import messages
from wazzup.models.messages import template_componenets, template_parameters


class Test_send_template_with_header_message:

    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        template_mame = 'my_template_name'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        template_message = messages.TemplateMessage(
            to=recipient_phone_number,
            template_name=template_mame,
            components=[
                template_componenets.ComponentHeader(
                    parameters=[
                        template_parameters.NamedTextParameter(
                            parameter_name='my_parameter_name',
                            value='My Header Text'
                        )
                    ]
                )
            ]
        )

        # Call
        response = driver.send_template_message(template_message)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'to': f'{recipient_phone_number}',
                    'type': 'template',
                    'template': {
                        'name': f'{template_mame}',
                        'language': {'code': 'pt_BR'},
                        'components': [
                            {
                                'type': 'header',
                                'parameters': [
                                    {
                                        'type': 'text',
                                        'parameter_name': 'my_parameter_name',
                                        'text': 'My Header Text'
                                    }
                                ]
                            }
                        ]
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]


class Test_send_template_with_body_message:

    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        template_mame = 'my_template_name'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        template_message = messages.TemplateMessage(
            to=recipient_phone_number,
            template_name=template_mame,
            components=[
                template_componenets.ComponentBody(
                    parameters=[
                        template_parameters.NamedTextParameter(
                            parameter_name='my_parameter_name',
                            value='My Header Text'
                        )
                    ]
                )
            ]
        )

        # Call
        response = driver.send_template_message(template_message)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'to': f'{recipient_phone_number}',
                    'type': 'template',
                    'template': {
                        'name': f'{template_mame}',
                        'language': {'code': 'pt_BR'},
                        'components': [
                            {
                                'type': 'body',
                                'parameters': [
                                    {
                                        'type': 'text',
                                        'parameter_name': 'my_parameter_name',
                                        'text': 'My Header Text'
                                    }
                                ]
                            }
                        ]
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]


class Test_send_template_with_footer_message:

    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        template_mame = 'my_template_name'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        template_message = messages.TemplateMessage(
            to=recipient_phone_number,
            template_name=template_mame,
            components=[
                template_componenets.ComponentFooter(
                    parameters=[
                        template_parameters.NamedTextParameter(
                            parameter_name='my_parameter_name',
                            value='My Header Text'
                        )
                    ]
                )
            ]
        )

        # Call
        response = driver.send_template_message(template_message)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'to': f'{recipient_phone_number}',
                    'type': 'template',
                    'template': {
                        'name': f'{template_mame}',
                        'language': {'code': 'pt_BR'},
                        'components': [
                            {
                                'type': 'footer',
                                'parameters': [
                                    {
                                        'type': 'text',
                                        'parameter_name': 'my_parameter_name',
                                        'text': 'My Header Text'
                                    }
                                ]
                            }
                        ]
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]


class Test_send_template_with_button_message:

    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        template_mame = 'my_template_name'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        template_message = messages.TemplateMessage(
            to=recipient_phone_number,
            template_name=template_mame,
            components=[
                template_componenets.ComponentButton(
                    parameters=[
                        template_parameters.PayloadParameter('My Payload Text')
                    ]
                )
            ]
        )

        # Call
        response = driver.send_template_message(template_message)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'to': f'{recipient_phone_number}',
                    'type': 'template',
                    'template': {
                        'name': f'{template_mame}',
                        'language': {'code': 'pt_BR'},
                        'components': [
                            {
                                "type": "button",
                                "sub_type": "quick_reply",
                                "index": "0",
                                "parameters": [
                                    {
                                        "type": "payload",
                                        "payload": "My Payload Text",
                                    },
                                ],
                            }
                        ],
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]
