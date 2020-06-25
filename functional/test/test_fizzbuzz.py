import unittest
import sys
sys.path.append("../lib")
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_if_ver(self):
        self.assertEqual("1", fizzbuzz.if_ver(1))
        self.assertEqual("2", fizzbuzz.if_ver(2))
        self.assertEqual("Fizz", fizzbuzz.if_ver(3))
        self.assertEqual("4", fizzbuzz.if_ver(4))
        self.assertEqual("Buzz", fizzbuzz.if_ver(5))
        self.assertEqual("Fizz", fizzbuzz.if_ver(6))
        self.assertEqual("7", fizzbuzz.if_ver(7))
        self.assertEqual("8", fizzbuzz.if_ver(8))
        self.assertEqual("Fizz", fizzbuzz.if_ver(9))
        self.assertEqual("Buzz", fizzbuzz.if_ver(10))
        self.assertEqual("11", fizzbuzz.if_ver(11))
        self.assertEqual("Fizz", fizzbuzz.if_ver(12))
        self.assertEqual("13", fizzbuzz.if_ver(13))
        self.assertEqual("14", fizzbuzz.if_ver(14))
        self.assertEqual("FizzBuzz", fizzbuzz.if_ver(15))
        self.assertEqual("16", fizzbuzz.if_ver(16))
        self.assertEqual("17", fizzbuzz.if_ver(17))
        self.assertEqual("Fizz", fizzbuzz.if_ver(18))
        self.assertEqual("19", fizzbuzz.if_ver(19))
        self.assertEqual("Buzz", fizzbuzz.if_ver(20))
        self.assertEqual("Fizz", fizzbuzz.if_ver(21))
        self.assertEqual("22", fizzbuzz.if_ver(22))
        self.assertEqual("23", fizzbuzz.if_ver(23))
        self.assertEqual("Fizz", fizzbuzz.if_ver(24))
        self.assertEqual("Buzz", fizzbuzz.if_ver(25))
        self.assertEqual("26", fizzbuzz.if_ver(26))
        self.assertEqual("Fizz", fizzbuzz.if_ver(27))
        self.assertEqual("28", fizzbuzz.if_ver(28))
        self.assertEqual("29", fizzbuzz.if_ver(29))
        self.assertEqual("FizzBuzz", fizzbuzz.if_ver(30))
        self.assertEqual("31", fizzbuzz.if_ver(31))
        self.assertEqual("32", fizzbuzz.if_ver(32))
        self.assertEqual("Fizz", fizzbuzz.if_ver(33))
        self.assertEqual("34", fizzbuzz.if_ver(34))
        self.assertEqual("Buzz", fizzbuzz.if_ver(35))
        self.assertEqual("Fizz", fizzbuzz.if_ver(36))
        self.assertEqual("37", fizzbuzz.if_ver(37))
        self.assertEqual("38", fizzbuzz.if_ver(38))
        self.assertEqual("Fizz", fizzbuzz.if_ver(39))
        self.assertEqual("Buzz", fizzbuzz.if_ver(40))
        self.assertEqual("41", fizzbuzz.if_ver(41))
        self.assertEqual("Fizz", fizzbuzz.if_ver(42))
        self.assertEqual("43", fizzbuzz.if_ver(43))
        self.assertEqual("44", fizzbuzz.if_ver(44))
        self.assertEqual("FizzBuzz", fizzbuzz.if_ver(45))
        self.assertEqual("46", fizzbuzz.if_ver(46))
        self.assertEqual("47", fizzbuzz.if_ver(47))
        self.assertEqual("Fizz", fizzbuzz.if_ver(48))
        self.assertEqual("49", fizzbuzz.if_ver(49))
        self.assertEqual("Buzz", fizzbuzz.if_ver(50))
        self.assertEqual("Fizz", fizzbuzz.if_ver(51))
        self.assertEqual("52", fizzbuzz.if_ver(52))
        self.assertEqual("53", fizzbuzz.if_ver(53))
        self.assertEqual("Fizz", fizzbuzz.if_ver(54))
        self.assertEqual("Buzz", fizzbuzz.if_ver(55))
        self.assertEqual("56", fizzbuzz.if_ver(56))
        self.assertEqual("Fizz", fizzbuzz.if_ver(57))
        self.assertEqual("58", fizzbuzz.if_ver(58))
        self.assertEqual("59", fizzbuzz.if_ver(59))
        self.assertEqual("FizzBuzz", fizzbuzz.if_ver(60))
        self.assertEqual("61", fizzbuzz.if_ver(61))
        self.assertEqual("62", fizzbuzz.if_ver(62))
        self.assertEqual("Fizz", fizzbuzz.if_ver(63))
        self.assertEqual("64", fizzbuzz.if_ver(64))
        self.assertEqual("Buzz", fizzbuzz.if_ver(65))
        self.assertEqual("Fizz", fizzbuzz.if_ver(66))
        self.assertEqual("67", fizzbuzz.if_ver(67))
        self.assertEqual("68", fizzbuzz.if_ver(68))
        self.assertEqual("Fizz", fizzbuzz.if_ver(69))
        self.assertEqual("Buzz", fizzbuzz.if_ver(70))
        self.assertEqual("71", fizzbuzz.if_ver(71))
        self.assertEqual("Fizz", fizzbuzz.if_ver(72))
        self.assertEqual("73", fizzbuzz.if_ver(73))
        self.assertEqual("74", fizzbuzz.if_ver(74))
        self.assertEqual("FizzBuzz", fizzbuzz.if_ver(75))
        self.assertEqual("76", fizzbuzz.if_ver(76))
        self.assertEqual("77", fizzbuzz.if_ver(77))
        self.assertEqual("Fizz", fizzbuzz.if_ver(78))
        self.assertEqual("79", fizzbuzz.if_ver(79))
        self.assertEqual("Buzz", fizzbuzz.if_ver(80))
        self.assertEqual("Fizz", fizzbuzz.if_ver(81))
        self.assertEqual("82", fizzbuzz.if_ver(82))
        self.assertEqual("83", fizzbuzz.if_ver(83))
        self.assertEqual("Fizz", fizzbuzz.if_ver(84))
        self.assertEqual("Buzz", fizzbuzz.if_ver(85))
        self.assertEqual("86", fizzbuzz.if_ver(86))
        self.assertEqual("Fizz", fizzbuzz.if_ver(87))
        self.assertEqual("88", fizzbuzz.if_ver(88))
        self.assertEqual("89", fizzbuzz.if_ver(89))
        self.assertEqual("FizzBuzz", fizzbuzz.if_ver(90))
        self.assertEqual("91", fizzbuzz.if_ver(91))
        self.assertEqual("92", fizzbuzz.if_ver(92))
        self.assertEqual("Fizz", fizzbuzz.if_ver(93))
        self.assertEqual("94", fizzbuzz.if_ver(94))
        self.assertEqual("Buzz", fizzbuzz.if_ver(95))
        self.assertEqual("Fizz", fizzbuzz.if_ver(96))
        self.assertEqual("97", fizzbuzz.if_ver(97))
        self.assertEqual("98", fizzbuzz.if_ver(98))
        self.assertEqual("Fizz", fizzbuzz.if_ver(99))
        self.assertEqual("Buzz", fizzbuzz.if_ver(100))

    def test_ternary_ver(self):
        self.assertEqual("1", fizzbuzz.ternary_ver(1))
        self.assertEqual("2", fizzbuzz.ternary_ver(2))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(3))
        self.assertEqual("4", fizzbuzz.ternary_ver(4))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(5))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(6))
        self.assertEqual("7", fizzbuzz.ternary_ver(7))
        self.assertEqual("8", fizzbuzz.ternary_ver(8))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(9))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(10))
        self.assertEqual("11", fizzbuzz.ternary_ver(11))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(12))
        self.assertEqual("13", fizzbuzz.ternary_ver(13))
        self.assertEqual("14", fizzbuzz.ternary_ver(14))
        self.assertEqual("FizzBuzz", fizzbuzz.ternary_ver(15))
        self.assertEqual("16", fizzbuzz.ternary_ver(16))
        self.assertEqual("17", fizzbuzz.ternary_ver(17))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(18))
        self.assertEqual("19", fizzbuzz.ternary_ver(19))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(20))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(21))
        self.assertEqual("22", fizzbuzz.ternary_ver(22))
        self.assertEqual("23", fizzbuzz.ternary_ver(23))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(24))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(25))
        self.assertEqual("26", fizzbuzz.ternary_ver(26))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(27))
        self.assertEqual("28", fizzbuzz.ternary_ver(28))
        self.assertEqual("29", fizzbuzz.ternary_ver(29))
        self.assertEqual("FizzBuzz", fizzbuzz.ternary_ver(30))
        self.assertEqual("31", fizzbuzz.ternary_ver(31))
        self.assertEqual("32", fizzbuzz.ternary_ver(32))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(33))
        self.assertEqual("34", fizzbuzz.ternary_ver(34))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(35))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(36))
        self.assertEqual("37", fizzbuzz.ternary_ver(37))
        self.assertEqual("38", fizzbuzz.ternary_ver(38))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(39))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(40))
        self.assertEqual("41", fizzbuzz.ternary_ver(41))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(42))
        self.assertEqual("43", fizzbuzz.ternary_ver(43))
        self.assertEqual("44", fizzbuzz.ternary_ver(44))
        self.assertEqual("FizzBuzz", fizzbuzz.ternary_ver(45))
        self.assertEqual("46", fizzbuzz.ternary_ver(46))
        self.assertEqual("47", fizzbuzz.ternary_ver(47))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(48))
        self.assertEqual("49", fizzbuzz.ternary_ver(49))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(50))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(51))
        self.assertEqual("52", fizzbuzz.ternary_ver(52))
        self.assertEqual("53", fizzbuzz.ternary_ver(53))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(54))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(55))
        self.assertEqual("56", fizzbuzz.ternary_ver(56))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(57))
        self.assertEqual("58", fizzbuzz.ternary_ver(58))
        self.assertEqual("59", fizzbuzz.ternary_ver(59))
        self.assertEqual("FizzBuzz", fizzbuzz.ternary_ver(60))
        self.assertEqual("61", fizzbuzz.ternary_ver(61))
        self.assertEqual("62", fizzbuzz.ternary_ver(62))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(63))
        self.assertEqual("64", fizzbuzz.ternary_ver(64))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(65))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(66))
        self.assertEqual("67", fizzbuzz.ternary_ver(67))
        self.assertEqual("68", fizzbuzz.ternary_ver(68))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(69))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(70))
        self.assertEqual("71", fizzbuzz.ternary_ver(71))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(72))
        self.assertEqual("73", fizzbuzz.ternary_ver(73))
        self.assertEqual("74", fizzbuzz.ternary_ver(74))
        self.assertEqual("FizzBuzz", fizzbuzz.ternary_ver(75))
        self.assertEqual("76", fizzbuzz.ternary_ver(76))
        self.assertEqual("77", fizzbuzz.ternary_ver(77))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(78))
        self.assertEqual("79", fizzbuzz.ternary_ver(79))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(80))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(81))
        self.assertEqual("82", fizzbuzz.ternary_ver(82))
        self.assertEqual("83", fizzbuzz.ternary_ver(83))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(84))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(85))
        self.assertEqual("86", fizzbuzz.ternary_ver(86))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(87))
        self.assertEqual("88", fizzbuzz.ternary_ver(88))
        self.assertEqual("89", fizzbuzz.ternary_ver(89))
        self.assertEqual("FizzBuzz", fizzbuzz.ternary_ver(90))
        self.assertEqual("91", fizzbuzz.ternary_ver(91))
        self.assertEqual("92", fizzbuzz.ternary_ver(92))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(93))
        self.assertEqual("94", fizzbuzz.ternary_ver(94))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(95))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(96))
        self.assertEqual("97", fizzbuzz.ternary_ver(97))
        self.assertEqual("98", fizzbuzz.ternary_ver(98))
        self.assertEqual("Fizz", fizzbuzz.ternary_ver(99))
        self.assertEqual("Buzz", fizzbuzz.ternary_ver(100))

if __name__ == "__main__":
    unittest.main()
