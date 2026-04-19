l = []

while True:
    c = int(input('''
     1. Push Elements
     2. Pop Elements
     3. Peek Elements
     4. Display Elements
     5. Exit
     '''))

    if c == 1:
        n = input('Enter the element to push: ')
        l.append(n)
        print(l)

    elif c == 2:
        if len(l) == 0:
            print('Stack is empty')
        else:
            p = l.pop()
            print(p)
            print(l)

    elif c == 3:
        if len(l) == 0:
            print('Stack is empty')
        else:
            print("Last Stack Value:", l[-1])

    elif c == 4:
        print("Display Elements:", l)

    elif c == 5:
        print('Exit')
        break

    else:
        print('Invalid Choice')