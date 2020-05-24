class Athletics:

    def __init__(self, athletics_name = None, stage_duration = None, number_of_participants = None, distance_in_meters = None):
        self.athletics_name = athletics_name
        self.stage_duration = stage_duration
        self.number_of_participants = number_of_participants
        self.distance_in_meters = distance_in_meters

    def __del__(self):
        return

    def __str__(self):
        stage_duration = 'Stage duration: {}\n'.format(self.stage_duration)
        number_of_participants = 'Number of participants: {}\n'.format(self.number_of_participants)
        distance_in_meters = 'Distance in meters: {}\n'.format(self.distance_in_meters)
        return stage_duration + number_of_participants + distance_in_meters

class Running:
    def __init__(self, types_of_running = None):
        self.types_of_running = types_of_running

    def __del__(self):
        return

    def __str__(self):
        types_of_running = f'Types of running: {self.types_of_running}'
        return types_of_running

class Jumping:
    def __init__(self, types_of_jumping = None, jump_distance_in_centimeters = None):
        self.types_of_jumping = types_of_jumping
        self.jump_distance_in_centimeters = jump_distance_in_centimeters

    def __del__(self):
        return

    def __str__(self):
        types_of_jumping = f'Types of jumping: {self.types_of_jumping}'
        jump_distance_in_centimeters = f'Jump distance in centimeters: {self.jump_distance_in_centimeters}'
        return types_of_jumping + jump_distance_in_centimeters
