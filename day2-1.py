input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]

TWELVE = 12
TWO = 2
HALT = 99

input[1] = TWELVE
input[2] = TWO




FROM=0
TO=len(input)-1
STEP=4


def add(a, b):
    return a + b

def mult(a, b):
    return a * b

fmap = { 1: add, 2: mult }


def run():
    for i in range(FROM, TO, STEP):
        opcode = input[i]
        if opcode == HALT:
            return
        op = fmap[opcode]
        a = input[input[i + 1]]
        b = input[input[i + 2]]
        value = op(a, b)
        location = input[i + 3]
        input[location] = value

run()
print(input[0])

        
    #print(input[i])


