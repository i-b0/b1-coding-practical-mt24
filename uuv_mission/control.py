# A Proportional-Derivative (PD) controller for UUVs. 
# The controller computes control inputs based on the error e[t] between the reference and current positions
# The controller proportional gain is Kp = 0.15 and the derivative gain is Kd = 0.6
class PDController:
    def __init__(self, Kp: float = 0.12, Kd: float = 0.7):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0
        self._initialised = False

    # Create a reset method to reset the previous error
    def reset(self):
        self.previous_error = 0.0
        self._initialised = False

    def compute_control(self, reference: float, current_position: float) -> float:
        error = reference - current_position

        # Check if this is the first call to avoid derivative kick
        if not self._initialised:
            derivative = 0.0
            self._initialised = True
        # Compute derivative of error
        derivative = (error - self.previous_error)
        control_input = self.Kp * error + self.Kd * derivative
        self.previous_error = error
        return control_input





