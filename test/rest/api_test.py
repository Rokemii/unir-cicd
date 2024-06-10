import http.client
import os
import unittest
from urllib.request import urlopen
import urllib

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "4")

    def test_substract_route(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2")

    def test_multiply_route(self):
        url = f"{BASE_URL}/calc/multiply/4/3"
        try:
            # Realiza la solicitud al servidor
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            
            # Lee y decodifica la respuesta
            result = response.read().decode()

            # Verifica el estado de la respuesta
            self.assertEqual(response.status, http.client.OK)

            # Verifica el resultado de la multiplicación
            self.assertEqual(result, "12")
        
        except Exception as e:
            # Si ocurre algún error durante la solicitud o la verificación, muestra el error
            self.fail(f"Error durante la prueba: {e}")

    def test_divide_route(self):
        url = f"{BASE_URL}/calc/divide/8/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "4.0")

    def test_power_route(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "8")

    def test_square_root_route(self):
        url = f"{BASE_URL}/calc/square_root/25"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "5.0")

    def test_log_base_10_route(self):
        url = f"{BASE_URL}/calc/log_base_10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2.0")
        
    def test_api_add_with_NaN_Value(self):
        url = f"{BASE_URL}/calc/add/2/n"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Operator cannot be converted to number")

    def test_substract_route_with_NaN_Value(self):
        url = f"{BASE_URL}/calc/substract/5/a"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Operator cannot be converted to number")

    def test_multiply_route_with_NaN_Value(self):
        url = f"{BASE_URL}/calc/multiply/4/b"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Operator cannot be converted to number")

    def test_divide_route_with_NaN_Value(self):
        url = f"{BASE_URL}/calc/divide/8/c"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Operator cannot be converted to number")

    def test_power_route_with_NaN_Value(self):
        url = f"{BASE_URL}/calc/power/2/d"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Operator cannot be converted to number")

    def test_square_root_route_with_NaN_Value(self):
        url = f"{BASE_URL}/calc/square_root/e"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Operator cannot be converted to number")

    def test_log_base_10_route_with_NaN_Value(self):
        url = f"{BASE_URL}/calc/log_base_10/f"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Operator cannot be converted to number")

    def test_log_base_10_route_with_value_0(self):
        url = f"{BASE_URL}/calc/log_base_10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "No se puede calcular el logaritmo de un número no positivo")

    def test_square_root_negative_value(self):
        url = f"{BASE_URL}/calc/square_root/-4"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "No se puede sacar una raiz cuadrada con un numero negativo")

    def test_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/8/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertEqual(e.read().decode(), "Division by zero is not possible")
