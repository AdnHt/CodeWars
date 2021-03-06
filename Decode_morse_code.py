# 6 kyu / Decode the Morse code
# Details
#   https://www.codewars.com/kata/decode-the-morse-code


def decode_morse(morse_code):
    MORSE_CODE = {
        '-.-.--': '!', '.-..-.': '"', '...-..-': '$', '.-...': '&',
        '.----.': '\'', '-.--.': '', '-.--.-': ',', '.-.-.': '+',
        '--..--': ':', '-....-': '-', '.-.-.-': '.', '-..-.': '/',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', '---...': ':', '-.-.-.': ';',
        '-...-': '=', '..--..': '?', '.--.-.': '@', '.-': 'A',
        '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
        '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
        '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
        '.-.': 'R', '...': 'S', '...---...': 'SOS', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '..--.-': '_'}

    return ' '.join(''.join(MORSE_CODE[a] for a in word.split())
                    for word in morse_code.split('   ')).strip()
