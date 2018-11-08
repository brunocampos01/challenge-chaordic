import json
import unittest
from flask import Flask
import part_1 

part_1 = Flask('part_1')

@part_1.route('/chaordic.com.br/v1/products/', methods=['POST'])
class TestHome(unittest.TestCase):
    def test_post(self):
        app = part_1.test_client()
        response = app.post('/chaordic.com.br/v1/products/', data = json.dumps(
            dict(id = "123", name = "mesa")))
        self.assertEqual(201, response.status_code)

if __name__ == '__main__':
    unittest.main()