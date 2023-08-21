# python program to convert time
# from 12 hour to 24 hour

# input 09:04:45 -> PM
# output 21:04:30

# input 12.04.45 -> AM
# Output 00:04:20

# function to convert to 24hour

def convert24(t):

# check if the last two elements is Am
# and first two elements is 12
    if t[-2:] == 'AM' and t[:2] == '12':
        return '00' + t[2:-2]
    # remove the AM
    elif t[-2:] == 'AM':
        return t[:-2]
    
# check if the last two elements is Pm
# and first two elements is 12 
    elif t[-2] =='PM' and t[:2] == '12':
        # remove the pm
         return t[:-2] 
    
# add 12 to pm
    else:
        return str(int(t[:2] )+ 12) + t[2:8]
# prompt user
prompt = input('Enter time in 12 hour:')
result = convert24(prompt)
# print result
print(result)



    



 
    

