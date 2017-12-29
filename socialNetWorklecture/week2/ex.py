from __future__ import print_function
import os  # using get local path

os.chdir("C:/pythonwork/week2")  # change folder path

cwd = os.getcwd()  # get working directory vairable

#==============================================================================
# print(cwd)
#==============================================================================


def cal_age(x):
    return x + 15


file = open(cwd + "/age_test.txt", "r")
file_w = open(cwd + "/age_both.txt", "w")

count = 0
for age in file.readlines():
    age = age.strip()
    if(count == 0):
        new_headers = str(age) + ";Age in 2015"
        file_w.write(new_headers + '\n')
    else:
        old_age = int(age)
        new_age = cal_age(old_age)
        file_w.write(str(age) + ";" + str(new_age) + '\n')
    count += 1

file.close()
file_w.close()
