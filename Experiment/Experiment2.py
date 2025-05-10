class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (22/7) * self.radius * self.radius
    def perimeter(self):
        return 2 * (22/7) * self.radius

# c1 = circle(5)
# print(c1.area())
# print(c1.perimeter())

class employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showDetails(self):
        print("Role: ", self.role)
        print("Department: ", self.department)
        print("Salary: ", self.salary)


a = ['Jay']
print(a[::-1])
a.remove('Jay')