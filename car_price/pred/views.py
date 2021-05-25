import pickle
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
# import pickle
from django.contrib.auth.decorators import login_required


# load data set
df = pd.read_csv("data/car_preprocessing.csv")


# Split data
X = df.drop('Price', axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=51)

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

# Load Model
model = joblib.load('old_car_price_prediction_model.pkl')

# it help to get predicted value of hosue  by providing features value


def predict_price(Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Mileage, Engine, Seats, Name):

    x=np.zeros(len(X.columns))  # create zero numpy array

    # adding feature's value accorind to their column index
    x[0]=Year
    x[1]=Kilometers_Driven
    x[2]=Fuel_Type
    x[3]=Transmission
    x[4]=Owner_Type
    x[5]=Mileage
    x[6]=Engine
    x[7]=Seats

    if Name in X.columns:
        name_index=np.where(X.columns == Name)[0][0]
        x[name_index]=1

        # print(x)
            # feature scaling
    x=sc.transform([x])[0]
        # print(x)

        # return the predicted value by train xgboost Regrssion model
    return model.predict([x])[0]
# Create your views here.


@login_required(login_url='/login/')
def index(request):
    context={'a': 'hello'}
    return render(request, 'main.html', context)

def predict(request):
    if request.method == 'POST':
        Year=request.POST.get('year')
        Kilometers_Driven=request.POST.get('kilometers_driven')
        Fuel_Type=request.POST.get('fuel_type')
        Transmission=request.POST.get('transmission')
        Owner_Type=request.POST.get('owner_type')
        Mileage=request.POST.get('mileage')
        Engine=request.POST.get('engine')
        Seats=request.POST.get('seats')
        Name=request.POST.get('name')

        f_price=predict_price(Year, Kilometers_Driven, Fuel_Type,
                                Transmission, Owner_Type, Mileage, Engine, Seats, Name)
        price=round(f_price*100000, 2)
        # render the html page and show the output
        return render(request, 'result.html', {'prediction_price': price})
