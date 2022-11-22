import boa

while True:
    text = input("boa >> ")
    result, error1 =  boa.run("<stdin>", text)

    if error1:
        print(error1.string())
    else:
        print(result)