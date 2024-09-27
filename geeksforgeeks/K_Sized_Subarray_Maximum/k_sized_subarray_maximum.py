import unittest
### The big O is n*k
def mine_max_of_subarrays(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        sub = arr[i:k+i]
        maxis = max(sub)
        result.append(maxis)
    return result

### Chatgpt solution
from collections import deque

def max_of_subarrays(k, arr):
    result = []
    dq = deque()  # Usaremos deque para almacenar los índices

    for i in range(len(arr)):
        # Eliminar los elementos que están fuera de la ventana de tamaño k
        if dq and dq[0] == i - k:
            dq.popleft()

        # Eliminar los elementos más pequeños que el actual del final de la deque
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Agregar el índice actual al final de la deque
        dq.append(i)

        # Cuando alcanzamos al menos k elementos, el máximo es el elemento en la cabeza de la deque
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


########## Unitest ##########

class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(max_of_subarrays(3, [1, 2, 3, 1, 4, 5, 2, 3, 6]),
                         [3, 3, 4, 5, 5, 5, 6])

    def test_2(self):
        self.assertEqual(max_of_subarrays(4,
                                        [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]),
                                        [10, 10, 10, 15, 15, 90, 90])

if __name__ == "__main__":
    unittest.main()

