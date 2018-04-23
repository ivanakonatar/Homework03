
def Max(list):

    if len(list) == 1:
        return list[0]

    else:
        return max(list[0],Max(list[1:]))


lista=[1,2,33]
print(Max(lista))











