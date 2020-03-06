def main():
    msg = 'hello world!'

    vowels = ['a','e','i','o','u']

    msg = list(msg)
    msg_copy = msg.copy()
    idx = 0
    for i in range(len(msg)):
        if msg[i] in vowels:
            msg_copy.pop(idx)
            idx -= 1
        idx += 1

    msg = ''.join(msg_copy)
    msg = msg.upper()

    print(msg)
    

main()
