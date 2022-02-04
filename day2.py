# Day 2

def part1(input):
    x = 0
    y = 0
    with open(input) as filename:
        for line in filename:
            command = line.split(' ')[0]
            value = int(line.split(' ')[1])
            if command == 'forward':
                x = x + value
            elif command == 'down':
                y = y + value
            elif command == 'up':
                y = y - value
        if y < 0:
            y = 0

    print(x*y)

def part2(input):
    x = 0
    y = 0
    aim = 0
    with open(input) as filename:
        for line in filename:
            command = line.split(' ')[0]
            value = int(line.split(' ')[1])
            if command == 'forward':
                x = x + value
                y = y + aim * value
            elif command == 'down':
                aim = aim + value
            elif command == 'up':
                aim = aim - value
        if y < 0:
            y = 0

    print(x*y)
        
part1('inputs/day2.txt')
part2('inputs/day2.txt')   

    
