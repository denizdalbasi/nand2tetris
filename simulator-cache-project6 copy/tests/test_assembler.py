import unittest
from assembler.symbol_table import SymbolTable

class TestSymbolTable(unittest.TestCase):
    def setUp(self):
        self.st = SymbolTable()

    def test_predefined_symbols(self):
        self.assertEqual(self.st.get_address("SP"), 0)
        self.assertEqual(self.st.get_address("R0"), 0)
        self.assertEqual(self.st.get_address("R15"), 15)
        self.assertEqual(self.st.get_address("SCREEN"), 16384)

    def test_add_and_contains(self):
        self.assertFalse(self.st.contains("LOOP"))
        self.st.add_entry("LOOP", 10)
        self.assertTrue(self.st.contains("LOOP"))
        self.assertEqual(self.st.get_address("LOOP"), 10)

if __name__ == "__main__":
    unittest.main()