'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements!

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''


def move_zeros(array):
    new_array = []
    nulls = []
    for i in range(len(array)):
       if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                nulls.append(array[i])
            else: new_array.append(array[i])
       else:
            new_array.append(array[i])
    return new_array + nulls
