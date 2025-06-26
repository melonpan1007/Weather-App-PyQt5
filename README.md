# ☁️ Accurate Weather App (PyQt5)

A sleek and accurate weather app built with PyQt5 that fetches real-time weather data based on city name input using the OpenWeatherMap API.

## 🚀 Features

- 🌍 Search any city and get real-time weather updates.
- 🌡️ Displays current temperature in Celsius.
- 🌥️ Shows weather condition with appropriate emoji.
- 🔄 Handles a wide range of errors with specific messages:
  - Invalid city names (e.g., typos like `mumabi`)
  - Empty input field
  - API errors (invalid key, rate limit, etc.)
  - Server or connection issues

---

## 🖼️ Preview

### ✅ Working Example:
![screenshot png](https://github.com/user-attachments/assets/ab12b8fb-e5bf-4547-843f-957133d96277)

### ❌ Error Handling (invalid city):
![error_screenshot png](https://github.com/user-attachments/assets/fba6704d-fa72-452f-8275-bf679d8b117f)

## 📦 Installation

First, clone the repository:

```bash
git clone https://github.com/melonpan1007/Weather-App-PyQt5.git
cd Weather-App-PyQt5
````

Then, install the required packages:

```bash
pip install -r requirements.txt
```

> Make sure Python 3 and `pip` are installed on your system.

---

## ▶️ Running the App

Replace the API key in `weather_app.py`:

```python
api_key = "YOUR_API_KEY_HERE"
```

Then run the app using:

```bash
python weather_app.py
```

---

## ❗ Notes

* 🔑 **API Key Required**: This app uses the free [OpenWeatherMap API](https://openweathermap.org/api). Sign up, get your API key, and paste it in the script.
* ⌛ Activation Delay: Your API key may take a few minutes to go live after creation.
* 📝 Input Matters: Spelling errors (e.g., `mumabi` instead of `mumbai`) will return a "City not found" message.
* 📊 Accuracy: Data is fetched directly from OpenWeatherMap’s live weather feed and may slightly vary depending on refresh cycles.

> 🛡️ The code includes detailed error handling using `match-case` and exception blocks to help users understand exactly what went wrong. From server errors to invalid input — you’re covered!

---

## 📁 File Structure

```
Weather-App-PyQt5/
│
├── weather_app.py          # Main Python app
├── requirements.txt        # Required Python packages
├── screenshots/
│   ├── success_ui.png      # Screenshot showing correct weather
│   └── error_ui.png        # Screenshot showing error handling
└── README.md
```

---

## 🧠 Technologies Used

* Python 3
* PyQt5
* OpenWeatherMap API
* Requests

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 👤 Author

Made with ❤️ by [melonpan1007](https://github.com/melonpan1007)

````
