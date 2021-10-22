list1 = [1, 2, 3]
try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
except:
    print('error입니당')
else:
    print('error입니당!')
finally:
    print('error입니당!!')