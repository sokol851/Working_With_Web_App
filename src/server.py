from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler
import requests


class MyServer(BaseHTTPRequestHandler):
    """
        Класс отвечает за обработку входящих запросов от клиентов
    """

    def __get_html_content(self):
        response = requests.get('https://raw.githubusercontent.com/sokol851/Working_With_Web_App/main/index.html')
        data = response.text
        return data

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Тип данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа
