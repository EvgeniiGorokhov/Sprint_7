import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password


class TestCourierLogin:
    @allure.title('Проверка успешной аутентификации курьера при вводе валидных данных')
    @allure.description('Проверяются код и тело ответа.')
    def test_courier_login_success(self):
        response = requests.post(Urls.URL_COURIER_LOGIN, data=Data.VALID_COURIER_DATA)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе невалидных данных')
    @allure.description('В тест по очереди передаются наборы данных с несуществующим логином или неверным паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.COURIER_DATA_WITH_WRONG_PASSWORD
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_COURIER_LOGIN, data=nonexistent_credentials)
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': Data.PASSWORD},
        {'login': Data.LOGIN, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_COURIER_LOGIN, data=empty_credentials)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}