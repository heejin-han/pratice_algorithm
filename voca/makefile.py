# ??
FLAG = ""

# ????
out_file = open('vocabulary.txt', 'w')

while FLAG != "q":
    voca = input("?? ??? ?????: ")

    if voca == "q":
        exit()

    korean = input("??? ?? ?????: ")
    out_file.write("%s: %s\n" % (voca, korean))

out_file.close()

