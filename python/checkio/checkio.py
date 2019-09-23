# import re

# def checkio(pwd):
#     if len(pwd) <= 10:
#         return f'wrong len {len(pwd)}'
#     for i in pwd:
#         try:
#             int(i)
#             print(f'pass has number')
#         except:
#             print(f'{i} is not a number')
#             if i == str.upper(i):
#                 print(f'pass has upperr')
#             if i == str.lower(i):
#                 print(f'pass has lower')
#             if re.match("[a-zA-Z0-9]+", pwd):
#                 print(f'pass has asci')
#     return 0




import re

def checkio(data: str) -> bool:
    #print(bool(re.search("[A-Z]", data)))
    if bool(re.search("[a-z]", data)) and bool(re.search("[A-Z]", data)) and bool(re.search("[0-9]", data)):
                print(f'pass has asci')
                return True
    return False


print(checkio("ULFFunH8ni"))
