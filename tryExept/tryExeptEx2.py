import random
def Guess(participants):
    try:
        my_participant_dict = {}
        for participant in participants:
            my_participant_dict[participant] = random.randint(1, 9)
        if 'Larry' in my_participant_dict and my_participant_dict['Larry'] == 9:
            return True
        
    except KeyError:
        return None            

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))