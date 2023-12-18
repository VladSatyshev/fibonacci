import unittest
from src.fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        # src: https://www.dcode.fr/fibonacci-numbers
        self.valid_fibonacci = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            6: 8,
            7: 13,
            8: 21,
            9: 34,
            10: 55,
            100: 354224848179261915075,
            151: 16130531424904581415797907386349,
            200: 280571172992510140037611932413038677189525,
            253: 33449372971981195681356806732944396691005381570580873,
            300: 222232244629420445529739893461909967206666939096499764990979600,
            355: 69362907070206748494476200566565775354902428015845969798000696945226974645,
            400: 176023680645013966468226945392411250770384383304492191886725992896575345044216019675,
            457: 143835667151675481333619103454952008707730339918865881486873359084765896974634068647640876549937,
            499: 86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501,
            500: 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125,
        }

    def test_valid_fib_N(self):
        for valid_input, valid_result in self.valid_fibonacci.items():
            self.assertEqual(fibonacci(valid_input, "N"), valid_result)

    def test_valid_fib_LogN(self):
        for valid_input, valid_result in self.valid_fibonacci.items():
            self.assertEqual(fibonacci(valid_input, "LogN"), valid_result)

    def test_wrong_type_n_fib_N(self):
        self.assertRaises(TypeError, fibonacci, "100", "N")

    def test_wrong_type_n_fib_LogN(self):
        self.assertRaises(TypeError, fibonacci, "100", "LogN")

    def test_wrong_type_a(self):
        self.assertRaises(TypeError, fibonacci, "100", 1)

    def test_argument_missing(self):
        self.assertRaises(TypeError, fibonacci, 100)

    def test_negative_value_n_fib_N(self):
        self.assertRaises(ValueError, fibonacci, -1, "N")

    def test_negative_value_n_fib_LogN(self):
        self.assertRaises(ValueError, fibonacci, -1, "LogN")

    def test_value_n_over500_fib_N(self):
        self.assertRaises(ValueError, fibonacci, 501, "N")

    def test_value_n_over500_fib_LogN(self):
        self.assertRaises(ValueError, fibonacci, 501, "LogN")

    def test_wrong_value_a(self):
        self.assertRaises(ValueError, fibonacci, 100, "Log(N)")
