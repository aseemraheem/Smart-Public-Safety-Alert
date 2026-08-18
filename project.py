import time
from colorama import Fore, Style, init

init(autoreset=True)

# -------------------------------
# Countdown Function
# -------------------------------
def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(Fore.YELLOW + f"Time remaining: {i} seconds", end="\r")
        time.sleep(1)
    print()


# -------------------------------
# Traffic Light Class
# -------------------------------
class TrafficLight:
    def __init__(self, direction):
        self.direction = direction
        self.color = "RED"

    def set_green(self, time_duration):
        self.color = "GREEN"
        print(Fore.GREEN + f"{self.direction} light is GREEN for {time_duration} seconds")
        countdown(time_duration)

    def set_red(self):
        self.color = "RED"
        print(Fore.RED + f"{self.direction} light is RED")


# -------------------------------
# AI Controller
# -------------------------------
class AIController:
    def decide_priority(self, traffic_data):
        return max(traffic_data, key=traffic_data.get)


# -------------------------------
# Traffic Controller
# -------------------------------
class TrafficController:
    def __init__(self):
        self.lights = {
            "North": TrafficLight("North"),
            "South": TrafficLight("South"),
            "East": TrafficLight("East"),
            "West": TrafficLight("West")
        }
        self.ai = AIController()

    def reset_all(self):
        for light in self.lights.values():
            light.set_red()

    def handle_emergency(self):
        direction = input("Enter direction for Emergency (North/South/East/West): ")
        print(Fore.CYAN + "\n🚑 Emergency Activated!")
        self.reset_all()
        self.lights[direction].set_green(15)

    def handle_priority(self):
        direction = input("Enter direction for Priority Vehicle: ")
        print(Fore.MAGENTA + "\n🚓 Priority Vehicle Activated!")
        self.reset_all()
        self.lights[direction].set_green(12)

    def normal_operation(self):
        print("\nEnter Traffic Density (numbers):")
        traffic_data = {
            "North": int(input("North: ")),
            "South": int(input("South: ")),
            "East": int(input("East: ")),
            "West": int(input("West: "))
        }

        print(Fore.BLUE + f"Traffic Data: {traffic_data}")

        priority_direction = self.ai.decide_priority(traffic_data)
        print(Fore.YELLOW + f"AI Selected Direction: {priority_direction}")

        self.reset_all()

        green_time = traffic_data[priority_direction] // 2
        if green_time < 5:
            green_time = 5

        self.lights[priority_direction].set_green(green_time)

    def run(self):
        while True:
            print(Style.BRIGHT + "\n===== TRAFFIC CONTROL MENU =====")
            print("1. Normal Operation (AI)")
            print("2. Emergency Vehicle")
            print("3. Priority Vehicle")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.normal_operation()

            elif choice == "2":
                self.handle_emergency()

            elif choice == "3":
                self.handle_priority()

            elif choice == "4":
                print(Fore.RED + "Program Stopped.")
                break

            else:
                print(Fore.RED + "Invalid choice!")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    controller = TrafficController()
    controller.run()