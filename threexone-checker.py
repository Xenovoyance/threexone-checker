import time

def threexone(input=1):
    steps = 1
    nextnum = next_input(input)
    print(nextnum)
    while nextnum != 1:
        nextnum = next_input(nextnum)
        print(nextnum)
        steps += 1
        continue
    return steps

def next_input(input):
    if (input % 2) == 0: 
        return int(input / 2)
    else: 
        return int((3 * input) + 1)

if __name__ == "__main__":
    start_time = time.time()
    integer_to_check = 100
    print("3X+1 of " + str(integer_to_check) + " executed in " + str(threexone(integer_to_check)) + " steps, and in " + str((time.time() - start_time) * 1000) + " ms")
