class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        empty_list = [] 

        for i in s:
            for x, z in roman_numerals.items():
                if i == x:
                    empty_list.append(z)


        result = 0
        for i in range(len(empty_list)):
            current_value = empty_list[i]

            if i + 1 < len(empty_list) and current_value < empty_list[i + 1]:
                result -= current_value
            else:
                result += current_value

        return result