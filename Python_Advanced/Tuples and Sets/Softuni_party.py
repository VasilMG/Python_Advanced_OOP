def is_vip(guest):
    return guest[0].isdigit()


n = int(input())


vip_set = set()
normal_gets = set()

for r in range(n):
    reservation = input()
    if is_vip(reservation):
        vip_set.add(reservation)
    else:
        normal_gets.add(reservation)
        
while True:
    command = input()
    
    if command == "END":
        break
    if is_vip(command):
        vip_set.remove(command)
    else:
        normal_gets.remove(command)
        
print(len(vip_set) + len(normal_gets))
[print(g) for g in sorted(vip_set)]
[print(g) for g in sorted(normal_gets)]
