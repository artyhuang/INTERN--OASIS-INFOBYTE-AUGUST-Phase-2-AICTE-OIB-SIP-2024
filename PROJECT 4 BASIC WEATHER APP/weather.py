import requests
import tkinter as tk
from tkinter import messagebox

api_key = "af81412c297cf0138e5d8f0dfe82181a"

def get_weather():
    zip_code = zip_code_entry.get()
    country_code = country_code_entry.get()
    
    if zip_code and country_code:
        weather_data, api_stat = current_weather_by_ZIP(zip_code, country_code, api_key)
        
        if api_stat == 200:
            description = weather_data['weather'][0]['description']
            city = weather_data['name']
            temperature = weather_data['main']['temp']
            temp_max = weather_data['main']['temp_max']
            temp_min = weather_data['main']['temp_min']
            wind_speed = weather_data['wind']['speed']
            humidity = weather_data['main']['humidity']

            weather_info.config(
                text=f'The current temperature in {city} is {temperature}°C and weather condition is {description}.\n'
                     f"Today's highest temperature is {temp_max}°C and lowest temperature is {temp_min}°C.\n"
                     f'The climate is {humidity}% humid.\n'
                     f'The speed of wind is {wind_speed} m/s.'
            )
        else:
            messagebox.showerror("Error", "City not found or invalid API response.")
    else:
        messagebox.showwarning("Input Error", "Please enter both ZIP code and country code.")

def current_weather_by_ZIP(zip_code, country_code, api_key):
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&units=metric&appid={api_key}')
    return result.json(), result.status_code
root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")
zip_code_label = tk.Label(root, text="Enter ZIP Code:")
zip_code_label.pack(pady=5)
zip_code_entry = tk.Entry(root)
zip_code_entry.pack(pady=5)
country_code_label = tk.Label(root, text="Enter Country Code:")
country_code_label.pack(pady=5)
country_code_entry = tk.Entry(root)
country_code_entry.pack(pady=5)
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)
weather_info = tk.Label(root, text="", wraplength=400, justify="left")
weather_info.pack(pady=10)
root.mainloop()
