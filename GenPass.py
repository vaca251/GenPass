try:
    import random, argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--length', '-l', type=int, help='Passwords length', required=True)
    parser.add_argument('--amount', '-a', type=int, help='Number of passwords', required=True)
    parser.add_argument('--file', '-f', type=str, help='File for saving all passwords', required=False, default="output.txt")
    parser.add_argument('--chars', '-c', type=str, help='Password characters', required=False, default="1234567890+-*_qwertyuiopasdfghjkl;'zxcvbnm,.!@#$%^&*QWERTYUIOPASDFGHJKLZXCVBNM")
    args = parser.parse_args()
    logotip = [
        " ██████╗ ███████╗███╗   ██╗██████╗  █████╗ ███████╗███████╗",
        "██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝",
        "██║  ███╗█████╗  ██╔██╗ ██║██████╔╝███████║███████╗███████╗",
        "██║   ██║██╔══╝  ██║╚██╗██║██╔═══╝ ██╔══██║╚════██║╚════██║",
        "╚██████╔╝███████╗██║ ╚████║██║     ██║  ██║███████║███████║",
        " ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝",
        "                        By Vaca251                         ",
    ]
    for x in logotip:
        print(x)
    print("[Info] Collecting information...")
    chars = args.chars
    num = args.amount
    leng = args.length
    file = args.file

    while True:
        userinput = input(f"[Warning] {num} passwords with length {leng} will be generated into the {file} file. Сontinue? [y/n]")
        if userinput == "y":
            print("[Info] Generation...")
            for b in range(num):
                password = ""
                for i in range(leng):
                    password += random.choice(chars)
                with open(file, 'a') as file2:
                    file2.write(f"{password}\n")
            print("Done")
            exit()
        elif userinput == "n":
            exit()
        else:
            print("[Error] Enter y or n")       
except Exception as e:
    print(f"[Error] {e}")
    exit()