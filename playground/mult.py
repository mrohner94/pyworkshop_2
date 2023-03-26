import unittest

def multiply(x, y):
    return x * y

# Should not inline this test, but for learning purposees
class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 10

        self.assertEqual(multiply(test_x, test_y), 50, "should be 50")

    

if __name__ == "__main__":
    unittest.main()
        