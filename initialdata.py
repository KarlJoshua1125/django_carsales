import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("carsales-admin-key.json")
firebase_admin.initialize_app(cred, {
    # Your database URL
    "databaseURL": "https://carsalesproject-e94ec-default-rtdb.firebaseio.com"
})

dbref = db.reference("CarsList")
dbref.push({"ID": 1, "Name": "Toyota Camry", "Year": 2018, "Price": 2000})
dbref.push({"ID": 2, "Name": "Honda Civic", "Year": 2019, "Price": 2200})
dbref.push({"ID": 3, "Name": "Chevrolet Silverado",
           "Year": 2017, "Price": 1800})
dbref.push({"ID": 4, "Name": "Ford F-150", "Year": 2020, "Price": 2500})
dbref.push({"ID": 5, "Name": "Nissan Altima", "Year": 2021, "Price": 3000})

print(dbref.get())
{'-NStGHVsdVrTzVAAxzq5': {'ID': 1, 'Name': 'Toyota Camry', 'Price': 2000, 'Year': 2018}, '-NStGHZZjP61Tge3Rq9N': {'ID': 2, 'Name': 'Honda Civic', 'Price': 2200, 'Year': 2019}, '-NStGHc-GiuYGyadmChe': {'ID': 3,
                                                                                                                                                                                                         'Name': 'Chevrolet Silverado', 'Price': 1800, 'Year': 2017}, '-NStGHfd-wO6GkYF8Xsl': {'ID': 4, 'Name': 'Ford F-150', 'Price': 2500, 'Year': 2020}, '-NStGHjBAsQnWKq5qhI7': {'ID': 5, 'Name': 'Nissan Altima', 'Price': 3000, 'Year': 2021}}
