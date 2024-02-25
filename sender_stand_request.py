import requests
import configuration


# Создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)


# Получение данных по треку
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO + str(track))
