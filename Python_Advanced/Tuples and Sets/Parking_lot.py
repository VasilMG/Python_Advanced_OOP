n = int(input())

command = [input().split(", ") for _ in range(n)] 

parking_lot = set()

for direction, car in command:
    if direction == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)
     
if parking_lot:   
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")