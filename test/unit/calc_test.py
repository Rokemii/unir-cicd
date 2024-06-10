import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(8, 4))
        self.assertEqual(0, self.calc.substract(8, 8))
        self.assertEqual(6, self.calc.substract(18, 12))
        self.assertEqual(1, self.calc.substract(1, 0))
        
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(8, 0))
        self.assertEqual(32, self.calc.power(2, 5))
        self.assertEqual(1, self.calc.power(1, 0))
        
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(5, self.calc.raiz_cuadrada(25))
        self.assertEqual(0, self.calc.raiz_cuadrada(0))
        self.assertEqual(3, self.calc.raiz_cuadrada(9))
        self.assertEqual(1, self.calc.raiz_cuadrada(1)) 
        
    def test_logarthim_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.logaritmo_base_10(10))
        self.assertEqual(2, self.calc.logaritmo_base_10(100))
        self.assertEqual(-3, self.calc.logaritmo_base_10(0.001))
        self.assertEqual(0, self.calc.logaritmo_base_10(1)) 
        
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
        
    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object()) 
        
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
        
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
        
    def test_sqroot_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, "2")
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, None)
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, object())
        
    def test_logaritmo_base_10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.logaritmo_base_10, "2")
        self.assertRaises(TypeError, self.calc.logaritmo_base_10, None)
        self.assertRaises(TypeError, self.calc.logaritmo_base_10, object())
        
    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)   
        
    def test_sqrt_method_fails_with_number_less_than_0(self):
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, -1000)
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, -9)
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, -5)
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, -1) 
        
    def test_logarithm_method_fails_with_number_equal_0(self):
        self.assertRaises(TypeError, self.calc.logaritmo_base_10, 0)
            
    def test_check_type_fails_with_invalid_types(self):
        self.assertRaises(TypeError, self.calc.check_type, "hello")
        self.assertRaises(TypeError, self.calc.check_type, [1, 2, 3])
        self.assertRaises(TypeError, self.calc.check_type, {"key": "value"})

    def test_check_type_passes_with_valid_types(self):
        self.assertIsNone(self.calc.check_type(5))
        self.assertIsNone(self.calc.check_type(3.14))
        
    def test_check_types_passes_with_valid_types(self):
        self.assertIsNone(self.calc.check_types(5, 10))
        self.assertIsNone(self.calc.check_types(3, 3.14))
        self.assertIsNone(self.calc.check_types(2.5, 7.8))

    def test_check_types_fails_with_invalid_types(self):
        self.assertRaises(TypeError, self.calc.check_types, "hello", 10)
        self.assertRaises(TypeError, self.calc.check_types, 5, [1, 2, 3])
        self.assertRaises(TypeError, self.calc.check_types, 3.14, {"key": "value"})

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
