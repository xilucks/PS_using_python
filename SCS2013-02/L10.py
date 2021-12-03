#E-1
# Create a Car class with color (string), num_door (integer) and max_speed (integer) instance attributes.
#
# Then, create three car objects:
#
# car_A: red color, 3 doors, and 200 max speed
# car_B: blue color, 4 doors, and 240 max speed
# car_C: green color, 2 doors, and 210 max speed

class Car:
    def __init__(self, color, num_doors, max_speed):
        self.color = color
        self.num_doors = num_doors
        self.max_speed = max_speed
car_A = Car("red",3,200)
#E-2
# Write a program to create an instance called s1 of a specified class Student htat has the following namespace (which is displayed by print(s1.__dict__))
#
# {'student_id': 102, 'student_name': 'James', 'class_name': 'SCS2013'}
class Student:
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name

s1 = Student(102,'James,SCS2013')
print(s1.__dict__)

#E-3
# Create a class Calculator that has two integer attributes first and second and
#
# instance variables
#
# two integer attributes: first and second
# instance methods
#
# add, sub, mul, div, pow: methods performing addition, subtraction, multiplication, division, and power of the two instance variables and return the value

class Calculator:
    # constructor
    def __init__(self, first = 1, second = 1):
        self.first = first
        self.second = second
    # instance methods: add, sub, mul, div, pow
    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first//self.second
    def pow(self):
        return self.first ** self.second
    def display_all(self):
        print(f'First number {self.first}, Second number {self.second}')
        print(f'Add: {self.add()}, Sub: {self.sub()}, Mul: {self.mul()}, Div: {self.div()}, Pow: {self.pow()}')


#E-4
# Create a class G_Calculator that has arbitrary number of integer attributes and three instance methods
#
# instance variables
#
# arbitrary number of integers: nums
# note that it can be either tuple type or list type
# instance methods
#
# sums and products performing summation and multiplication of all the elements in nums and return the value
# get_Numbers that takes arbitrary number of integers using user input (: take multiple integers separated by space) and assign it to the instance variable nums
# note that the user input needs to be converted to a list of integers
class G_Calculator:
  # constructor
    def __init__(self, *args):
        self.nums = args

    def sums(self):
        result = 0
        for i in self.nums:
            result += i
        return result
    def products(self):
        result = 1
        for i in self.nums:
            result *= i
        return result
    def get_Numbers(self):
        self.nums = input()
        self.nums = [ int(i) for i in self.nums.split()]

#E-5
# Create a class called MyString that has two methods: get_String that accepts a string from the user and print_String that prints the string in upper case.
#
# Note that an object is constructed with an empty string.
class MyString:
    def __init__(self):
        self.my_str = ''

    def get_String(self):
        self.my_str = input()

    def print_String(self):
        print(self.my_str.upper())
#E-6

# Create a class for the implementation of the Queue data structure.
#
# instance variable
#
# queue: a list
# max_size: max size of the queue
# instance methods
#
# size: return the current size of the queue list
#
# isEmpty: return the boolean that tells the queue is empty
#
# isFull: return the boolean that tells the queue is full (no more space to store elements)
#
# enqueue: adds an element to the end (leftmost) of the queue
#
# note that we can use insert method of the list to add an element to the leftmost position of the list
# if the queue has no more space, we just need to print some message "Queue is Full"
# dequeue: removes an item from the front end (rightmost) of the queue
#
# note that we can use pop method of the list to remove the rightmost element of the list
# if the queue is empty, we just need to print a message "Queue is Emtpy"
# print_queue: prints the queue status

class Queue:
  # constructor
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

  # instance methods: size, isEmpty, isFull, enqueue, dequeue, print_queue
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []

    def isFull(self):
        return len(self.queue) == self.max_size

    def enqueue(self,element):
        if not self.isFull():
            self.queue.insert(0,element)
    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop()
    def print_queue(self):
        print(self.queue)
  # test
  # myQueue = Queue(10)  # create a queue object that has maximum size of 10
  # myQueue.print_queue()
  #
  # myQueue.enqueue(4)
  # myQueue.enqueue(5)
  # myQueue.enqueue(6)
  #
  # myQueue.print_queue()
  #
  # myQueue.enqueue('q')
  # myQueue.enqueue('u')
  # myQueue.enqueue('e')
  #
  # myQueue.dequeue()
  # myQueue.print_queue()
  #
  # myQueue.enqueue('u')
  # myQueue.enqueue('e')
  #
  # myQueue.print_queue()
  #
  # myQueue.enqueue(1)
  # myQueue.enqueue(2)
  # myQueue.enqueue(3)
  # myQueue.enqueue(11)
  #
  # myQueue.print_queue()
  #
  # myQueue.dequeue()
  #
  # myQueue.print_queue()