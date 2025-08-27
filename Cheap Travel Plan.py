from amadeus import Client, ResponseError
from datetime import datetime

# Initialize Amadeus client
amadeus = Client(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)

# Airline Code Dictionary
AIRLINE_NAMES = {
    "AI": "Air India",
    "IX": "Air India Express",
    "QP": "Akasa Air",
    "6E": "IndiGo",
    "SG": "SpiceJet",
    "I5": "AirAsia India",
    "G8": "GoFirst",
    "UK": "Vistara",
    "DN": "Deccan Charters",
    "BZ": "Blue Dart Aviation",
    "GF": "Gulf Air",
    "WY": "Oman Air",
    "SV": "Saudia",
    "G9": "Air Arabia",
    "EY": "Etihad Airways",
    "OV": "SalamAir"
}

# ----------------- Flight Search -----------------
def find_cheapest_flight(origin, destination, depart_date, adults):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin.upper(),
            destinationLocationCode=destination.upper(),
            departureDate=depart_date,
            adults=adults,
            max=5,  # limit to 5 results
            currencyCode="INR"
        )

        flights = response.data
        for flight in flights:
            price = float(flight['price']['total'])
            airline_code = flight['itineraries'][0]['segments'][0]['carrierCode']
            airline = AIRLINE_NAMES.get(airline_code, airline_code)

            dep = flight['itineraries'][0]['segments'][0]['departure']['at']
            arr = flight['itineraries'][0]['segments'][0]['arrival']['at']
            dep_time = datetime.fromisoformat(dep).strftime("%d %b %Y, %I:%M %p")
            arr_time = datetime.fromisoformat(arr).strftime("%d %b %Y, %I:%M %p")

            print(f"✈️ Airline: {airline}")
            print(f"📍 Departure: {dep_time}")
            print(f"📍 Arrival:   {arr_time}")
            print(f"💰 Price: ₹{int(price):,}")
            print("-" * 40)

    except ResponseError as error:
        print("Error fetching flights:", error)
# ----------------- Main Program -----------------
if __name__ == "__main__":
    print("Welcome to the Flightly Cheap Travel Plan Finder!")

    while True:
        origin = input("\nEnter origin airport code (e.g., DXB): ").strip()
        destination = input("Enter destination airport code (e.g., DEL): ").strip()
        depart_date = input("Enter departure date (YYYY-MM-DD): ").strip()
        adults = int(input("Enter number of adults: ").strip())

        find_cheapest_flight(origin, destination, depart_date, adults)

        again = input("\nDo you want to search again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Flightly Cheap Travel Plan Finder!")
            break