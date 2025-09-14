Modularing Programing:- a larg program divide into small modules. 
    --> script
    --> top-don
        --> function
    --> object orinted
#functional object's provided by python.

https://prod.liveshare.vsengsaas.visualstudio.com/join?A3B395414980495F8D5E8CA2C8289D548E5E
object bbased not support polymorphism, inheritance.

Oops -> provide security on data.
     -> code reuseability

hou to achive.
Encapsulation, Polymorphism, Abstraction, Inheritance, Hidding, Binding(Static, Dynamic)(data binding, methode binding)

Class--> user defind datatype, class is a blueprint of object. non-primitive data type. combination of data and methodes.
 Methode--> methode provide abstraction of data. by default all methodes are static.that sho static behavior.
    private-->data mamber
    public--> everyone can access anyhare and provide to methodes.
    protected--> both the class share our data so that use protected.
    default--> vithin a module.

    highly secured syntax __demo__ 
    secured syntax __demo

Object--> Instance of the class. Realtime entity. class variable. 

self--> self hold the object ref of curent object of the curr class

every object containe three property -> state, behavior, Identity.  

5-5 object (identity, behavior, state) homevork

different betbeen methode--> in pu


constructor--> initialize the data mamber
setter injection--> set individual value (set each each value)

class data mamber pr bina object ke operation perform nhi kr sakte.
be create methode for define the behavior, that provide data abstraction.
__str__ that return trace code object. this is method of objecct code.

Q.1 Adiition of to height object.
// codebetter


Inheritance--> code reusability, is -a relationship, parent-child relationship. order of inheritance is top-doun, 
syntax for inheritance--> class DerivedClass (BaseClass): pass // BaseClass functional object.
derived class object is to be responsible for memry allocation of all the data member of its base class.
derived class objects is to be elligible for calling of all the methode of its parent class
types of Inheritanc--> 
--> Single lavel - one parent one child, only one class can be inherit and one class can be derived.
--> Multilavel - combination of multiple simple inheritance. A<--B<--C<--D B,C is intermideat class.
--> Multiple - A , B both parent classes and onle  C is derived class.
--> Heirarchical - Combination of multilavel Inheritance. like lavel of tree.
--> Hybrid - combination of to inheritance.
super--> super is a method hich is to be call the parent class constructor from the child class constructor.

Polymorphism--> ABC() Abstract Base Class under the abc module.
abstract class ka object nhi btnate. must inheritable class. abstract class jisme inherit hoti hai usme uski methode ko override krna pdta hai.

e cant create object of abstract class.
an abstract class called must inheritable class.
it is complersarly overriding of abstract method of the abstact class. in hich class abstrct class is to be inherited.
ABC used to declear abstract class. inherit the ABC class.
Q2. rite a program for all shapes ith abstract methode area.
Q3. vhicle class --> color|price|chesses no| registratio no
vhikle --> to vheeler --

Abstraction achive on class lavel

Vehicle
├── LandVehicle
│   ├── TwoWheeler
│   │   ├── FuelBased
│   │   │   ├── Bike
│   │   │   └── Scooter
│   │   └── FuelLess
│   │       ├── Bicycle
│   │       └── E-Bike
│   │
│   ├── ThreeWheeler
│   │   ├── FuelBased
│   │   │   └── AutoRickshaw
│   │   └── FuelLess
│   │       └── E-Rickshaw
│   │
│   └── FourWheeler
│       ├── FuelBased
│       │   ├── Car
│       │   ├── Jeep
│       │   ├── Truck
│       │   └── Bus
│       └── FuelLess
│           ├── E-Car
│           ├── E-Bus
│           └── SolarCar
│
├── AirVehicle
│   ├── FuelBased
│   │   ├── Airplane
│   │   └── Helicopter
│   └── FuelLess
│       ├── Glider
│       ├── Drone (Electric)
│       └── SolarPlane
│
└── WaterVehicle
    ├── FuelBased
    │   ├── Ship
    │   └── MotorBoat
    └── FuelLess
        ├── SailBoat
        ├── PaddleBoat
        └── SolarFerry
