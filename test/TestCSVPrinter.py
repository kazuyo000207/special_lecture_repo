import unittest
import sys
sys.path.append('../speciallecture')
from speciallecture.sample import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("./test/sample.csv")
        l=printer.read()
        self.assertEqual(3, len(l))
        print("test_read1")

    def test_read2(self):
        printer = CSVPrinter("./test/sample.csv")
        l=printer.read()
        self.assertEqual("value2B", l[1][1])
        print("test_read2")

    def test_read3(self):
        try:
            printer = CSVPrinter("./test/sample2.csv")
            l=printer.read()
            unittest.TestCase.fail("This line should not be iinvoked")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
            print("test_read3")


# if __name__ == '__main__':
#     test = TestCSVPrinter()
#     test.test_read1()
#     test.test_read2()
#     test.test_read3()