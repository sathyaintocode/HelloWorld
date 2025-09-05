import unittest
import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)
    
    def test_sub(self):
        self.assertEqual(app.sub(6,3), 3)

    def test_div(self):
        self.assertEqual(app.div(6,3), 2)

if __name__ == '__main__':
    unittest.main()