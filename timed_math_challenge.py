def to_number(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0

    for i in range(len(roman) - 1):
        if roman_numerals[roman[i]] < roman_numerals[roman[i + 1]]:
            total -= roman_numerals[roman[i]]
        else:
            total += roman_numerals[roman[i]]

    total += roman_numerals[roman[-1]]  # Bu satır doğru konumda olmalıdır.
    return total

# Fonksiyonu kullanarak sonuçları alın
print(to_number('MMXI'))
print(to_number('XC'))
print(to_number('MCMVII'))
print(to_number('MCMXC'))
