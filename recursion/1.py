# this is the example of the head recursion in which the job has to be made in the function must be called first

# count = 0


# def f():
#   global count
#   if count == 4:
#     return 
#   print('adi')
#   count += 1
#   f()


# f()


# this is the example of the tail recursion in which the function has to be called first


count = 0 

def func():
    global count
    if count == 4:
        return 
    count += 1
    func()
    print('Adi')



func()