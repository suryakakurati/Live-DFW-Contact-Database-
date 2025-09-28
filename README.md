A Flask web app to manage, search, and add service contacts in the Dallas-Fort Worth area using CSV files.

Features

🔍 Search contacts by Service or Name

📄 View detailed Profile for each contact

➕ Add new service contacts with full details (phone, service, email, website, rating, comments)

📋 Dynamic services list from Services.csv

🌐 Live Demo Available at https://suryeah.pythonanywhere.com

Project Structure
mysite/
│
├─ People.csv          # Contact details
├─ Services.csv        # List of services
├─ flask_app.py        # Main Flask app
├─ static/Logo.jpg     # Logo image
└─ templates/
    ├─ Add.html
    ├─ Profile.html
    ├─ Search.html
    └─ results.html

Setup & Installation
# Clone repo
git clone https://github.com/suryakakurati/Live-DFW-Contact-Database-.git
cd mysite

# Create virtual environment
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install flask pandas

Run the App Locally
python flask_app.py


Open your browser at:

http://127.0.0.1:5000/


Or access the live demo directly: [https://suryeah.pythonanywhere.com](url)

Usage

Search for a contact by Service or Name.

Click a contact to view full details.

Add a new contact via the Add Contact page.

Notes

CSV files act as the database.

Admin password set in flask_app.py as app.config['ADMIN_PASSWORD'] = 'admin'.

Ignore __pycache__ files—they are auto-generated.
