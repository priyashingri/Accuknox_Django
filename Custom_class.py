class Rectangle:
    def __init__(self, length: int, width: int):
        #initialisation 
        self.length = length
        self.width = width

    def __iter__(self):
        # Define the iteration
        self._iter_data = [
            {'length': self.length},
            {'width': self.width}
        ]
        return iter(self._iter_data)

if __name__ == "__main__":
    #instance of Rectangle
    rect = Rectangle(length=2, width=3)
    
    # Iterate over Rectangle instance
    for item in rect:
        print(item)
