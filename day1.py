# Day 1

def part1(input):
    base = 0
    count = 0
    with open(input) as filename:
        for f in filename:
            if int(f) > base:
                count += 1
            base = int(f)
    print(count-1)

def part2(input):
    base = 0
    count = 0
    data = []
    with open(input) as filename:
        for f in filename:
            data.append(f)     
    
    for i in range(0, len(data)-2):
        window = int(data[i]) + int(data[i+1]) + int(data[i+2])
        if window > base:
            count += 1
        base = window
    print(count-1)
        
part1('inputs/day1.txt')
part2('inputs/day1.txt')
