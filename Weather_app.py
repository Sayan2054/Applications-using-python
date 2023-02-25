import requests
from tkinter import *
from tkinter import messagebox

# function to get weather data
def get_weather():
    # get user input for city name
    city = city_entry.get()

    # API url to fetch weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=<API_KEY>"

    try:
        # get weather data from API
        response = requests.get(url)
        data = response.json()

        # extract relevant weather information
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        # update the weather label
        weather_label.config(text=f"{city}: {temp}°C, {desc.capitalize()}")

    except Exception as e:
        # show error message if city is not found
        messagebox.showerror("Error", f"City not found: {city}")

# create tkinter window
window = Tk()
window.title("Weather Application")

# create city entry field
city_entry = Entry(window, font=("Arial", 14), width=20)
city_entry.pack(pady=20)

# create button to get weather data
get_weather_button = Button(window, text="Get Weather", font=("Arial", 14), command=get_weather)
get_weather_button.pack()

# create label to show weather data
weather_label = Label(window, font=("Arial", 18))
weather_label.pack(pady=20)

# run the window
window.mainloop()
