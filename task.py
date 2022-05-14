UP_PAYMENT = 800
MAX_PAYMENT = 4500
TO_SAVE = 0.7
payment = 300
current_age = 27
total_money = 0

CAR_PRICE = 300000
is_car_byeid = False
House_price = 600000
is_House_byelid = False
while current_age <= 60:
    total_money += 12 * payment * TO_SAVE
    if payment < MAX_PAYMENT:
        payment += UP_PAYMENT
    if total_money >= CAR_PRICE and not is_car_byeid:
        print('Я могу позволите себе ламборгини')
        is_car_byeid = True
    if total_money >= House_price and not is_House_byelid:
        print('Я могу позволите себе дом')
        is_House_byelid = True

    print('Нам сейчас: ', current_age, 'У нас сейчас: ', total_money)
    current_age += 1
    
