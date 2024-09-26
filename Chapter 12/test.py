class Email:
    def __init__(self,sender_name:str,receiver_name:str) -> None:
        self.sender_name = sender_name
        self.receiver_name = receiver_name

    def hello(self):
        return "Hello world"
    
def main():
    t1 = Email(sender_name="Surendra",receiver_name="Saket")
    value = getattr(t1,"hello")()
    print(value)

if __name__ =="__main__":
    main()