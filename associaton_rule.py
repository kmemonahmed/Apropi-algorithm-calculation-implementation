iteration = int(input("Enter How Many Pattern : "))
# iteration = 7
pattern = []
# pattern = [['Beef', 'Chicken', 'Milk'], ['Beef', 'Cheese'], ['Cheese', 'Boots'], ['Beef', 'Chicken', 'Cheese'], ['Beef', 'Chicken', 'Clothes', 'Cheese', 'Milk'], ['Chicken', 'Clothes', 'Milk'], ['Chicken', 'Milk', 'Clothes']]
unique = []
composit = []
i=1
m=0
n=0
count_dict = {}

min_support = int(input("Enter Minimum Support : "))
min_confidence = int(input("Enter Minimum Confidence : "))
# min_support = 50
# min_confidence = 50

while i<=iteration:
    temp = input(f'Enter Pattern {i} : ')
    convert_to_list = temp.split(',')
    pattern.append(convert_to_list)
    i+=1

for j in pattern:
    for k in j:
        composit.append(k)
        if k not in unique:
            unique.append(k)

for j in unique:
    m = composit.count(j)
    temp_dict= {
        j:m
    }

    count_dict.update(temp_dict)

print(f'\nFrequent Item - 1-item set = {count_dict}\n')

support_in_fraction = (min_support/100)*iteration
support = int(support_in_fraction)

print(f'\nMinimum Support In Fraction = {support_in_fraction}\n')
print(f'\nMinimum Support = {support}\n')

copy_count_dict = count_dict.copy()
for k,v in copy_count_dict.items():
    if v < support:
        count_dict.pop(k)

print(f'\nFrequent Item - 1-item set After Cutoff = {count_dict}\n')

temp_for_two_item_list = []

for k in count_dict.keys():
    temp_for_two_item_list.append(k)
    


two_item_pattern = []
temp_list = []

s=1
e=0

while s <= len(temp_for_two_item_list) and e < len(temp_for_two_item_list)-1:
    if s != e:
        temp_list.append(temp_for_two_item_list[e])
        temp_list.append(temp_for_two_item_list[s])
        two_item_pattern.append(temp_list)
        temp_list = []
    s+=1
    if s == len(temp_for_two_item_list):
        s = e+1
        e+=1

print(f'\nFrequent Item - 2-item set (Pattern Only) = {two_item_pattern}---lengh = {len(two_item_pattern)}\n')

es = 0
ea = 0 
count = 0
count_dict_2 = {}

while ea < len(two_item_pattern):
    if two_item_pattern[ea][0] in pattern[es] and two_item_pattern[ea][1] in pattern[es]:
        # print(f'{two_item_pattern[ea][0]},{two_item_pattern[ea][1]}----------{pattern[es]}--------yes')
        count +=1
    if es != len(pattern)-1:
        es+=1
    else:
        temp_dict = {
            str(two_item_pattern[ea]):count
        }
        count_dict_2.update(temp_dict)
        count=0
        ea+=1
        es = 0
    
print(f'\nFrequent Item - 2-item set ={count_dict_2}\n')     

copy_count_dict = count_dict_2.copy()

for k,v in copy_count_dict.items():
    if v < support:
        count_dict_2.pop(k)

print(f'\nFrequent Item - 2-item set After Cutoff = {count_dict_2}\n')

# NOW ASSOCIATION RULE FOR {A}->{B}

associaton_rule_for_2 = []
temp = []
temp_2 = []
for k,v in count_dict_2.items():
    purify = k.strip("[']")
    purify = purify.replace("'","")
    purify = purify.replace(" ","")
    purify = purify.split(',')
    temp.append(purify[0])
    temp.append(purify[1])
    temp.append(v)
    s = int(v)/int(count_dict[purify[0]])
    s=round(s,2)
    temp.append(s)
    temp.append(s*100)
    
    temp_2.append(purify[1])
    temp_2.append(purify[0])
    temp_2.append(v)
    s = int(v)/int(count_dict[purify[1]])
    s=round(s,2)
    temp_2.append(s)
    temp_2.append(s*100)
    associaton_rule_for_2.append(temp)
    associaton_rule_for_2.append(temp_2)
    temp=[]
    temp_2=[]

print(f'\nAssociaton Rule for a--->b = {associaton_rule_for_2}\n')

print('------------Final Rules a--->b------------------')
for emon in associaton_rule_for_2:
    if emon[4] >= min_confidence:
        print(emon)

print('---------------------------------------------\n')

temp_for_three_item_list = []

