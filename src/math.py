# math functions
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 0
    return x / y

def subtract(x, y):
    return x - y;

if __name__ == '__main__':
    print(add(1, 2))
    print(multiply(1, 2))
    print(divide(1, 0))
    print(subtract(1, 2))