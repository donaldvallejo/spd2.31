class Cooking:
    def __init__(self, time, temp, pressure, desired):
        self.well_done = 3000
        self.medium = 2500
        self.cooked_constant = 0.05
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.desired = desired

    def is_cookeding_criteria_satisfied(self):
        return is_well_done() or is_medium()

    def is_well_done(self):
        return self.desired == 'well-done' and  \
            get_cooking_progress() >= self.well_done

    def is_medium(self):
        return self.desired == 'medium' and  \
            get_cooking_progress() >= self.medium

    def get_cooking_progress(self):
        return self.time * self.temp * self.pressure * self.cooked_constant


TIME = 30 # [min]
TEMP = 103 # [celsius]
PRESSURE = 20 # [psi]
DESIRED_STATE = 'well-done'
COOKING = Cooking(TIME, TEMP, PRESSURE, DESIRED_STATE)

if COOKING.is_cookeding_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')
