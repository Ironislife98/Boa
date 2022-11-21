import boa

while True:
    text = input("boa >> ")
    result, error = boa.run(text)

    if error:
        print(error.string())
    else:
        print(result)