import unittest
from Problemas.python import median_two_sorted_arrays
import importlib.util

class TestMedianTwoSortedArrays(unittest.TestCase):
    
    def test_python_case_1(self):
        #Input: nums1 = [1,3], nums2 = [2]
        #Output: 2.00000
        exce = median_two_sorted_arrays.Solution()
        self.assertEqual(exce.find_median_sorted_arrays([1,3],[2]),2.00000)
    
    def test_python_case_2(self):
        #Input: nums1 = [1,2], nums2 = [3,4]
        #Output: 2.50000
        exce = median_two_sorted_arrays.Solution()
        self.assertEqual(exce.find_median_sorted_arrays([1,2],[3,4]),2.50000)
    
    def test_c_plus_plus_case_1(self):
        
        module_name = "suma_module.so"

        # Intentamos encontrar y cargar el módulo dinámicamente
        try:
            spec = importlib.util.find_spec(module_name)
            if spec is not None:
                suma_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(suma_module)
                self.assertEqual(suma_module(5,7),12)
            else:
                raise ImportError(f"No se pudo encontrar el módulo: {module_name}")
        except ImportError as e:
            print(f"Error al importar el módulo: {e}")
            exit(1)

        
        
        