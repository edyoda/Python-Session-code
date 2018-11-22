def binary_search(l,key):
    if len(l) == 0:
        return False
    else:        
        mid = len(l) // 2     
        if key == l[mid]:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid],key)
        else:
            return binary_search(l[mid+1:],key)
        
if __name__ == '__main__':
    print("Statement in bs.py")
    l = [15,25,45,50,56,70,80,90]
    key = 15
    result = binary_search(l,key)
    print(result)