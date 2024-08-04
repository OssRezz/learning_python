class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_avaible = True

    def sell(self):
        if self.is_avaible:
            self.is_avaible = False
            print(f"EL vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"EL vehiculo {self.brand}. No esta disponible")

    def check_status(self):
        return self.is_avaible

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError(
            "Este metodo debe ser implementando por la subclase")

    def stop_engine(self):
        raise NotImplementedError(
            "Este metodo debe ser implementando por la subclase")


class Car(Vehicle):
    def start_engine(self):
        if not self.is_avaible:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"

    def start_engine(self):
        if not self.is_avaible:
            return f"El motor del coche {self.brand} ha sido detenido"
        else:
            return f"El coche {self.brand} no esta disponible"


class Bike(Vehicle):
    def start_engine(self):
        if not self.is_avaible:
            return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicileta {self.brand} no esta disponible"

    def start_engine(self):
        if not self.is_avaible:
            return f"La bicicleta {self.brand} ha sido detenido"
        else:
            return f"La bicileta {self.brand} no esta disponible"


class Truck(Vehicle):
    def start_engine(self):
        if not self.is_avaible:
            return f"El motor del camión {self.brand} esta en marcha"
        else:
            return f"El camión {self.brand} no esta disponible"

    def start_engine(self):
        if not self.is_avaible:
            return f"El motor del camión {self.brand} ha sido detenido"
        else:
            return f"El camión {self.brand} no esta disponible"


class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.purchased_vehicles = []
        
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_status():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand}, no esta disponible")
            
    def inquired_vehicles(self, vehicle: Vehicle):
        if vehicle.check_status():
            availablity = "Disponible"
        else:
            availablity = "Disponible"
        print(f"El {vehicle.brand}, esta {availablity} y cuesta {vehicle.price}")
        


class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"EL {vehicle.brand} ha si añadido al inventario")
        
    def add_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha si añadido")
        
    def show_available_vehicles(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.is_avaible:
                print(f"- {vehicle.brand} por {vehicle.get_price()}")
                
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 45000)
truck1 = Truck("Volvo", "FH19", 80000)

customer1 = Customer("James")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

dealership.show_available_vehicles()

customer1.inquired_vehicles(car1)

customer1.buy_vehicle(car1)

dealership.show_available_vehicles()

