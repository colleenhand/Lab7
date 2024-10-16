#The Authors' names are: Colleen and Margaret
def letter_o(word):
    total = 0
    for x in word:
        if x == "o":
            total = total + 1
    print(total)

letter_o("bonobos")
