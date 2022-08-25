from life360 import life360
import datetime
import whatsappBot as wtsp
import time

if __name__ == "__main__":

    # TODO: make a class of alerts and creat list of (alert.time,alert.message) for more generic alerts
    FEEDING_TIME = "19:00"
    #check every minute if it's the feeding time
    while True:
        now = datetime.datetime.now()
        curr_time = str(now.time())[0:5]

        if curr_time == FEEDING_TIME:
            # setting the connection with the life360 api
            authorization_token = "**********" # DO NOT REVEAL ON GITHUB
            api = life360(authorization_token=authorization_token)

            # returns json of all the circle dictionaries that you're member in
            circles = api.get_circles()

            # grabs the Family circle (the 1st circle)
            circle_id = circles[0]['id']
            circle = api.get_circle(circle_id)


            # setting a list of tuples for each member that is currently at home and calling
            at_home = []
            for m in circle['members']:
                if m['location']['name'] == "Home":
                    at_home.append((m['firstName'], m['loginPhone']))

            msg = "It's time to feed Spike!"
            wtsp.send_message(contacts, msg)
            print(at_home)
        print(curr_time)
        time.sleep(60) 
