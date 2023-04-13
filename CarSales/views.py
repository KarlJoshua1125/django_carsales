from django.shortcuts import render, redirect
from django.apps import apps
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from .forms import CarForm


def connectDB():
    if not firebase_admin._apps:
        cred = credentials.Certificate("carsales-admin-key.json")
        firebase_admin.initialize_app(cred, {
            # Your database URL
            "databaseURL": "https://carsalesproject-e94ec-default-rtdb.firebaseio.com/"
        })
    dbconn = db.reference("CarsList")
    return dbconn


def carslist(request):
    cars = []
    dbconn = connectDB()
    tblCars = dbconn.get()
    for key, value in tblCars.items():
        cars.append({"id": value["ID"], "name": value["Name"],
                    "year": value["Year"], "price": value["Price"]})
    return render(request, 'carslist.html', {'cars': cars})


def addcar(request):
    if request.method == 'GET':
        return render(request, 'addcar.html')
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            name = form.cleaned_data.get("name")
            year = form.cleaned_data.get("year")
            price = form.cleaned_data.get("price")
        dbconn = connectDB()
        dbconn.push({"ID": id, "Name": name, "Year": year, "Price": price})
        return redirect('carslist')

def updatecar(request, id):
    cr = []
    dbconn = connectDB()
    tblCars = dbconn.get()

    if request.method == 'GET':
        for key, value in tblCars.items():
            if (value["ID"] == id):
                global updatekey
                updatekey = key
                cr.append({"id": value["ID"], "name": value["Name"],
                          "year": value["Year"], "price": value["Price"]})
        return render(request, 'addcar.html', {'car': cr[0]})
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data.get("name"))
            year = int(form.cleaned_data.get("year"))
            price = float(form.cleaned_data.get("price"))
            updateitem = dbconn.child(updatekey)
            updateitem.update(
                {"ID": id, "Name": name, "Year": year, "Price": price})
        return render(request, 'addcar.html', {'car':{}})
    
def deletecar(request, id):
    dbconn = connectDB()
    tblCars = dbconn.get()
    for key, value in tblCars.items():
        if(value["ID"] == id):
            deletekey = key
            break
    delitem = dbconn.child(deletekey)
    delitem.delete()
    return redirect('carslist')
