
input('senderName :')
input('reciverName :')
input('SenderAddress :')
input('RecieverAddress :')
input('Weight :')
input('FeePerOunce :')

class Packet:
    def __init__(self, senderName,reciverName,SenderAddress,RecieverAddress,weight,FeePerOunce):
        self.senderName
        self.reciverName
        self.SenderAddress
        self.RecieverAddress
        self.weight
        self.FeePerOunce

        self.senderName = senderName
        self.senderName = reciverName
        self.senderName = SenderAddress
        self.senderName = RecieverAddress
        self.senderName = weight
        self.senderName = FeePerOunce

    def calculate_cost(self):
        # Define how to calculate the cost of shipping a packet
        pass

class FastDelivery(Packet):
    def __init__(self, senderName,reciverName,SenderAddress,RecieverAddress,weight,FeePerOunce):
        super().__init__(self, senderName,reciverName,SenderAddress,RecieverAddress,weight,FeePerOunce):
       
    def calculate_cost(self):
        # Define a faster delivery cost calculation
        pass

class FragilePacket(Packet):
    def __init__(self, senderName,reciverName,SenderAddress,RecieverAddress,weight,FeePerOunce):
        super().__init__(self, senderName,reciverName,SenderAddress,RecieverAddress,weight,FeePerOunce):
        

    def handle_with_care(self):
        # Define how to handle fragile packets
        pass