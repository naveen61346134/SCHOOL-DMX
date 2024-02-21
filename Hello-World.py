from time import sleep
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"
mainStr = "Hello World"
result = ""

for i in range(len(mainStr)):
    strChar = mainStr[i]
    breaker = False
    for char in list(chars):
        if strChar == char:
            result += char
            print(result)
            sleep(0.01)
        elif str(strChar).isspace():
            result += " "
            break
        if result == mainStr:
            breaker = True
            break
        else:
            print(f"{result}{char}")
            sleep(0.01)

    if breaker is True:
        break
