from wazzup.drivers import WhatsAppMessagingDriver
from wazzup.models import messages


class Test_send_text_message:
    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        message_content = 'Hello, this is a test message!'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        text_message = messages.TextMessage(
            message_content=message_content,
            to=recipient_phone_number,
        )

        # Call
        response = driver.send_text_message(text_message=text_message)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'recipient_type': 'individual',
                    'to': f'{recipient_phone_number}',
                    'type': 'text',
                    'text': {
                        'preview_url': False,
                        'body': f'{message_content}',
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]


class Test_reply_message:
    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = 'phone_number_id'
        recipient_phone_number = 'recipent_phone_number'
        message_content = 'Hello, this is a test message!'
        message_id = 'message_id'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        text_message = messages.TextMessage(
            message_content=message_content,
            to=recipient_phone_number,
        )

        # Call
        response = driver.reply_message(text_message, message_id)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'recipient_type': 'individual',
                    'to': f'{recipient_phone_number}',
                    'type': 'text',
                    'text': {
                        'preview_url': False,
                        'body': f'{message_content}',
                    },
                    'context': {
                        'message_id': message_id,
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]


class Test_react_to_message:
    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        message_id = 'message_id'
        emoji = '\U0001f44d'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        text_message = messages.MessageReaction(
            message_id=message_id,
            emoji=emoji,
            to=recipient_phone_number,
        )

        # Call
        response = driver.react_to_message(text_message)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'recipient_type': 'individual',
                    'to': f'{recipient_phone_number}',
                    'type': 'reaction',
                    'reaction': {
                        'message_id': message_id,
                        'emoji': emoji,
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]


class Test_send_image_message:
    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        image_id = 'image_id'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        image_message = messages.ImageMessage(
            image_id=image_id,
            to=recipient_phone_number,
        )

        # Call
        response = driver.send_image_message(image_message=image_message)

        # Assert Response
        assert response.status_code == 200, response.json()

        # Assert Request
        assert requests_mock.request.call_args_list == [
            mocker.call(
                'POST',
                f'https://graph.facebook.com/v23.0/{phone_number_id}/messages',
                json={
                    'messaging_product': 'whatsapp',
                    'recipient_type': 'individual',
                    'to': f'{recipient_phone_number}',
                    'type': 'image',
                    'image': {
                        'uuid': f'{image_id}',
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]


class Test_send_location_message:
    def test_calls_whatsapp_with_expected_data(self, mocker, requests_mock):
        # Prepare
        requests_mock.request.return_value.status_code = 200

        access_token = 'my_access_token'
        phone_number_id = '1111111111111111'
        recipient_phone_number = '222222222222222'
        latitude = '123'
        longitude = '456'
        name = 'Casa da Xuxa'
        address = 'Rua no fim do arcoiris'
        driver = WhatsAppMessagingDriver(access_token, phone_number_id)

        location_message = messages.LocationMessage(
            to=recipient_phone_number,
            latitude=latitude,
            longitude=longitude,
            name=name,
            address=address,
        )

        # Call
        response = driver.send_location_message(location_message)

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
                    'type': 'location',
                    'location': {
                        'latitude': latitude,
                        'longitude': longitude,
                        'name': name,
                        'address': address,
                    },
                },
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'},
            )
        ]
