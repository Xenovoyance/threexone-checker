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
    #print("Part 1: " + part_one() + " executed in " + str(time.time() - start_time) + " seconds")
    #print("Part 2: " + part_two() + " executed in " + str(time.time() - start_time) + " seconds")

    txo = 9723098723409283740239847230498972309872340928374023984723049897230987234092837402398472304989723098723409283740239847230498
    print("3X+1 of " + str(txo) + " executed in " + str(threexone(txo)) + " steps, and in " + str((time.time() - start_time) * 1000) + " ms")
