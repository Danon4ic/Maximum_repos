def palin(a):
    a = a.lower()
    rev_a = a[::-1]  
    if a == rev_a:  
        return True
    else:
        return False
a = input()
res = palin(a)
if res:
    print("True")
else:
    print("False")
