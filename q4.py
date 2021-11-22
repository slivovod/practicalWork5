list_1 = input().split()
list_2 = input().split()
common_elements = set(list_1) & set(list_2)
if(common_elements):
    print(True)
else:
    print(False)