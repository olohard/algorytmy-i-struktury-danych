def sprawdz(expr):
    stack = []

    for char in expr:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False

            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False

    if stack:
        return False
    return True

if __name__ == "__main__":
    print("Podaj nawiasy: ")
    txt = ''
    a = input()

    txt += a

    if sprawdz(txt):
        print("Balanced")
    else:
        print("Not Balanced")