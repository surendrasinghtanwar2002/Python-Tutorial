                                                                    ## In this section we will practise the class decorator in python ##

def simple_decorator(fun):
    def wrapper():
        print("Something added on the function")
        fun()
        print("Something added after the function")
    return wrapper

@simple_decorator
def hello():
    print("Hy surendra")

def main():
    hello()

if __name__ == "__main__":
    main()

