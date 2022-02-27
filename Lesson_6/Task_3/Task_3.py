from os.path import join
dict1 = {}
dict_user = []
dict_hobby = []


file_users = open(join(".", "task_3_users.csv"),mode="r",encoding="utf-8") #Сортировка ФИО
for x in file_users:
    user_1 = x.split(",")[0][0]
    user_2 = x.split(',')[1][0]
    user_3 = x.split(',')[-1][0]
    dict_user.append(user_1 + user_2 + user_3)
file_users.close()


file_hobby = open(join(".", "task_3_hobby.csv"),mode="r",encoding="utf-8") #Сортировка хобби
for x in file_hobby:
    hobby = x.split("\n")[0].replace(",", ";")
    dict_hobby.append(hobby)
file_hobby.close()

counter = 0
while counter < len(dict_user):
    try:

        if dict_hobby[counter] in dict_hobby:
            b = dict_hobby[counter]
    except IndexError:
        b = None

    a = dict_user[counter]
    dict1[a] = b
    counter += 1
print(dict1)

file_rezult = open(join(".", "task_3_rezult.txt"),mode="w",encoding="utf-8")
file_rezult.write(str(dict1))
file_rezult.close()