stringElem = "123456789ABCDEFGHIJKLMNPQRSTUVWXYSabcdefghijkmnopqrstuvwxyz@$&"
def encode(id, string):
    if id ==0:
        return print(string[0])
    arr = []
    base = len(string)
    while id:
        id = id//base
        rem = id%base
        # print(id, rem)
        arr.append(string[rem])
        # print(arr)
        arr.reverse()
        out = "".join(arr)
        # print(out)
    return out
