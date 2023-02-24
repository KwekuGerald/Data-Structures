#computer Application In Civil Engineering (CE 257)
"""
FRIMPONG GERALD ABEIKU
6936921
Github account:kweku_gerald
Github link:https://github.com/KwekuGerald/Data-Structures.git
"""

#list of cars and their prices
CarsInGarage={
    "Honda Civic":22500,
    "Volkswagen GTI":29880,
    "Hyundai Sonata":24150,
    "Tesla Model 3":46990,
    "Polestar 2":48400,
    "Chevrolet Camaro":25600,
    "Ford Mustang":27470,
    "Nissan Z":39990,
    "BMW 2 Series":45200,
    "Mercedes Benz C Class":43550,
    "Mercedes Benz S Class":114500,
    "BMW 7 Series":93900,
    "Genesis G90 U":52725,
    "Porsche Panamera":88400,
    "2022 Audi A8":86500,
    "Lamborghini Urus":1000000,
    "Mclaren P1":115000000,
    "Koenigssegg One":2000000,
    "Aston Martins":2300000,
    "La Ferrari":2700000,
    "Buggati Chiron":3300000,
    "Buggati Veyron":3400000,
    "Lamborghini Sian":3600000,
    "Lamborghini Veneno":4500000,
    "Buggati Divo":580000,
    "Mercedes Maybach":8000000,
    "Mercedes Maybach":8000000,
    "Bugatti Centodiaca":9000000,
    "Bugatti La Voiture Noir":18000000,
}  

#get  user order for car_name 
car_name= input("Enter your car_name:")

#Check if car is in the garage 
if car_name in CarsInGarage:
    print("The",car_name, "Is avaliable in garage.")
    print("The price of the",car_name, "is",CarsInGarage[car_name], "$")
else:
    print("Sorry, the", car_name, "is not in garage")
    
