def print_times_table(time_value):
    if isinstance(time_value, int)==False:
        raise Excepton("print_time_table only works with integer")
    count = 1
    while count < 13:
        result = count * time_value
        print(count,"times",time_value, "equals",result )
        count = count+ 1

print_times_table("six")
