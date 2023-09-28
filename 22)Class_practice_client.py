class Client:
    """
    Class that emulates behavior
    """
    def __init__(self, new_id):
        " Emulates registration client in bank "
        self.id = new_id
        self.money = 0
    
    def add(self, money):
        " Emulates adding some money at client account"
        self.money += money
    
    def take_out(self, money):
        " Emulates taking money from client's account "
        self.money -= money
    
    def information(self):
        " Prints information of client"
        print("Client's id is: ", self.id, " and here is ", self.money ," money in this account")

client_list = []
for id in range(5):
    client_list.append(Client(id))
    client_list[id].add(id*1000 + 100)
    client_list[id].information()