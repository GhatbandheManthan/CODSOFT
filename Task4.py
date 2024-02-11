import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(location):
    api_key = "1eb93e58f0c30af5c044c942d4ad7db0"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data
    except requests.RequestException as e:
        messagebox.showerror("Error", f"An error occurred while fetching data: {e}")
        return None

def display_weather(data):
    if data and data.get("cod") == 200:
        weather_text = f"Weather in {data['name']}:\n"
        weather_text += f"Temperature: {data['main']['temp']}°C\n"
        weather_text += f"Humidity: {data['main']['humidity']}%\n"
        weather_text += f"Wind Speed: {data['wind']['speed']} m/s\n"
        weather_text += f"Weather Description: {data['weather'][0]['description']}"
        text_output.config(state=tk.NORMAL)
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, weather_text)
        text_output.config(state=tk.DISABLED)
    elif data:
        error_message = data.get("message", "Unknown error occurred.")
        messagebox.showerror("Error", f"Error: {error_message}")
    else:
        messagebox.showerror("Error", "No data retrieved. Please check your internet connection or input.")

def get_weather():
    location = entry_location.get()
    weather_data = get_weather_data(location)
    display_weather(weather_data)

# Create main window
root = tk.Tk()
root.title("Weather Forecast App")

# Create input label and entry
label_location = tk.Label(root, text="Enter the name of a city or a zip code:")
label_location.pack(pady=5)
entry_location = tk.Entry(root, width=40)
entry_location.pack(pady=5)

# Create button to get weather
button_get_weather = tk.Button(root, text="Get Weather", command=get_weather)
button_get_weather.pack(pady=5)

# Create text widget to display weather output
text_output = tk.Text(root, width=50, height=10)
text_output.pack(pady=5)
text_output.config(state=tk.DISABLED)

root.mainloop()
