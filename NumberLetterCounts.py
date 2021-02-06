def getNumWord(number):
    number = list(str(number))
    numWord = []
    teen = False
    for place in range(0, len(number)):
        digit = number[place]
        place = len(number) - place
        if place == 4:
            numWord.append("one")
            numWord.append("thousand")
        elif place == 3:
            if digit == "1":
                numWord.append("one")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "2":
                numWord.append("two")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "3":
                numWord.append("three")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "4":
                numWord.append("four")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "5":
                numWord.append("five")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "6":
                numWord.append("six")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "7":
                numWord.append("seven")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "8":
                numWord.append("eight")
                numWord.append("hundred")
                numWord.append("and")
            elif digit == "9":
                numWord.append("nine")
                numWord.append("hundred")
                numWord.append("and")
        elif place == 2:
            if digit == "1":
                teen = True
            elif digit == "2":
                numWord.append("twenty")
            elif digit == "3":
                numWord.append("thirty")
            elif digit == "4":
                numWord.append("forty")
            elif digit == "5":
                numWord.append("fifty")
            elif digit == "6":
                numWord.append("sixty")
            elif digit == "7":
                numWord.append("seventy")
            elif digit == "8":
                numWord.append("eighty")
            elif digit == "9":
                numWord.append("ninety")
        elif place == 1:
            if teen:
                if digit == "0":
                    numWord.append("ten")
                elif digit == "1":
                    numWord.append("eleven")
                elif digit == "2":
                    numWord.append("twelve")
                elif digit == "3":
                    numWord.append("thirteen")
                elif digit == "4":
                    numWord.append("fourteen")
                elif digit == "5":
                    numWord.append("fifteen")
                elif digit == "6":
                    numWord.append("sixteen")
                elif digit == "7":
                    numWord.append("seventeen")
                elif digit == "8":
                    numWord.append("eighteen")
                elif digit == "9":
                    numWord.append("nineteen")
            else:
                if digit == "1":
                    numWord.append("one")
                elif digit == "2":
                    numWord.append("two")
                elif digit == "3":
                    numWord.append("three")
                elif digit == "4":
                    numWord.append("four")
                elif digit == "5":
                    numWord.append("five")
                elif digit == "6":
                    numWord.append("six")
                elif digit == "7":
                    numWord.append("seven")
                elif digit == "8":
                    numWord.append("eight")
                elif digit == "9":
                    numWord.append("nine")
    if numWord[len(numWord)-1] == "and":
        numWord.remove("and")
    return "".join(numWord)

#print(getNumWord(int(input("Enter a number:  "))))

sum = 0
for x in range(1, 1001):
    sum += len(getNumWord(x))

print(sum)