for k in count_dict_2.keys():
    purify = k.strip("[']")
    purify = purify.replace("'","")
    purify = purify.replace(" ","")
    purify = purify.split(',')
    temp_for_three_item_list.append(purify)

unique_2 = []
for x in temp_for_three_item_list:
    for y in x:
        if y not in unique_2:
            unique_2.append(y)

temp_for_three_item_list = unique_2

print(f'\nunique for three item list = {temp_for_three_item_list}\n')

# temp_for_three_item_list = [1,2,3,4,5]

three_item_pattern = []
temp_list = []

s=2
e=0
f=1

while s <= len(temp_for_three_item_list)+2 and e < len(temp_for_three_item_list)-1 and f < len(temp_for_three_item_list):
    if s != e and s!=f:
        temp_list.append(temp_for_three_item_list[e])
        temp_list.append(temp_for_three_item_list[f])
        temp_list.append(temp_for_three_item_list[s])
        three_item_pattern.append(temp_list)
        temp_list = []
    s+=1
    if s == len(temp_for_three_item_list):
        s = f+1
        f+=1
        if f == len(temp_for_three_item_list):
            s = e+1
            e+=1
            f = e+1

print(f'\nFrequent Item - 3-item set (Pattern Only) = {three_item_pattern}---lengh = {len(three_item_pattern)}\n')


es = 0
ea = 0 
count = 0
count_dict_3 = {}

while ea < len(three_item_pattern):
    if three_item_pattern[ea][0] in pattern[es] and three_item_pattern[ea][1] in pattern[es] and three_item_pattern[ea][2] in pattern[es]:
        count +=1
    if es != len(pattern)-1:
        es+=1
    else:
        temp_dict = {
            str(three_item_pattern[ea]):count
        }
        count_dict_3.update(temp_dict)
        count=0
        ea+=1
        es = 0
    
print(f'\nFrequent Item - 3-item set ={count_dict_3}\n')

copy_count_dict = count_dict_3.copy()

for k,v in copy_count_dict.items():
    if v < support:
        count_dict_3.pop(k)

print(f'\nFrequent Item - 3-item set After Cutoff = {count_dict_3}\n')



# NOW ASSOCIATION RULE FOR {A,B}->{C}

associaton_rule_for_3 = []
now=[]
temp = []
temp_2 = []
for k,v in count_dict_3.items():
    purify = k.strip("[']")
    purify = purify.replace("'","")
    purify = purify.replace(" ","")
    purify = purify.split(',')

    now.append(purify[0])
    now.append(purify[1])
    g = str(now)
    temp.append(now)
    temp.append(purify[2])
    temp.append(v)
    s = int(v)/int(count_dict_2[g])
    s=round(s,2)
    temp.append(s)
    temp.append(s*100)
    
    temp_2.append(purify[2])
    temp_2.append(now)
    temp_2.append(v)
    s = int(v)/int(count_dict[purify[2]])
    s=round(s,2)
    temp_2.append(s)
    temp_2.append(s*100)
    associaton_rule_for_3.append(temp)
    associaton_rule_for_3.append(temp_2)

    temp=[]
    temp_2=[]
    now=[]

    now.append(purify[0])
    now.append(purify[2])
    g = str(now)
    temp.append(now)
    temp.append(purify[1])
    temp.append(v)
    s = int(v)/int(count_dict_2[g])
    s=round(s,2)
    temp.append(s)
    temp.append(s*100)

    temp_2.append(purify[1])
    temp_2.append(now)
    temp_2.append(v)
    s = int(v)/int(count_dict[purify[1]])
    s=round(s,2)
    temp_2.append(s)
    temp_2.append(s*100)
    associaton_rule_for_3.append(temp)
    associaton_rule_for_3.append(temp_2)

    temp=[]
    temp_2=[]
    now=[]

    now.append(purify[1])
    now.append(purify[2])
    g = str(now)
    temp.append(now)
    temp.append(purify[0])
    temp.append(v)
    s = int(v)/int(count_dict_2[g])
    s=round(s,2)
    temp.append(s)
    temp.append(s*100)

    temp_2.append(purify[0])
    temp_2.append(now)
    temp_2.append(v)
    s = int(v)/int(count_dict[purify[1]])
    s=round(s,2)
    temp_2.append(s)
    temp_2.append(s*100)
    associaton_rule_for_3.append(temp)
    associaton_rule_for_3.append(temp_2)

    temp=[]
    temp_2=[]
    now=[]

print(f'\nAssociaton Rule for a,b--->c = {associaton_rule_for_3}\n')

        
print('------------Final Rules a,b--->c------------------')

for emon in associaton_rule_for_3:
    if emon[4] >= min_confidence:
        print(emon)