# Main Loop
    # GET Equipment from db
    # select Equipment
    # set time
    # calc stats
    # login
    # write stats to database

from Database.database import DatabaseClass
import hashlib
db = DatabaseClass()

def main():
    while True:
        # GET EQUIPMENT FROM DB
        equipment = db.get_equipment()

        # SELECT EQUIPMENT
        equipment_selected = False

        print('Select a apparaat: ')
        for i in equipment:
            print(i['ID'], '-', i['Name'])

        selected_equipment = -1
        while not equipment_selected:
            selected_equipment = int(input('Apparaat ID: '))
            for i in equipment:
                if selected_equipment == i['ID']:
                    equipment_selected = True
                    break

        # SET TIME
        time = input('Hoeveel minuten is er gesport? ')

        # CALCULATE STATS
        # TODO: Better formula for calculating calories (http://www.calorieenverbranden.nl/)
        calories = int(time) * 9

        # LOGIN
        email = input('Email: ')
        pw = input('PW: ')

        # Sha1 encryption for password
        sha1 = hashlib.sha1()
        sha1.update(pw.encode(encoding='UTF-8'))

        # Check if there is a customer with given login
        user = db.get_customer(email, sha1.hexdigest())

        # Login failed
        if user:
            print('Login success')

            # Write to database
            db.set_sport_activity(selected_equipment, user['User_ID'], time, calories)
        else:
            print('Login failed')

        print('\n')

try:
    main()
except KeyboardInterrupt:
    print('Program exit')
