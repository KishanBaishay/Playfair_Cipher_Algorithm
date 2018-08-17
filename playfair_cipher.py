# Conversion of pain text to cipher text using Playfair Cipher

plain_text=input("Enter the Plain Text:")
playfair_matrix=[['M','O','N','A','R'],['C','H','Y','B','D'],['E','F','G','I','K'],['L','P','Q','S','T'],['U','V','W','X','Z']]

list_0=plain_text.split(' ')
plain_text=('').join(list_0)
print("")
list_0=list(plain_text)
m=len(list_0)
list_1=[]
smallchar_index=[]

#Checking for duplicate characters in the string
j=0
while j<m:
    if j<m and (j+1)<m:
        if list_0[j]==list_0[j+1]:
            list_1.append(list_0[j])
            list_1.append('X')
            j=j-1
        else:
            list_1.append(list_0[j])
            list_1.append(list_0[j+1])
    elif j<m and (j+1)>=m:
        list_1.append(list_0[j])
    j=j+2

#Finding the index of small characters
m=len(list_1)
for i in range(m):
    if list_1[i]>='a' and list_1[i]<='z':
        ascii_val=ord(list_1[i])
        list_1[i]=chr(ascii_val-32)
        smallchar_index.append(i)
    
l=len(list_1)
if l%2!=0:
    list_1.append('X')
    
modified_text=('').join(list_1)
print("Modified Text :",modified_text)

list_2=[]    
i=0
p=q=r=s=0
while i<l:
    for j in range(0,5):
        for k in range(0,5):
            if list_1[i]==playfair_matrix[j][k]:
                p=j
                q=k
            if list_1[i+1]==playfair_matrix[j][k]:
                r=j
                s=k
    if p==r and q!=s:
        q=(q+1)%5
        s=(s+1)%5    
        list_2.append(playfair_matrix[p][q])
        list_2.append(playfair_matrix[r][s])
    elif q==s and p!=r:
        p=(p+1)%5
        r=(r+1)%5
        list_2.append(playfair_matrix[p][q])
        list_2.append(playfair_matrix[r][s])
    else:
        list_2.append(playfair_matrix[p][s])
        list_2.append(playfair_matrix[r][q])
    i=i+2

l=len(list_2)
m=len(smallchar_index)
k=i=0
while i<l and k<m:
   if i==(smallchar_index[k]):
       ascii_val=ord(list_2[i])
       list_2[i]=chr(ascii_val+32)
       k=k+1
   i=i+1
 
cipher_text=('').join(list_2)
print("")
print("After Encryption the Cipher Text is :",cipher_text)


# Conversion of cipher text to plain text

l=len(cipher_text) 
list_3=list(cipher_text)
for i in range(l):
    if list_3[i]>='a' and list_3[i]<='z':
        ascii_val=ord(list_3[i])
        list_3[i]=chr(ascii_val-32)

i=0
p=q=r=s=0
list_4=[]
while i<l:
    for j in range(0,5):
        for k in range(0,5):
            if list_3[i]==playfair_matrix[j][k]:
                p=j
                q=k
            if list_3[i+1]==playfair_matrix[j][k]:
                r=j
                s=k
    if p==r and q!=s:
        q=(q-1)%5
        s=(s-1)%5
        list_4.append(playfair_matrix[p][q])
        list_4.append(playfair_matrix[r][s])
    elif q==s and p!=r:
        p=(p-1)%5
        r=(r-1)%5
        list_4.append(playfair_matrix[p][q])
        list_4.append(playfair_matrix[r][s])
    else:
        list_4.append(playfair_matrix[p][s])
        list_4.append(playfair_matrix[r][q])
    i=i+2
print("")

l=len(list_4)
i=k=0
while i<l and k<m:
    if i==(smallchar_index[k]):
        ascii_val=ord(list_4[i])
        list_4[i]=chr(ascii_val+32)
        k=k+1
    i=i+1

change_text=('').join(list_4)
list_4=change_text.split('X')
req_plain_text=('').join(list_4)
print("After Decryption the Plain Text is :",req_plain_text)
