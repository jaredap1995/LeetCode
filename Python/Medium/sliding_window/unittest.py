import unittest
from longest_substring_without_repeating_charachters import Solution

class TestSolution(unittest):
    def setUp(self):
        self.solution = Solution()
    
    def test_longest_string(self):
        # Test case where the input string is empty
        self.assertEqual(self.solution.longest_string(''), 0)
        
        # Test case where the input string has only one character
        self.assertEqual(self.solution.longest_string('a'), 1)
        
        # Test case where the input string has no repeating characters
        self.assertEqual(self.solution.longest_string('abcdefg'), 7)
        
        # Test case where the input string has repeating characters
        self.assertEqual(self.solution.longest_string('abcabcbb'), 3)
        
        # Test case where the input string has repeating characters at the end
        self.assertEqual(self.solution.longest_string('pwwkew'), 3)
        
        # Test case where the input string has repeating characters at the beginning
        self.assertEqual(self.solution.longest_string('bbbbb'), 1)
        
        # Test case where the input string has repeating characters throughout
        self.assertEqual(self.solution.longest_string('abcbde'), 4)
        
if __name__ == '__main__':
    unittest.main()

