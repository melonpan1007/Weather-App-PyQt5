# 🌦️  Weather App (PyQt5 + OpenWeatherMap)

A simple and elegant desktop weather app built using **Python** and **PyQt5**. It allows users to enter a city name and get the **current temperature**, **weather description**, and a **matching icon**, all powered by the **OpenWeatherMap API**.

---

## 🖼️ Preview

### ✅ Working Example:
![Weather App Screenshot](![screenshot png](https://github.com/user-attachments/assets/ab12b8fb-e5bf-4547-843f-957133d96277))

### ❌ Error Handling (invalid city):
![City Not Found](![error_screenshot png](https://github.com/user-attachments/assets/fba6704d-fa72-452f-8275-bf679d8b117f))



---

## 🔧 Features

✅ Search by city name  
✅ Displays current temperature in Celsius  
✅ Shows weather description and icon  
✅ Error handling for invalid city names  
✅ Clean and minimal GUI with PyQt5

---

## 🧰 Tech Stack

- Python
- PyQt5
- OpenWeatherMap API
- Requests module

---

## 📦 Installation

First, clone the repository:

```bash
git clone https://github.com/yourusername/accurate-weather-app.git
cd accurate-weather-app
````

Then, install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 Get Your API Key

1. Go to [https://openweathermap.org/](https://openweathermap.org/)
2. Create a free account
3. Go to the **API keys** section in your dashboard
4. Copy your key
5. Replace `"your_api_key_here"` in the code with your actual API key:

```python
API_KEY = "your_api_key_here"
```

---

## 🚀 Run the App

```bash
python weather_app.py
```

---

## 📝 Example Usage

* Input: `mumbai`
* Output:

  * 🌡️ Temperature: `28°C`
  * ☁️ Description: `Overcast clouds`
  * 📷 Weather icon

---

## ❗ Notes

* Make sure your API key is active (sometimes it takes a few hours after creation).
* Spelling matters! The app will show `"City not found"` if there's a typo like `"mumabi"` instead of `"mumbai"`.
* Accuracy may vary slightly based on OpenWeatherMap's real-time data refresh rate.

---

## 📁 Project Structure

```
accurate-weather-app/
│
├── weather_app.py
├── README.md
├── requirements.txt
└── screenshot.png
```

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).





