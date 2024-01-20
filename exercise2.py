#exercise2
#print the sum of the curret number and the previous number
print (" printing current and previous number sum in a range (10)")

#string for previuos number
prev_num = 0

for i in range (1,11):
    #adding the previous number the current number
    sum= prev_num + i
    
    
    print ("Current number is", i ,"Previous number is", prev_num,  "sum is", sum)
    
    #string for current number
    prev_num = i