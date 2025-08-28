# Base Class (Parent)
class Smartwatch:
    # Constructor to initialize attributes
    def __init__(self, brand, model, display_size, battery_life):
        self.brand = brand              # Brand name of the smartwatch
        self.model = model              # Model of the smartwatch
        self.display_size = display_size  # Display size in inches
        self.battery_life = battery_life  # Battery life in hours
        self.is_on = False              # Tracks if the watch is powered on

    # Method to power on/off the smartwatch
    def toggle_power(self):
        self.is_on = not self.is_on
        status = "on" if self.is_on else "off"
        print(f" {self.brand} {self.model} is now powered {status}.")

    # Method to display watch details
    def info(self):
        if not self.is_on:
            print(f" {self.brand} {self.model} is powered off. Please turn it on.")
            return
        print(f" {self.brand} {self.model}")
        print(f"   Display: {self.display_size} inches")
        print(f"   Battery Life: {self.battery_life} hours")

    # Method to check notifications
    def check_notifications(self, app):
        if not self.is_on:
            print(f" Cannot check notifications. {self.brand} {self.model} is powered off.")
            return
        print(f" Checking notifications from {app} on {self.brand} {self.model}...")


# Child Class (Inheritance Example)
class FitnessSmartwatch(Smartwatch):
    # Constructor with extra attributes
    def __init__(self, brand, model, display_size, battery_life, heart_rate_monitor, step_counter):
        super().__init__(brand, model, display_size, battery_life)
        self.heart_rate_monitor = heart_rate_monitor  # Boolean: has heart rate monitor
        self.step_counter = step_counter              # Current step count
        self.calories_burned = 0                     # Tracks calories burned

    # Overriding info method to include fitness features
    def info(self):
        if not self.is_on:
            print(f" {self.brand} {self.model} is powered off. Please turn it on.")
            return
        super().info()
        print(f"   Heart Rate Monitor: {'Yes' if self.heart_rate_monitor else 'No'}")
        print(f"   Steps: {self.step_counter}")
        print(f"   Calories Burned: {self.calories_burned} kcal")

    # Overriding check_notifications to prioritize fitness apps
    def check_notifications(self, app):
        if not self.is_on:
            print(f" Cannot check notifications. {self.brand} {self.model} is powered off.")
            return
        print(f" {self.brand} {self.model} is checking fitness updates from {app}...")

    # New method unique to FitnessSmartwatch
    def track_workout(self, activity, duration_minutes):
        if not self.is_on:
            print(f" Cannot track workout. {self.brand} {self.model} is powered off.")
            return
        try:
            duration = float(duration_minutes)
            if duration <= 0:
                raise ValueError("Duration must be positive.")
            # Simulate calorie calculation (e.g., 10 kcal per minute for simplicity)
            calories = duration * 10
            self.calories_burned += calories
            self.step_counter += int(duration * 100)  # Simulate 100 steps per minute
            print(f" {self.brand} {self.model} tracked {activity} for {duration} minutes.")
            print(f"   Steps added: {int(duration * 100)}, Calories burned: {calories} kcal")
        except ValueError as e:
            print(f" Error: {e}. Please enter a valid duration.")


# Creating Objects (Instances)
watch1 = Smartwatch("Apple", "Watch Series 8", 1.9, 18)
watch2 = FitnessSmartwatch("Garmin", "Forerunner 255", 1.3, 24, True, 0)

# Using the Objects
print("=== Standard Smartwatch ===")
watch1.toggle_power()  # Turn on
watch1.info()
watch1.check_notifications("Messages")
watch1.toggle_power()  # Turn off
watch1.info()  # Should show powered-off message

print("\n=== Fitness Smartwatch ===")
watch2.toggle_power()  # Turn on
watch2.info()
watch2.check_notifications("Strava")
watch2.track_workout("Running", 30)
watch2.info()  # Show updated steps and calories
watch2.track_workout("Cycling", -5)  # Test error handling
watch2.toggle_power()  # Turn off