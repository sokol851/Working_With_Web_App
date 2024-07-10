#!/usr/bin/python
from http.server import HTTPServer
from src.server import MyServer


hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Остановка веб сервера
    webServer.server_close()
    print("Server stopped.")
