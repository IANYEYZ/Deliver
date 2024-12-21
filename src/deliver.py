import sys

pos = 0
sz = 2560
package = 0
stacks = [[] for _ in range(sz)]
notes = {}
codeFile = {}
routineFile = {}
def move(pos, distance):
    pos += distance
    pos = pos % sz
    return pos

def takePackage(package, pos):
    if len(stacks[pos]) > 0:
        package = stacks[pos].pop()
    return package

def match(words, str):
    str = str.split()
    if words == str:
        return True
    else:
        return False

def str2int(s):
    if s == "TOP":
        return stacks[pos][-1]
    elif s == "PACKAGE":
        return package
    elif s[0] == '-':
        return -int(s[1:])
    else:
        return int(s)

def loadAndRunCode(filename):
    with open(filename, "r") as file:
        code = file.read()
        code_lines = code.split("\n")
        codeFile[filename] = code_lines
        runCode(code_lines, 0, len(code_lines) - 1, filename)

def findMatchingEnd(code, current_line):
    nested_if_count = 1
    for i in range(current_line + 1, len(code)):
        if code[i].startswith("If"):
            nested_if_count += 1
        elif code[i] == "End":
            nested_if_count -= 1
            if nested_if_count == 0:
                return i

def runCode(code, current_line, ed, filename):
    if current_line > ed:
        return
    # print(code[current_line])
    words = code[current_line].split()
    # print(words)
    global pos, package, stacks
    # print(pos, package, current_line, stacks[pos])
    if len(words) == 0:
        runCode(code, current_line + 1, ed, filename)
        return
    while words[0] == " " or words[0] == "\t":
        words = words[1:]
    if words[0] == "Move":
        distance = str2int(words[1])
        pos = move(pos, distance)
        runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Take":
        if match(words, "Take the top package from the pile"):
            package = takePackage(package, pos)
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Throw":
        if match(words, "Throw the top package from the pile away"):
            stacks[pos].pop()
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Let":
        if match(words[:len(words) - 1], "Let the package to be"):
            package = str2int(words[-1])
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Put":
        if match(words, "Put the package onto the pile"):
            # print("Here!")
            stacks[pos].append(package)
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Add":
        if match(words, "Add the package to the pile"):
            stacks[pos][-1] += package
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Merge":
        if match(words, "Merge the package to the pile"):
            stacks[pos][-1] *= package
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Divide":
        if match(words, "Divide the package to the pile"):
            stacks[pos][-1] //= package
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Takeaway":
        if match(words, "Takeaway the package from the pile"):
            stacks[pos][-1] -= package
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "If":
        if match(words, "If the pile has no package"):
            if len(stacks[pos]) == 0:
                runCode(code, current_line + 1, ed, filename)
            else:
                runCode(code, findMatchingEnd(code, current_line) + 1, ed, filename)
        elif match(words, "If the pile has packages"):
            if len(stacks[pos]) > 0:
                runCode(code, current_line + 1, ed, filename)
            else:
                runCode(code, findMatchingEnd(code, current_line) + 1, ed, filename)
        elif match(words[:len(words) - 1], "If the pile's top package is"):
            # print("Here!")
            if stacks[pos][-1] == str2int(words[-1]):
                runCode(code, current_line + 1, ed, filename)
            else:
                runCode(code, findMatchingEnd(code, current_line) + 1, ed, filename)
        elif match(words[:len(words) - 1], "If the pile's top package is not"):
            if stacks[pos][-1] != str2int(words[-1]):
                runCode(code, current_line + 1, ed, filename)
            else:
                runCode(code, findMatchingEnd(code, current_line) + 1, ed, filename)
    elif words[0] == "End":
        runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Report":
        if match(words, "Report package id"):
            print(package, end="")
            runCode(code, current_line + 1, ed, filename)
        if match(words, "Report package name"):
            print(chr(package), end="")
            runCode(code, current_line + 1, ed, filename)
    elif words[0] == "Routine":
        name = words[1][:len(words[1]) - 1]
        notes[name] = [current_line + 1, -1]
        notes[name][1] = findMatchingEnd(code, notes[name][0])
        routineFile[name] = filename
        runCode(code, notes[name][1] + 1, ed, filename)
    elif words[0] == "Follow":
        if match(words[:len(words) - 1], "Follow the routine"):
            name = words[3]
            # print(notes[name][0], notes[name][1])
            runCode(codeFile[routineFile[name]], notes[name][0], notes[name][1], routineFile[name])
            runCode(code, current_line + 1, ed, filename)
        if match(words[:len(words) - 1], "Follow the circuit"):
            name = words[3]
            loadAndRunCode(name)
            runCode(code, current_line + 1, ed, filename)

def main():
    if len(sys.argv) != 2:
        print("Usage: deliver <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    loadAndRunCode(filename)

if __name__ == "__main__":
    main()
