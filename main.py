from PIL import Image

colors = {
    'A': (225,0,0), #ROOD
    'C': (0,225,0), #GROEN
    'G': (0,0,225), #BLAUW
    'T': (0,0,0)    #ZWART
}

def decode(char): #Vertaal character uit het alfabet naar een drie letterige code als in DNA
    if char== '0':
        return ['A','A','A']
    if char== '1':
        return ['A','A','C']
    if char== '2':
        return ['A','A','G']
    if char== '3':
        return ['A','A','T']
    if char== '4':
        return ['A','C','A']
    if char== '5':
        return ['A','C','C']
    if char== '6':
        return ['A','C','G']
    if char== '7':
        return ['A','C','T']
    if char== '8':
        return ['A','G','A']
    if char== '9':
        return ['A','G','C']
    if char== 'a':
        return ['A','G','G']
    if char== 'b':
        return ['A','G','T']
    if char== 'c':
        return ['A','T','A']
    if char== 'd':
        return ['A','T','C']
    if char== 'e':
        return ['A','T','G']
    if char== 'f':
        return ['A','T','T']
    if char== 'g':
        return ['C','A','A']
    if char== 'h':
        return ['C','A','C']
    if char== 'i':
        return ['C','A','G']
    if char== 'j':
        return ['C','A','T']
    if char== 'k':
        return ['C','C','A']
    if char== 'l':
        return ['C','C','C']
    if char== 'm':
        return ['C','C','G']
    if char== 'n':
        return ['C','C','T']
    if char== 'o':
        return ['C','G','A']
    if char== 'p':
        return ['C','G','C']
    if char== 'q':
        return ['C','G','G']
    if char== 'r':
        return ['C','G','T']
    if char== 's':
        return ['C','T','A']
    if char== 't':
        return ['C','T','C']
    if char== 'u':
        return ['C','T','G']
    if char== 'v':
        return ['C','T','T']
    if char== 'w':
        return ['G','A','A']
    if char== 'x':
        return ['G','A','C']
    if char== 'y':
        return ['G','A','G']
    if char== 'z':
        return ['G','A','T']
    if char== 'A':
        return ['G','C','A']
    if char== 'B':
        return ['G','C','C']
    if char== 'C':
        return ['G','C','G']
    if char== 'D':
        return ['G','C','T']
    if char== 'E':
        return ['G','G','A']
    if char== 'F':
        return ['G','G','C']
    if char== 'G':
        return ['G','G','G']
    if char== 'H':
        return ['G','G','T']
    if char== 'I':
        return ['G','T','A']
    if char== 'J':
        return ['G','T','C']
    if char== 'K':
        return ['G','T','G']
    if char== 'L':
        return ['G','T','T']
    if char== 'M':
        return ['T','A','A']
    if char== 'N':
        return ['T','A','C']
    if char== 'O':
        return ['T','A','G']
    if char== 'P':
        return ['T','A','T']
    if char== 'Q':
        return ['T','C','A']
    if char== 'R':
        return ['T','C','C']
    if char== 'S':
        return ['T','C','G']
    if char== 'T':
        return ['T','C','T']
    if char== 'U':
        return ['T','G','A']
    if char== 'V':
        return ['T','G','C']
    if char== 'W':
        return ['T','G','G']
    if char== 'X':
        return ['T','G','T']
    if char== 'Y':
        return ['T','T','A']
    if char== 'Z':
        return ['T','T','C']
    if char== '.':
        return ['T','T','G']
    if char== ' ':
        return ['T','T','T']

def addLetter(array, char): #Voegt letter code (uit decode) toe aan de lijst
    for letter in decode(char):
        array.append(letter)

def translateText(array, input): #Voegt iedere letter code uit input toe aan de lijst, met wat chatches voor special cases
    for letter in input:
        if letter != '\n':
            if letter == ',':
                letter == ' '
            addLetter(array , letter)

def createImage(x,y, array): #Zorgt voor iedere code letter in de gecoderde text de juiste kleur toe volgens colors en maakt een plaatje
    img = Image.new('RGB', (x, y))
    for i in range(x):
        for j in range(y):
            if i*y + j < len(array): 
                color = array[i*y + j]
                img.putpixel((j,i), colors[color])
    img.save('output.png')

    return img

text = """Chaos is infromation. So information is chaos. Our DNA is Chaos. 
Every physics thoery, filosofical thought or great poets words can be discribed by chaos"""
result = []

translateText(result, text)
print(result)

wallpaper = createImage(100,100,result)
wallpaper.show()
