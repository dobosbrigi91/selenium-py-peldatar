class MessageBox:
    def __init__(self):
        self.operation = []

    def send(self):
        self.operation.append(2)

    def receive(self):
        self.operation.append(1)

    def get_operation(self):
        return self.operation


mb = MessageBox()
mb.send()
mb.receive()
mb.send()
mb.send()
mb.receive()

a = mb.get_operation()
price_send = 15
price_receive = 0
send = mb.operation.count(2)
receive = mb.operation.count(1)
price = price_send * send + price_receive * receive
print('A költség:', price, 'Ft')

