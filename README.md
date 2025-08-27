✈️ Flightly – Cheap Flight Finder

**Flightly** is a Python-based flight search tool using the **Amadeus API**.  
Easily find affordable flights by entering origin, destination, travel date, and number of passengers.  
The program displays airline, departure & arrival times, and total price in INR.

---

## 🚀 Features
- 🔍 Search flights by origin & destination airport codes  
- 📅 Input your travel date  
- 👥 Specify number of passengers  
- 💰 Displays total price in INR  
- 🔄 Search multiple times in one run  

---

## 🛠️ Tech Stack
- **Python 3**  
- **Amadeus API**  

---

## 📂 Project Structure
```

Flightly/
│── Cheap Travel Plan.py        # Main script
│── README.md            # Documentation
│── .gitignore           # Ignore sensitive files

````

---

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/ASHWELL-CG/Flightly.git
cd Flightly
````

2. **Install dependencies**

```bash
pip install amadeus
```

3. **Get Amadeus API Credentials**

* Go to [Amadeus for Developers](https://developers.amadeus.com) and **sign up** for a free account.
* After logging in, go to **My Apps → Create New App**.
* Give your app a name (e.g., Flightly) and select **Flight Offers Search API**.
* Copy your **API Key (Client ID)** and **API Secret (Client Secret)**.

4. **Add API credentials**
   Edit `Cheap Travel Plan.py` and replace with your own credentials:

```python
amadeus = Client(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)
```

5. **Run the project**

```bash
Cheap Travel Plan.py
```

---

## 🖼️ Example Output

```
✈️ Airline: Air India
📍 Departure: 10 Oct 2025, 08:15 AM
📍 Arrival:   10 Oct 2025, 11:30 AM
💰 Price: ₹6,500
----------------------------------------
```

---

## 📌 Future Enhancements

* 🌍 Multi-currency support (USD, EUR, AED, etc.)
* ⏱️ Filters for cheapest/fastest flights
* 💻 Web interface using Flask or Streamlit
* 🤖 AI-powered flight search assistant

---

## 🤝 Contributing

Contributions are welcome!
Please fork the repository and submit a pull request for improvements.

