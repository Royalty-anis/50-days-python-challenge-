def any_number():
   total_count = 0
   total_num = 0
   while True:
    num = input("num: ")
    if num.lower() == 'stop':
           break
    else:
             total_num += int(num)
             total_count += 1  
   return total_num / total_count
 try:
     print(any_number())
 except ValueError:
     print("int only,use 'stop' to get your calculations" )
