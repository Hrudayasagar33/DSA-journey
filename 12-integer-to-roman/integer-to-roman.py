class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to their Roman numeral symbols in descending order
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_numeral = []
        
        # Greedily process each value-symbol pair
        for value, symbol in value_map:
            # Check how many times the value fits into the current number
            if num >= value:
                count = num // value
                roman_numeral.append(symbol * count)
                num %= value  # Update num to the remaining value
                
        return "".join(roman_numeral)
