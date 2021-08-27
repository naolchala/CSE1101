def check_speed(speed):
    if speed < 70:
        print "Ok"
    else:
        points = (speed - 70)/5

        if points > 12:
            print "License suspended"
        else:
            print "Points:", points
