def split_and_join(line):
    temp = []
    temp = line.split(" ")
    line = '-'.join(temp)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)