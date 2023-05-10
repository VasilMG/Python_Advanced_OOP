from collections import deque
price = int(input())
barrel = int(input())
bullets = deque(input().split())
locks = deque(input().split())
price_intelligence = int(input())
current_barrel = deque()
inital_bullets = len(bullets)
c_bullets = inital_bullets

def reload(ba , bu ):
    if bu:
        for j in range(ba):
            if bu:
                current_barrel.append(bu.pop())
    return current_barrel

current_barrel = reload(barrel, bullets)

while c_bullets > 0:
    if current_barrel:
        if locks:
            current_bullet = int(current_barrel.popleft())
            current_lock = int(locks[0])
            if current_bullet <= current_lock:
                locks.popleft()
                print("Bang!")
                c_bullets -= 1
            else:
                print("Ping!")
                c_bullets -= 1
                continue
            
        else:
            break
    else:
        if bullets:
            current_barrel = reload(barrel, bullets)
            print("Reloading!")
        else:
            break
        
bullets_left = len(bullets) + len(current_barrel)
money_earned = price_intelligence - (inital_bullets - bullets_left) * price
if locks and not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")  
    
elif not locks:
    print(f"{bullets_left} bullets left. Earned ${money_earned}")      

    