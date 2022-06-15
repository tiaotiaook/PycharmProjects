import random

interval = random.randint(26,30)

for i in range(47):
    new_list=[]
    s1 = (random.randint(1,30) + interval) % 30
    new_list.append(s1)
    s2 = (random.randint(1,30) + interval) % 30
    new_list.append ( s2)
    s3 = (random.randint(1,30) + interval) % 30
    new_list.append ( s3 )
    s4 = (random.randint(1,30) + interval) % 30
    new_list.append ( s4)
    s5 = (random.randint(1,30) + interval) % 30
    new_list.append ( s5 )
    s6 = (random.randint(1,30) + interval) % 30
    new_list.append ( s6 )
    # print(new_list)

    flag = False
    for i in range(len(new_list)):
        for j in range(i):
            if new_list[i]==new_list[j]:
                flag = True
                break
        if flag:
            break

    if flag:
        print(f"有重复,{new_list}")
    else:
        print(f"没有重复,{new_list}")

# s1 =random.randint(1,30)
# s2 =random.randint(1,30)
# s3 =random.randint(1,30)
# s4 =random.randint(1,30)
# s5 =random.randint(1,30)
# s6 =random.randint(1,30)

# ss1 = s_1+interval
# sss1 = ss_1 % 30
# print(ss1)
# print(sss_1)


# sss2 = (s2 + interval) % 30
# sss3 = (s3 + interval) % 30
# sss4 = (s4 + interval) % 30
# sss5 = (s5 + interval) % 30
# sss6 = (s6 + interval) % 30

# list = [s1,s2,s3,s4,s5,s6]
#
# print(list)













