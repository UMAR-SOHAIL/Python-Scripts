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
while True:
    print("please distinguish your moarse code by a comma \",\" and don't add spaces between comma e.g .,.. not ., ..")
    user = input("enter your moarse code: ")

    split = user.split(",")


    def space_remover(x):
        for i in x:
            for l in i:
                #if " " in l:
                while " " in l:
                    l = i.replace(" ","")
                    x[x.index(i)] = l
        return x

    s_rem = space_remover(split)
    
    g=""
    for morse in s_rem:
        f = mc[morse]
        g+=f


    print(g)

    ex = str(input("press q to quit or any other key to continue: "))

    if ex == "q" or ex ==" Q":
        break
    else:
        pass

