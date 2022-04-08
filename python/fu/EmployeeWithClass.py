class Employee:
    """Represents an employee"""
    count = 0

    def __init__(self, first, last ):
        """Initializes firstName, lastName and increments count"""
        self.firstName = first
        self.lastName = last

        Employee.count += 1 

        print("Employee constructor for %s, %s" \
            % ( self.lastName, self.firstName))

    def __del__(self):
        """Decrements count and prints message"""
        Employee.count -= 1 
        print("Employee destructor for %s, %s" \
            % ( self.lastName, self.firstName))
