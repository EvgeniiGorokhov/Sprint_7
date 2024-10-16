import requests
import allure
from urls import Urls


class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и тело ответа.')
    def test_orders_list_get_success(self):
        response = requests.get(Urls.URL_ORDERS_CREATE)
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]