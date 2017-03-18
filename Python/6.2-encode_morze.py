__author__ = 'minin'

morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : " "
}
modulation = {
    "." : "^_",
    "-" : "^^^_",
    " " : "__"
#    " " : "_______"
}
def encode_morze(text):
    encoded_text = ''
    modulated_text = ''
    for letter in text.upper():
        try:
            encoded_text += morse_code[letter] + " "
        except:
            encoded_text = encoded_text
    encoded_text = encoded_text[:len(encoded_text) - 1]

    for letter in encoded_text:
        modulated_text += modulation[letter]
    modulated_text = modulated_text[:len(modulated_text) - 1]

    return modulated_text

print encode_morze('Morze code')
print encode_morze('Prometheus')
print encode_morze('SOS')
print encode_morze('1')

#^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^
#^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^
#^_^_^___^^^_^^^_^^^___^_^_^
