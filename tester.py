x = ["<print>'HelloWorld'", "</print>"]


for line in x:
    if "<print>" in line:
        if "</print>" in line:
            out = line[7: line.index("</print>")]
        else:
            output = ""
            out = x[x.index(line): x.index("</print>")]
            for i in range(len(out)):
                if i == 0:
                    output += out[i][7:]
                else:
                    output += out[i]
            print(output)

for line in x:
    if "<print>" in line:
        if "</print>" in line:
            out = line
            out = out.replace("<print>", "print(")
            out = out.replace("</print>", ")")
            print(out)
        else:
            output = ""
            out = x[x.index(line): x.index("</print>")]
            for i in out:
                output += i
            print(output)