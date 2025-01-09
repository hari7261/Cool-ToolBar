import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from datetime import datetime, timedelta
import requests
import pyttsx3


class FloatingToolbarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Calendar Toolbar")
        self.root.geometry("300x400")
        self.root.configure(bg="#1e1e1e")
        self.root.attributes("-topmost", True)  # Make the window always on top

        # Set a futuristic font
        self.custom_font = ("Helvetica", 12, "bold")

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Weather API key
        self.api_key = "e9ab59fb6863fd7d3a55b2763bc489f3"  # Replace with your OpenWeatherMap API key

        # Create buttons for each feature
        self.create_buttons()

        # Update the date and weather initially
        self.update_date()
        self.update_weather()

    def create_buttons(self):
        """Create buttons for each feature."""
        # Button to display the current date
        date_button = ttk.Button(
            self.root,
            text="Show Date",
            command=self.show_date,
            style="Futuristic.TButton",
        )
        date_button.pack(pady=10)

        # Button to display the weather
        weather_button = ttk.Button(
            self.root,
            text="Show Weather",
            command=self.show_weather,
            style="Futuristic.TButton",
        )
        weather_button.pack(pady=10)

        # Button to add a task reminder
        task_button = ttk.Button(
            self.root,
            text="Add Task Reminder",
            command=self.add_task,
            style="Futuristic.TButton",
        )
        task_button.pack(pady=10)

        # Button to read the date aloud
        voice_button = ttk.Button(
            self.root,
            text="Read Date Aloud",
            command=self.read_date,
            style="Futuristic.TButton",
        )
        voice_button.pack(pady=10)

        # Button to set a countdown timer
        countdown_button = ttk.Button(
            self.root,
            text="Set Countdown Timer",
            command=self.set_countdown,
            style="Futuristic.TButton",
        )
        countdown_button.pack(pady=10)

        # Configure the style for a futuristic look
        self.style = ttk.Style()
        self.style.configure(
            "Futuristic.TButton",
            font=self.custom_font,
            foreground="#00ff00",
            background="#333333",
            borderwidth=0,
            focuscolor="#00ff00",
        )
        self.style.map(
            "Futuristic.TButton",
            background=[("active", "#555555")],
            foreground=[("active", "#00ff00")],
        )

    def update_date(self):
        """Update the date label with the current date."""
        now = datetime.now()
        self.current_date = now.strftime("%A, %B %d, %Y")
        self.root.after(1000, self.update_date)  # Update every second

    def update_weather(self):
        """Fetch and update the current weather."""
        city = "New York"  # Replace with your city
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            self.current_weather = f"{weather}, {temperature}°C"
        except Exception as e:
            self.current_weather = "Weather: Unavailable"
        self.root.after(60000, self.update_weather)  # Update every minute

    def show_date(self):
        """Display the current date in a message box."""
        messagebox.showinfo("Current Date", self.current_date)

    def show_weather(self):
        """Display the current weather in a message box."""
        messagebox.showinfo("Current Weather", self.current_weather)

    def add_task(self):
        """Add a task reminder."""
        task = simpledialog.askstring("Add Task", "Enter your task:")
        if task:
            messagebox.showinfo("Task Added", f"Task '{task}' has been added!")

    def read_date(self):
        """Read the current date aloud."""
        self.engine.say(f"Today's date is {self.current_date}")
        self.engine.runAndWait()

    def set_countdown(self):
        """Set a countdown timer."""
        event_name = simpledialog.askstring("Set Countdown", "Enter event name:")
        if event_name:
            event_time = simpledialog.askstring("Set Countdown", "Enter event time (YYYY-MM-DD HH:MM:SS):")
            try:
                event_time = datetime.strptime(event_time, "%Y-%m-%d %H:%M:%S")
                self.start_countdown(event_name, event_time)
            except ValueError:
                messagebox.showerror("Error", "Invalid date format!")

    def start_countdown(self, event_name, event_time):
        """Start the countdown timer."""
        now = datetime.now()
        if event_time > now:
            time_left = event_time - now
            messagebox.showinfo("Countdown", f"Time left for {event_name}: {time_left}")
            self.root.after(1000, lambda: self.start_countdown(event_name, event_time))
        else:
            messagebox.showinfo("Countdown", f"Event {event_name} has passed!")


# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FloatingToolbarApp(root)
    root.mainloop()
