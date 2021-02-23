ELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05
TIME = 30 # [min]
TEMP = 103 # [celcius]
PRESSURE = 20 # [psi]
DESIRED_STATE = 'well-done'
class CookType:
    def __init__(self, is_cooking_criteria_satisfied, get_cooking_progress):
        self.check_cooking = CheckCooking(is_cooking_criteria_satisfied, get_cooking_progress)
    def is_well_done(time, temperature, pressure, desired_state):    
        return desired_state == 'well-done' and  \
            self.check_cooking.get_cooking_progress(time, temperature, pressure) >= WELL_DONE
    def is_medium(time, temperature, pressure, desired_state):
        return desired_state == 'medium' and  \
            self.check_cooking.get_cooking_progress(time, temperature, pressure) >= MEDIUM
class CheckCooking:
    def __init__(self, is_well_done, is_medium):
        self.cook_type = CookType(is_well_done, is_medium)
    def is_cooking_criteria_satisfied(time, temperature, 
                                        pressure, desired_state):
        return is_well_done(time, temperature, pressure, desired_state) or \
            is_medium(time, temperature, pressure, desired_state)
    def get_cooking_progress(time, temperature, pressure):
        return time * temperature * pressure * COOKED_CONSTANT
    if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
        print('cooking is done.')
    else:
        print('ongoing cooking.')