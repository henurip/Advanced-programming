class Calculator:
   
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
       

    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2
    
test = Calculator(10.5,2.5)

hasilPenjumlahan = test.add()
print("Hasil Penjumlahan:", hasilPenjumlahan)

hasilPengurangan = test.substract()
print("Hasil pengurangan:",hasilPengurangan)

    