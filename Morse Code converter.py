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

    g=""
    for morse in split:
        f = mc[morse]
        g+=f


    print(g)

    ex = str(input("press q to quit or any other key to continue: "))

    if ex == "q" or ex ==" Q":
        break
    else:
        pass
