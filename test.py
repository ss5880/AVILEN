"""
このファイルに解答コードを書いてください
"""

def readFile():
    file = open('input.txt', "r")
    data = []
    num_row = 0
    for row in file:
        num_row += 1

    file = open('input.txt', "r")
    num_count = 0
    for line in file:
        num_count += 1
        if num_count != num_row:
            s = line.split(':')[0]
            i = line.split(':')[1].strip('\n')
            row = [int(s), i]
            data.append(row)

        else:
            M_num = int(line)

    data.sort(key=lambda data: data[0])

    output_string = ""
    for line in data:
        if M_num % line[0] == 0:
            for character in line[1:]:
                output_string += character

    print(output_string)

    if output_string == "":
        print(M_num)

def main():
    readFile()

if __name__ == '__main__':
    main()
