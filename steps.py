size=5
for row in range(size):
    star="";
    for col in range(size):
        if col>row:
            star = star + " "
        else:
            star = star + "*"
    print(star)

