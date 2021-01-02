morse = { 
    'A':'.-','B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
    'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
    'Y':'-.--', 'Z':'--..', ' ': ' '}

text = input('Enter your text: ')
translate = ''
for character in text:
    translate += morse[character.upper()] + ' '
print(translate)