                                        ## Tuple Practise Question ##
                                        
def my_generator ():
    for i in range(50000000):
        yield i

print(next(my_generator))


