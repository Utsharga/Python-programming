class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.units = 0.0
        self.points = 0.0
        self.gpa = 0.0 

    def get_name(self, name):
        return self.name

    def get_id (self, student_id):
        return self.student_id

    def get_units (self, units):
        return self.units

    def get_points (self, points):
        return self.points

    def get_gpa (self,gpa):
        return self.gpa

    def set_units (self, units):
        self.units = units

    def set_points (self, points):
        self.points = points

    def calculate_gpa (self):
        self.gpa = self.points/self.units

    
                            

   
            
        
        
