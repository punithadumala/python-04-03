#  Print no of upper case letters in a string..?

str1="StriNG"
count1=0
for i in str:
    if ord(i)>=65 and ord(i)<=90:
        count1+=1
print(f"No of upper letters present in string is :{count1}")
# -------------------------------------------------------------------------
str2="StriNG"
count2=0
for i in str2:
    if i.isupper():
        count2+=1
print(f"No of upper letters present in string is :{count2}")
# ----------------------------------------------------------------------

str3="No of uPPer case LeTteRs pResEnt in stRing"
count3=0
for i in str3:
    if i==i.upper() and i!=" ":
        count3+=1
print(f"No of upper letters present in string is :{count3}")
# ------------------------------------------------------------------------
str="Dumalapunithayadav"
res_str=""
vowels="AEIOUaeiou"
for i in str:
    char=""
    if i in vowels:
        char=chr(ord(i)+1)
        res_str=res_str+char
    else:
        res_str=res_str+i
print(res_str)

# --------------------------------------------------------
Anagram
str1="top"
str2="pot"
len_str1=len(str1)
len_str2=len(str2)
flag=True
if len_str1!=len_str2:
    print("Not an anagram")
else:
    for i in str1:
        if str1.count(i)!=str2.count(i):
            flag=False
            break
    if flag:
        print("Anagram")
    else:
        print("Not an Anagram")
            
# -------------------------------------------------------------