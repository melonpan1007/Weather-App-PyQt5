import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
import requests

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: "Calibri";
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: "Segoe UI Emoji";
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self): 
        api_key = "YOUR_API_KEY_HERE" # Replace "YOUR_API_KEY_HERE" with your actual OpenWeather API key
        city = self.city_input.text().strip()

        if not city:
            self.display_error("Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            status_code = http_error.response.status_code if http_error.response else None
            match status_code:
                case 400:
                    self.display_error("Bad Request. Check the city name.")
                case 401:
                    self.display_error("Unauthorized. Check your API key.")
                case 402:
                    self.display_error("Payment Required. API limit may be reached.")
                case 403:
                    self.display_error("Access Forbidden. Contact support.")
                case 404:
                    self.display_error("City not found. Please check the spelling.")
                case 500:
                    self.display_error("Server error. Try again later.")
                case 502:
                    self.display_error("Bad gateway. Try again.")
                case 503:
                    self.display_error("Service unavailable. Please try again.")
                case 504:
                    self.display_error("Gateway timeout. Try again later.")
                case _:
                    self.display_error("An unexpected error occurred. Please try again.")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error. Check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Request timed out. Please try again.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects. Check the URL and try again.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: {req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px; color: red;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px; color: black;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "🌩️"  # Thunderstorm
        elif 300 <= weather_id <= 321:
            return "🌦️"  # Drizzle
        elif 500 <= weather_id <= 504:
            return "🌧️"  # Rain
        elif weather_id == 511:
            return "🧊"  # Freezing rain
        elif 520 <= weather_id <= 531:
            return "🌦️"  # Shower rain
        elif 600 <= weather_id <= 622:
            return "❄️"  # Snow
        elif 701 <= weather_id <= 711:
            return "🌫️"  # Mist/Smoke
        elif 721 <= weather_id <= 781:
            return "🌁"  # Haze/Dust/Fog
        elif weather_id == 800:
            return "☀️"  # Clear sky
        elif weather_id == 801:
            return "🌤️"  # Few clouds
        elif weather_id == 802:
            return "⛅️"  # Scattered clouds
        elif weather_id == 803:
            return "🌥️"  # Broken clouds
        elif weather_id == 804:
            return "☁️"  # Overcast clouds
        else:
            return "❓"  # Unknown

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
