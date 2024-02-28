class Package:
    def __init__(self, senderName, receiverName, senderAddress, receiverAddress, weight, feePerOunce):
        self.senderName = senderName
        self.receiverName = receiverName
        self.senderAddress = senderAddress
        self.receiverAddress = receiverAddress
        self.weight = weight
        self.feePerOunce = feePerOunce

class OvernightPackage(Package):
    def __init__(self, senderName, receiverName, senderAddress, receiverAddress, weight, feePerOunce, overnightFeePerOunce):
        super().__init__(senderName, receiverName, senderAddress, receiverAddress, weight, feePerOunce)
        self.overnightFeePerOunce = overnightFeePerOunce

    def calculate_cost(self):
        return self.weight * (self.feePerOunce + self.overnightFeePerOunce)

    def display_info(self):
        print("Overnight Package Details:")
        print("Sender Name:", self.senderName)
        print("Receiver Name:", self.receiverName)
        print("Sender Address:", self.senderAddress)
        print("Receiver Address:", self.receiverAddress)
        print("Weight (oz):", self.weight)
        print("Fee per Ounce:", self.feePerOunce)
        print("Overnight Fee per Ounce:", self.overnightFeePerOunce)
        print("Total Cost:", self.calculate_cost())

class TwoDayPackage(Package):
    def __init__(self, senderName, receiverName, senderAddress, receiverAddress, weight, feePerOunce, flatFee):
        super().__init__(senderName, receiverName, senderAddress, receiverAddress, weight, feePerOunce,)
        self.flatFee = flatFee

    def calculate_cost(self):
        return (self.weight * self.feePerOunce) + self.flatFee

    def display_info(self):
        print("Two-Day Package Details:")
        print("Sender Name:", self.senderName)
        print("Receiver Name:", self.receiverName)
        print("Sender Address:", self.senderAddress)
        print("Receiver Address:", self.receiverAddress)
        print("Weight (oz):", self.weight)
        print("Fee per Ounce:", self.feePerOunce)
        print("Flat Fee:", self.flatFee)
        print("Total Cost:", self.calculate_cost())