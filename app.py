from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('e_commerce_rf.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        Customer_care_calls = int(request.form['Customer_care_calls'])

        Customer_rating = int(request.form['Customer_rating'])

        Cost_of_the_Product = int(request.form['Cost_of_the_Product'])

        Weight_in_gms = int(request.form['Weight_in_gms'])

        Discount_offered = float(request.form['Discount_offered'])

        Prior_purchases = float(request.form['Prior_purchases'])

        Warehouse_block = request.form['Warehouse_block']
        if (Warehouse_block == 'B'):
            WH_Block_B = 1
            WH_Block_C = 0
            WH_Block_D = 0
            WH_Block_E = 0

        elif (Warehouse_block == 'C'):
            WH_Block_B = 0
            WH_Block_C = 1
            WH_Block_D = 0
            WH_Block_E = 0

        elif (Warehouse_block == 'D'):
            WH_Block_B = 0
            WH_Block_C = 0
            WH_Block_D = 1
            WH_Block_E = 0

        elif (Warehouse_block == 'E'):
            WH_Block_B = 0
            WH_Block_C = 0
            WH_Block_D = 0
            WH_Block_E = 1

        else:
            WH_Block_B = 0
            WH_Block_C = 0
            WH_Block_D = 0
            WH_Block_E = 0

        Mode_of_Shipment = request.form['Mode_of_Shipment']
        if (Mode_of_Shipment == 'Road'):
            Mode_of_S_Road = 1
            Mode_of_S_Ship = 0

        elif (Mode_of_Shipment == 'Ship'):
            Mode_of_S_Road = 0
            Mode_of_S_Ship = 1

        else:
            Mode_of_S_Road = 0
            Mode_of_S_Ship = 0

        Gender = request.form['Gender']
        if (Gender == 'M'):
            Gender_M = 1

        else:
            Gender_M = 0

        Product_Importance = request.form['Product_Importance']
        if (Product_Importance == 'Low'):
            Product_Importance = 0

        elif (Product_Importance == 'Medium'):
            Product_Importance = 1

        elif (Product_Importance == 'High'):
            Product_Importance = 2

        prediction = model.predict([[Customer_care_calls, Customer_rating, Cost_of_the_Product, Weight_in_gms,
                                     Discount_offered, Prior_purchases, WH_Block_B, WH_Block_C, WH_Block_D, WH_Block_E,
                                     Mode_of_S_Road, Mode_of_S_Ship, Gender_M, Product_Importance]])

        output = prediction

        if output == 0:
            return render_template('index.html', prediction_text="The order will reach on time")
        elif output == 1:
            return render_template('index.html', prediction_text="The order probably won't reach on time")
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)