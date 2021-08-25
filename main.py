from Project import *



if __name__ == '__main__':
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    decorator3 = ConcreteDecoratorC(decorator2)
    print("Client: Now I've got a decorated component:")
    client_code(decorator3)

