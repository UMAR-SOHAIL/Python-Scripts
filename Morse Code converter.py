"""
MADE BY UMAR SOHAIL
STILL UNDER DEVELOPMENT
"""


mc = {
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z",
}

alpha = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
}
while True:
    print("please distinguish your morse code or word by spaces by spaces more than one space can also work")
    user = str(input("enter your moarse code: "))
    split = user.split(" ")

    def space_remover(li):
        while '' in li:
            li.remove('')
        return li

    def morse_alpha(o):
        g=""
        for morse in o:
            f = mc[morse]
            g+=f
        return g

    def alpha_morse(q):
        n = ""
        for bet in q:
            p = alpha[bet]
            n += " " + p
        return n


    if split[0] in mc:
        print (morse_alpha(space_remover(split)))

    else:
        print (alpha_morse(space_remover(split)))


    ex = str(input("press q to quit or any other key to continue: "))

    if ex == "q" or ex ==" Q":
        break
    else:
        pass
