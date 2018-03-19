"""
whitespaces have been removed from this code
MADE BY UMAR SOHAIL
"""
while True:
    rel = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Choose from 2-36 base")
    base_input = int(input("enter any base between from 2 to 36: "))
    print()
    number_input = int(input("enter number: "))
    tpm = number_input
    try:
        int_base = int(base_input)
    except ValueError:
        raise print("do a valid operation")
    r = ""
    assert base_input < 36
    while (tpm // base_input) > 0: 
        r = rel[tpm % base_input] + r
        tpm = tpm // base_input
    r = rel[tpm] + r
    print()
    print("%s is converted number by base %s" % (r, base_input))
    print()
    g = input("press 'q' to exit or any key to continue")
    if g == "q" or g == "Q":
        break
    else:
        pass
