# Day 1

def part1(): 
    base = 0
    count = 0
    with open('inputs/day1.txt') as filename:
        for line in filename:
            aux = int(line)
            if aux > base:
                count += 1
            base = aux
    return count-1

print(part1())

