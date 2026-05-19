input='leetcode'
# output='l'
count=1
for i in range(len(input)-1):
    if input[i] in input[i+1:len(input)]:
        continue
    else:
        if count == 1:
            print(input[i])
            break
        count+=1
 
# print(input[1])