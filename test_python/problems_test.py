import unittest
from Problemas.python import median_two_sorted_arrays,matrix_layer_rotation, merge_sort
import random

class TestMedianTwoSortedArrays(unittest.TestCase):
    
    def test_python_case_1(self):
        #Input: nums1 = [1,3], nums2 = [2]
        #Output: 2.00000
        exce = median_two_sorted_arrays.Solution()
        self.assertEqual(exce.find_median_sorted_arrays([1,3],[2]),2.00000)
    
    def test_python_case_2(self):
        #Input: nums1 = [1,2], nums2 = [3,4]
        #Output: 2.50000
        exec= median_two_sorted_arrays.Solution()
        self.assertEqual(exec.find_median_sorted_arrays([1,2],[3,4]),2.50000)
    

class TestMergeSort(unittest.TestCase):
    
    def test_case_1(self):
        
        n = 11
        min_value = 1
        max_value = 100

        # Genera una lista de n números aleatorios en el rango especificado
        lista = [random.randint(min_value, max_value) for _ in range(n)]
        
        arr_sorted=merge_sort.merge_sort(lista)
        
    
        self.assertEqual(arr_sorted,sorted(lista))
        
class TestMatrixLayerRotation(unittest.TestCase):
    
    def test_matrix_path(self):
        matrix = [
            [1,2,3,4,5,6],
            [20,1,2,3,4,7],
            [19,12,1,2,5,8],
            [18,11,4,3,6,9],
            [17,10,9,8,7,10],
            [16,15,14,13,12,11],
            
        ]
        
        matrix_layer_rotation.path(matrix,0)
    def test_matrix_path_2(self):
        matrix = [
            [1,2,3,4,5,6],
            [16,1,2,3,4,7],
            [15,8,7,6,5,8],
            [14,13,12,11,10,9],
            
        ]
        
        matrix_layer_rotation.path(matrix,1)
        
        
        