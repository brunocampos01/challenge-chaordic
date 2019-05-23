import unittest

import requests
from flask import Flask

part_1 = Flask('part_1')


class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.part_1 = part_1.test_client()

    def test_request(self):
        # envia uma requisicao POST
        result = requests.post('http://localhost:5000/chaordic.com.br/v1/products/',
                               json={"id": "123", "name": "mesa"})
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    print('INICIANDO OS TESTES')
    print(70 * '-')
    unittest.main(verbosity=2)  # verbosity=2, tras mais informação na saída, sobre a função
