import sys

def main(path):
    # Opening file
    with open(path) as f:
        lines = f.readlines()

    output = [] # def output list where every index is a new line

    # Remove beginning spaces and ending spaces to allow handling
    for line in range(len(lines)):
        lines[line] = lines[line].strip()
    #Blank comment

    for line in lines:

        """
        
        Essentially this code will find opening tags and closing tags and use whatever is within
        those tags as the code
        
        """
        if "<print>" in line:
            if "</print>" in line:
                outputstr = line[7: line.index("</print>")]
            else:
                outputstr = ""
                out = lines[lines.index(line): lines.index("</print>")]
                for i in range(len(out)):
                    if i == 0:
                        outputstr += out[i][7:]
                    else:
                        outputstr += out[i]
            output.append(f"print({outputstr})\n")

        """if "<input>" in line:
            if "</input>" in line:
                outputstr = line[7: line.index("</input>")]
            else:
                outputstr = ""
                out = lines[lines.index(line): lines.index("</input>")]
                for i in range(len(out)):
                    if i == 0:
                        outputstr += out[i][7:]
                    else:
                        outputstr += out[i]
            output.append(f"input({outputstr})\n")"""
        
        if "<var>" in line:
            if "<input>" in line:
                outputstr = line[5: line.index("</input>")]
                outputstr += ")"
                outputstr = outputstr.replace("<input>", "input(")
            elif "</var>" in line:
                outputstr = line[5: line.index("</var>")]
            else:
                outputstr = ""
                out = lines[lines.index(line): lines.index("</var>")]
                for i in range(len(out)):
                    if i == 0:
                        outputstr += out[i][5:]
                    else:
                        outputstr += out[i]
            output.append(f"{outputstr}\n")

        if "<if>" in line:
            if "</if>" in line:     # Handle when if statement is on one line
                firstbracket = 5
                secondbracket = line[firstbracket:].index(")") + firstbracket
                conditionstr = line[firstbracket: secondbracket]
                output.append(f"if {conditionstr}:\n")
                iftext = line[secondbracket + 1:]
                iftext = iftext.replace("</if>", "")
                output.append(f"    {iftext}")
            else:
                outputstr = ""
                out = lines[lines.index(line): lines.index("</if>")]
                for i in range(len(out)):
                    if i == 0:
                        outputstr += out[i][5:-1]
                    else:
                        outputstr += out[i]
                output.append(f"if {outputstr}:\n")



    with open(f"{path[:-4]}.py", "w+") as f:        # Output to the name of file.py
        f.writelines(output)

try:
    filename = sys.argv[1]
    main(filename)
except IndexError:
    #print("No file path given")            # Has to be commented out for testing
    main("test.boa")