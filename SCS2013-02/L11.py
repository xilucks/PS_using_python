#E-1
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(f'{self.name}{self.max_speed}{self.mileage}')
#E-2
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seat_capacity):
        super().__init__(name, max_speed, mileage)
        self.seat_capacity = seat_capacity
    def print_vehicle(self):
        super().print_vehicle()
        print(f'{self.seat_capacity}')
#E-3
class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, num_doors):
        super().__init__(name,max_speed,mileage)
        self.num_doors = num_doors

    def print_vehicle(self):
        super().print_vehicle()
        print(f'{self.num_doors}')
#E-4
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(f'{self.name}{self.max_speed}{self.mileage}')

    def charge(self):
        return self.mileage * 10


#E-5
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seat_capacity):
        super().__init__(name, max_speed, mileage)
        self.seat_capacity = seat_capacity
    def print_vehicle(self):
        super().print_vehicle()
        print(f'{self.seat_capacity}')

    def charge(self):
        charge = super().charge()
        charge += self.seat_capacity * 5
        return charge
#E-6
class Triange:
    def __init__(self, base, t_height):
        self.base = base
        self.t_height = t_height

    def tri_area(self):
        return 0.5 * self.base * self.t_height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

#E-7

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width= side, height= side)

class Pyramid(Square, Triange):
    def __init__(self,base, slant_height):
        Square.__init__(self,base)
        Triange.__init__(self,base,slant_height)
    def area(self):
        square_area = super().area()
        triangle_area = super().tri_area()
        return square_area +  4 * triangle_area

S1 = Square(5)

