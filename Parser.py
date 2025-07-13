import sys

input_str = sys.stdin.readline().strip()
i = 0  
output = []  

def peek():
    if i < len(input_str):
        return input_str[i]
    return None  

def consume(expected):
    global i
    if peek() == expected:
        i += 1
    else:
        raise Exception("Unexpected character: expected '" + expected + "', found '" + str(peek()) + "'")

def S():
    output.append('S')
    if peek() == 'a':
        consume('a')
        A()
        B()
    elif peek() == 'b':
        consume('b')
        B()
        A()
    else:
        raise Exception("Error in S")

def A():
    output.append('A')
    if peek() == 'b':
        consume('b')
        C()
    elif peek() == 'a':
        consume('a')
    else:
        raise Exception("Error in A")

def B():
    output.append('B')  
    if peek() == 'c':
        if i + 1 < len(input_str) and input_str[i + 1] == 'c':
            consume('c')
            consume('c')
            S()
            consume('b')
            consume('c')

def C():
    output.append('C')
    A()
    A()

def run():
    try:
        S()
        if i == len(input_str):
            print(''.join(output))
            print("YES")
        else:
            print(''.join(output))
            print("NO")
    except Exception:
        print(''.join(output))
        print("NO")

run()
