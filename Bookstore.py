# Initialize an empty list to store the gamers
gamers = []

# Define a function to add a gamer to the list if they have a name and availability
def add_gamer(gamer, gamers_list):
    """
    Add a gamer to the gamers list if they have a name and availability.
    
    Args:
    - gamer (dict): A dictionary containing the gamer's information.
    - gamers_list (list): The list of gamers.
    """
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        raise ValueError("Gamer missing critical information")

# Define some sample gamers
kimberly = {
    'name': "Kimberly Warner",
    'availability': ["Monday", "Tuesday", "Friday"]
}

# Add the gamers to the list
add_gamer(kimberly, gamers)

# Add more gamers to the list
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Define a function to build a frequency table of availability
def build_daily_frequency_table():
    """
    Build a frequency table for each day of the week.
    
    Returns:
    - dict: A dictionary representing the frequency table.
    """
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }

# Build a frequency table of availability for all gamers
availability_frequency = build_daily_frequency_table()

# Define a function to calculate the availability frequency table
def calculate_availability(gamers_list, availability_table):
    """
    Calculate the availability frequency table for all gamers.
    
    Args:
    - gamers_list (list): The list of gamers.
    - availability_table (dict): The availability frequency table.
    """
    for gamer in gamers_list:
        for day in gamer['availability']:
            availability_table[day] += 1

# Calculate the availability frequency table for all gamers
calculate_availability(gamers, availability_frequency)

# Define a function to find the best night for a game based on the availability frequency table
def find_best_night(availability_table):
    """
    Find the night with the highest availability based on the availability frequency table.
    
    Args:
    - availability_table (dict): The availability frequency table.
    
    Returns:
    - str: The best night for the game.
    """
    best_availability = max(availability_table.values())
    best_night = [day for day, availability in availability_table.items() if availability == best_availability]
    return best_night[0]

# Find the best night for a game
game_night = find_best_night(availability_frequency)

# Define a function to find all gamers available on a given night
def available_on_night(gamers_list, day):
    """
    Find all gamers available on a given night.
    
    Args:
    - gamers_list (list): The list of gamers.
    - day (str): The day to check for availability.
    
    Returns:
    - list: A list of gamers available on the given night.
    """
    return [gamer for gamer in gamers_list if day in gamer['availability']]

# Find all gamers available on the best night
attending_game_night = available_on_night(gamers, game_night)

# Define a string template for an email invitation
form_email = """Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. 
Come by on {day_of_week} and have a blast!

Magically Yours, the Sorcery Society"""

def send_email(gamers_who_can_attend, day, game):
    """
    Send email invitations to gamers who can attend the game night.
    
    Args:
    - gamers_who_can_attend (list): List of gamers who can attend.
    - day (str): The day of the game night.
    - game (str): The name of the game.
    """
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))

# Send email invitations to gamers available on the best night
send_email(attending_game_night, game_night, "Abruptly Goblins!")

# Find gamers unable to attend the best night and calculate the availability for the second-best night
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
available_second_game_night = available_on_night(gamers, second_night)

# Send email invitations to gamers available on the second-best night
send_email(available_second_game_night, second_night, "Abruptly Goblins!")
