number_of_floors = int(input("Number of floors: "))
rooms_per_floor = int(input("Rooms per floor: "))

total_guests = 0
room_records = [] 
breakpoint()
for floor in range(1, number_of_floors + 1):
    for room in range(1, rooms_per_floor + 1):
        guests = int(input(f"Floor {floor}, Room {room} - Enter number of guests: "))
        
        
print(f"Floor {floor}, Room {room} - Number of guests: {guests}")
        
total_guests += guests
room_info = (floor, room, guests)
room_records.append(room_info)                                       
        

print(room_records)

print("\nHOTEL ROOM SUMMARY")
for floor, room, guests in room_records: 
    print(f"Floor {floor} | Room {room} | Guests: {guests}")        
print(f"Total number of guests: {total_guests}")




