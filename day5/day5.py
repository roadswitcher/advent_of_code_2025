"""Day 5, AOC 2025"""


def read_data(filename:str):
    ranges = []
    ids = []

    filecontents = (line.rstrip('\r\n') for line in open(filename))
    for line in filecontents:
        if '-' in line:
            low, high = line.split('-')
            ranges.append([int(low), int(high)])
        elif line != '':
            ids.append(int(line))

    print(ranges)
    print(ids)



if __name__ == '__main__':
    read_data('test_input.txt')