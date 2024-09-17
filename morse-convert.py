
morse_code = {
    'a': ".-",'b': "-...",'c': "-.-.",
    'd': "-..",'e': ".",'f': "..-.",
    'g': "--.",'h': "....",'i': "..",
    'j': ".---",'k': "-.-",'l': ".-..",
    'm': "--",'n': "-.",'o': "---",
    'p': ".--.",'q': "--.-",'r': ".-.",
    's': "...",'t': "-",'u': "..-",
    'v': "...-",'w': ".--",'x': "-..-",
    'y': "-.--",'z': "--.."
}

while True:
    phrase = input("Enter a Phrase: ")
    p2 = list(str(phrase))
    while ' ' in p2:
        p2.remove(' ')
    result = [morse_code[x] for x in p2]
    print(' '.join(result))
