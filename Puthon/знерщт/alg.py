# import time
# l=[]
# num=56093
# start=time.time()
# for i in range (1,100130):
#     l.append(i)
# left=0
# right=len(l)
# while left<=right:
#     mid=(left+right)//2
#     if l[mid]==num:
#         print(mid)
#         break
#     if l[mid]>num:
#         right=mid
#     if l[mid]<num:
#         left=mid
# end=time.time()
# print(end-start)
# def strcount(s):
#     for let in set(s):
#         count=0
#         for sub in s:
#             if sub== let:
#                 count+=1
#         print(let, count)
# strcount("sssassdsdffaa")
a = []
for n in range(1, 10000):
    s = bin(n)[2:] # перевод в двоичную систему
    s = str(s)
    if s.count('1') % 2 == 0:
        s = "100" + s[3:] + '000'
    else:
        s = "111" + s[3:] + "111"
    r = int(s, 2) # перевод в десятичную систему
    if r > 1580:
        a.append(n)
print(min(a))