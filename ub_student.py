class UBStudent:
    def __init__(self, first_name, last_name, ubit):
        self.first_name = first_name
        self.last_name = last_name
        self.ubit = ubit
    
    def __str__(self):
        return 'UBStudent(first_name: {}, last_name: {}, ubit: {})'.format(self.first_name, self.last_name, self.ubit)
    
    def __repr__(self):
        return UBStudent.__str__(self)