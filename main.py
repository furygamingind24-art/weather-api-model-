import requests

# 1. Get the city name from the user as a clean string text
city_name = input("Whats the name of the city? ").strip()

# 2. Stitch the city name variable directly into the URL template using an f-string
url = f"https://wttr.in/{city_name}?format=j1"

print(f"\n🔍 Connecting to the weather server for {city_name}...")

# 3. Set up our multi-tier safety net to run the network tasks safely
try:
    response = requests.get(url, timeout=10)

    #
    response.raise_for_status()

    weather_data = response.json()


    current = weather_data["current_condition"][0]
    temp_c = current["temp_C"]
    condition = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]

    print("\n" + "=" * 35)
    print(f"🌍 Weather Report for {city_name.title()}:")
    print(f"🌡️  Temperature : {temp_c}°C")
    print(f"☁️  Condition   : {condition}")
    print(f"💧 Humidity    : {humidity}%")
    print("=" * 35)


except requests.exceptions.ConnectionError:
    print("\n❌ Network Error: Could not connect to the internet. Please check your connection.")

except requests.exceptions.HTTPError:
    print(f"\n❌ Location Error: Could not find any weather records for '{city_name}'. Check your spelling!")

except (KeyError, IndexError):
    print("\n❌ Data Error: The weather server sent back data in an unexpected format.")

