import math
# usd_salary = float(30_000)
# brl_salary = float(usd_salary*5/12)
print('--------------------------------------------------------')
min_usd_salary = 20000
loop_increment = min_usd_salary
max_usd_salary = 200000
include_value = 50000
while min_usd_salary <= max_usd_salary:
    print(str(min_usd_salary) + " yearly USD salary == " + str(round(min_usd_salary*5/12)) + " BRL monthly income.")    
    if((include_value > min_usd_salary) & (include_value < (min_usd_salary + loop_increment))):
        print(str(include_value) + " yearly USD salary == " + str(round(include_value*5/12)) + " BRL monthly income.")
    min_usd_salary = min_usd_salary + loop_increment
#print(str(usd_salary) + " yearly USD salary is equal to " + str(brl_salary) + " BRL monthly income.")
print('--------------------------------------------------------')