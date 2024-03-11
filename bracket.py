def bracket(expr):
    stack=[]

    for char in expr:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            currentChar=stack.pop()
            if currentChar=="(":
                if char!=")":
                    return False
            if currentChar=="[":
                if char!="]":
                    return False
            if currentChar=="}":
                if char!="}":
                    return False
    if stack:
        return False
    return True

if __name__=="__main__":
    expr=(input("Enter the expression = "))
    if bracket(expr):
        print("balanced")
    else:
        print("not balanced")