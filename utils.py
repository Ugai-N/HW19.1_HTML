from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs
file = Path(__file__).resolve().parent / 'index.html'

class MyServer(BaseHTTPRequestHandler):
    """Специальный класс, который отвечает за
    обработку входящих запросов от клиентов"""

    def __get_html_content(self):
        """ Метод для выборки скрипта из HTML-файла"""
        f = open(file, 'r', encoding='utf-8')
        result = f.read()
        return result

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))
