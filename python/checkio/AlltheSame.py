def all_the_same(list):
    if len(list) <= 1:
        return True
    for i in list:
        j = 0
        if  i != list[j+1]:
            j = j+1
            return False
    return True
