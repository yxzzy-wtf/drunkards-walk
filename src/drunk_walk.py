import random

max = 11
min = 1

def drunk(start, chance):
    i = 0
    at = start

    while i < 100000:
        if at == max:
            return i

        up = random.randint(0, 10) >= chance

        if up or at == min:
            at += 1
        else: 
            at -= 1
        i += 1
    return -1

# run simulation for each chance
for x in range(0, 10):
    success = 0
    fail = 0
    average = 0
    for y in range(0, 1000):
        steps = drunk(8, x)
        if steps != -1:
            average += steps
            success += 1
        else:
            fail +=1
    print("1000 with " + str(x) + "/10 chance to decrease: succeed=" + str(success) + " fail=" + str(fail) + " avg=" + ("N/A" if success == 0 else str(average / success)))
