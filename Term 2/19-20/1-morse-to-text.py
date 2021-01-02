def morse_to_text(string):
    words = string.split('   ')
    translate = ''
    for word in words:
        for character in word.split():
            translate += morse[character]
        translate += ' '
    return translate

def text_to_morse(string):
    translate = ''
    for character in string:
        translate += alphabet[character.upper()] + ' '
    return translate


alphabet = { 
    'A':'.-','B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
    'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
    'Y':'-.--', 'Z':'--..', ' ': ' '}

morse = { 
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    ' ':' '}

m = input('Enter mourse code: ')
text = morse_to_text(m)
print(text)
