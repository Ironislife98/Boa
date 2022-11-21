import boa

while True:
    text = input("boa >> ")
    result, error = boa.run("<stdin>", text)

    if error:
        print(error.string())
    else:
        print(result)