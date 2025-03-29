def addition(a, b):
    return a + b

# Testing here:

def testing():
    a = 1
    b = 2
    res = 3
    if addition(a, b) == res:
        return "Passed"
    else:
        return "Failed"

result = testing()
print(result)