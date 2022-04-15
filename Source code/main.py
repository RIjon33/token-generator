import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

print('''
████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

        ██████╗░██╗░░░██╗  ██████╗░██╗░░░░░██╗░█████╗░███╗░░██╗██████╗
        ██╔══██╗╚██╗░██╔╝  ██╔══██╗██║░░░░░██║██╔══██╗████╗░██║╚════██╗
        ██████╦╝░╚████╔╝░  ██████╔╝██║░░░░░██║██║░░██║██╔██╗██║░█████╔╝
        ██╔══██╗░░╚██╔╝░░  ██╔══██╗██║██╗░░██║██║░░██║██║╚████║░╚═══██╗
        ██████╦╝░░░██║░░░  ██║░░██║██║╚█████╔╝╚█████╔╝██║░╚███║██████╔╝
        ╚═════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝

----------------------------
  1 = Generate
  2 = Exit
----------------------------
''')

choice = int(input("Choice = "))

if choice == 1:
    print('''
    ----------------------------
    How Much You Wanna Generate?
    ----------------------------
    
    ----------------------------
    1 = 10
    2 = 50
    3 = 100
    4 = Custom
    ----------------------------
    ''')
    choice1 = int(input("Choice = "))

    if choice1 == 1:
        for i in range(10):
            first = ''.join((random.choice(chars) for i in range(24)))
            second = ''.join((random.choice(chars) for i in range(6)))
            third = ''.join((random.choice(chars) for i in range(27)))

            result = first + "." + second + "." + third

            print(result + "\n")
        print("Take it Thanks me Later")

    if choice1 == 2:
        for i in range(50):
            first = ''.join((random.choice(chars) for i in range(24)))
            second = ''.join((random.choice(chars) for i in range(6)))
            third = ''.join((random.choice(chars) for i in range(27)))

            result = first + "." + second + "." + third

            print(result + "\n")
        print("Take it Thanks me Later")

    if choice1 == 3:
        for i in range(100):
            first = ''.join((random.choice(chars) for i in range(24)))
            second = ''.join((random.choice(chars) for i in range(6)))
            third = ''.join((random.choice(chars) for i in range(27)))

            result = first + "." + second + "." + third

            print(result + "\n")
        print("Take it Thanks me Later")

    if choice1 == 4:
        print('''
        ----------------------------
        Amount:
        ----------------------------''')

        choice2 = int(input("Amount = "))

        for i in range(choice2):
            first = ''.join((random.choice(chars) for i in range(24)))
            second = ''.join((random.choice(chars) for i in range(6)))
            third = ''.join((random.choice(chars) for i in range(27)))

            result = first + "." + second + "." + third

            print(result + "\n")
        print("Take it! Thanks me Later")

    input("Press Enter to Exit...")

