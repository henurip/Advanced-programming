class Package:
    def __init__(self, sender_name, receiver_name, sender_address, receiver_address, weight, fee_per_ounce):
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.weight = weight
        self.fee_per_ounce = fee_per_ounce

class OvernightPackage(Package):
    def __init__(self, sender_name, receiver_name, sender_address, receiver_address, weight, fee_per_ounce, overnight_fee_per_ounce):
        super().__init__(sender_name, receiver_name, sender_address, receiver_address, weight, fee_per_ounce)
        self.overnight_fee_per_ounce = overnight_fee_per_ounce

    def calculate_cost(self):
        return self.weight * (self.fee_per_ounce + self.overnight_fee_per_ounce)

    def display_info(self):
        print("Overnight Package Details:")
        print("Sender Name:", self.sender_name)
        print("Receiver Name:", self.receiver_name)
        print("Sender Address:", self.sender_address)
        print("Receiver Address:", self.receiver_address)
        print("Weight (oz):", self.weight)
        print("Fee per Ounce:", self.fee_per_ounce)
        print("Overnight Fee per Ounce:", self.overnight_fee_per_ounce)
        print("Total Cost:", self.calculate_cost())

class TwoDayPackage(Package):
    def __init__(self, sender_name, receiver_name, sender_address, receiver_address, weight, fee_per_ounce, flat_fee):
        super().__init__(sender_name, receiver_name, sender_address, receiver_address, weight, fee_per_ounce)
        self.flat_fee = flat_fee

    def calculate_cost(self):
        return (self.weight * self.fee_per_ounce) + self.flat_fee

    def display_info(self):
        print("Two-Day Package Details:")
        print("Sender Name:", self.sender_name)
        print("Receiver Name:", self.receiver_name)
        print("Sender Address:", self.sender_address)
        print("Receiver Address:", self.receiver_address)
        print("Weight (oz):", self.weight)
        print("Fee per Ounce:", self.fee_per_ounce)
        print("Flat Fee:", self.flat_fee)
        print("Total Cost:", self.calculate_cost())

book_dictionary = {}

def add_book_to_dictionary(title, author, publication_year):
    book_dictionary[title] = {"Author": author, "Publication Year": publication_year}


add_book_to_dictionary("The Lord of the Rings", "J.R.R. Tolkien", 1954)
add_book_to_dictionary("Pride and Prejudice", "Jane Austen", 1813)
add_book_to_dictionary("To Kill a Mockingbird", "Harper Lee", 1960)

print(book_dictionary)