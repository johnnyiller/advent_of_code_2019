def add(a, b):
    return a + b

def mult(a, b):
    return a * b

fmap = { 1: add, 2: mult }

input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]

FROM=0
TO=len(input) - 1 
STEP=4
TARGET=19690720

def run(noun, verb):
    
    _input = list(input)

    HALT = 99

    _input[1] = noun
    _input[2] = verb

    for i in range(FROM, TO, STEP):
        opcode = _input[i]
        if opcode == HALT:
            return _input[0]
        op = fmap[opcode]
        a = _input[_input[i + 1]]
        b = _input[_input[i + 2]]
        value = op(a, b)
        location = _input[i + 3]
        _input[location] = value

def search():
    for i in range(FROM, TO):
        for j in range(FROM, TO):
            if run(i,j) == TARGET:
                return 100 * i + j

print(search())
