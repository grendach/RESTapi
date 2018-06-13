from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S))

# Data to serve with our API
PEOPLE = {
    "Igor": {
        "fname": "Igor",
        "lname": "Temchenko",
        "timestamp": get_timestamp()
        },
    "Sergii": {
        "fname": "Sergii"
        "lname": "Temchenko"
        "timestamp": get_timestamp()
        }
    "Oleksandr": {
        "fname": "Oleksandr"
        "lname": "Temchenko"
        "timestamp": get_timestamp()
        }
}
# create a handler for our read (GET) people
def read():
    """
    This function responss to a request for /api/people
    with the complete list of people

    :return: sorted list of people
    """
    #create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
