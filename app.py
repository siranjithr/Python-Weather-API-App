import requests
from config import API_KEY, BASE_URL, UNITS


def get_weather(city):
    """
    Fetch weather information for the given city.
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": UNITS
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print("\n" + "=" * 45)
        print("        🌦 Weather Report")
        print("=" * 45)
        print(f"📍 Location     : {city_name}, {country}")
        print(f"🌡 Temperature : {temperature} °C")
        print(f"🥵 Feels Like  : {feels_like} °C")
        print(f"☁ Condition   : {weather}")
        print(f"💧 Humidity    : {humidity}%")
        print(f"🌬 Wind Speed  : {wind_speed} m/s")
        print(f"🧭 Pressure    : {pressure} hPa")
        print("=" * 45)

    except requests.exceptions.HTTPError:
        print("\n❌ City not found. Please enter a valid city name.")

    except requests.exceptions.ConnectionError:
        print("\n❌ Internet connection error.")

    except requests.exceptions.Timeout:
        print("\n❌ Request timed out.")

    except Exception as error:
        print(f"\n❌ Unexpected Error: {error}")


def main():

    print("=" * 45)
    print("      🌍 Python Weather API App")
    print("=" * 45)

    while True:

        city = input("\nEnter City Name (or 'exit'): ").strip()

        if city.lower() == "exit":
            print("\n👋 Thank you for using the Weather App!")
            break

        if city == "":
            print("⚠ City name cannot be empty.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()