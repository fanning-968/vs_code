import time 

def main():

    with open('1/橡胶树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('1/橡胶树.txt', 'r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
        print()

    with open('1/橡胶树.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()