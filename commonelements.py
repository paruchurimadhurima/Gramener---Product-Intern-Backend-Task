def common_elements(list1, list2):
    return set(list1).intersection(set(list2)) # returns common elemenents

def uncommon_elements(list1, list2):
    return set(list1) - set(list2) # returns the set of elements present in list1 but not in list2

def main():
    list1 = input().strip().split()
    list2 = input().strip().split()
    print(common_elements(list1, list2))
    print(uncommon_elements(list1, list2))

main()