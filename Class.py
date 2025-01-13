class Instructor:
    def __init__(self, Ins_name, Ins_address):
        self.name = Ins_name
        self.address = Ins_address

instructor_1 = Instructor(f"Mili", "Dhaka")
instructor_2 = Instructor("Mahi", "Rajshahi")
print(instructor_1.name, instructor_1.address)
print(instructor_2.name, instructor_2.address)