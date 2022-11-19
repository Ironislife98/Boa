import sys

def main(path):
    # Opening file
    with open(path) as f:
        lines = f.readlines()

    output = [] # def output list where every index is a new line

    # Remove beginning spaces and ending spaces to allow handling
    for line in range(len(lines)):
        lines[line] = lines[line].strip()

    for line in lines:  # Iterate over all lines in file
        
        if line[0:6] == "write(":       # write should always be on its own line
            searchstart = 6
            offset = 0
            print(line[searchstart:])
            if "var(" in line[searchstart:]:
                endbracket = line[searchstart:].index(")")
                searchstart = endbracket + searchstart
                offset = 1


            endbracket = line[searchstart:].index(")")
            output.append(f"print({line[6:endbracket + 6]})\n")# pad with 6 chars because starting at 6 chars
        
        
        if line[0:3] == "new":
            searchstart = 4
            if line[searchstart:8] == "var(":
                searchstart = 8
                offset = 0

                if "input(" in line[searchstart:]:
                    endbracket = line[searchstart:].index(")")
                    searchstart = endbracket + searchstart
                    offset = 1

                endbracket = line[searchstart:].index(")")
                value = line[8:endbracket + searchstart + offset]

                name = line[endbracket + searchstart + 4 + offset: ]
                output.append(f"{name} = {value}\n")

    with open(f"{path[:-4]}.py", "w+") as f:        # Output to the name of file.py
        f.writelines(output)

try:
    filename = sys.argv[1]
    main(filename)
except IndexError:
    #print("No file path given")            # Has to be commented out for testing
    main("test.boa")