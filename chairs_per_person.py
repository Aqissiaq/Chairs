with open("reservations.csv") as f:
    for reservation in f:
        name, number = reservation.split(",")
        try:
            chairs_per_person = 50 / int(number)
            assert name is not ""
        except ZeroDivisionError:
            print("{} has attempted to reserve 0 seats".format(name))
        except ValueError:
            print("{} has reserved a non-number amount of seats".format(name))
        except AssertionError:
            print("Name must be a non-empty string")
            
        print("{} will get {} chairs per person".format(name, chairs_per_person))
