import csv

start = False
def run():
    new_data = ""
    nfl = open("weekswithoutwins.txt","r")
    for line in nfl:
        # print(line)
        new_data += line
        # new_data += values
    start = True
    replacer(new_data)
    start = False
    # print(new_data)
    nfl.close()

def replacer(initial_string): 
    
    lst1 = list(initial_string) 
    lst2 = [','] 
    occurrence = 2
    lst3 = [] 
      
    count = 1
    for j in range(0, len(initial_string)): 
        if(',' == lst1[j]): 
            count+= 1
            if(count % occurrence == 0): 
                lst3.append(j) 
      
    for i in lst3: 
        lst1[i] = ":1 "
      
    print(lst1)
    final_string = ''.join(lst1)
    print(final_string)
    new_list = final_string.split(',')
    print(new_list)
def init(new_data):
    final = ''
    count = 0
    print(type(new_data))
    for k in new_data:
        # print('k',k)
        # print(type(k))
        if k == ',':
            # count += 1
            final += k
            if count % 2 == 1:
                final += " 1 "
                count += 1
        else:
            final += k
            # count += 1
    print(final)
                    
            
run()