import unittest

"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

def solution(arg1 : str, arg2: str):
    return arg1.endswith(arg2)


"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs")
)

class TestSolution(unittest.TestCase):
    def test_true_cases(self):
        for string, ending in fixed_tests_True:
            with self.subTest(arg1=string, arg2=ending):
                self.assertTrue(solution(string, ending))

    def test_false_cases(self):
        for string, ending in fixed_tests_False:
            with self.subTest(arg1=string, arg2=ending):
                self.assertFalse(solution(string, ending))

if __name__ == '__main__':
    unittest.main()