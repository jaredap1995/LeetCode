class Solution(object):
    def partition(digits):
        if not digits:
            return []

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack (str_combo, next_digits):
            if len(next_digits)==0:
                result.append(str_combo)
                return

            letters = keyboard[next_digits[0]]

            for letter in letters:
                backtrack(str_combo+letter, next_digits[1:])
            
        backtrack("", digits)
        return result


