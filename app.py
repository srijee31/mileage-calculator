from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mileage_calculator():
    mileage = None
    liters_fueled = None
    price = ""
    amount = ""
    distance = ""

    if request.method == 'POST':
        try:
            price_val = float(request.form.get('price', 0))
            amount_val = float(request.form.get('amount', 0))
            distance_val = float(request.form.get('distance', 0))

            # Preserve submitted values in the input boxes
            price = request.form.get('price', '')
            amount = request.form.get('amount', '')
            distance = request.form.get('distance', '')

            if price_val > 0 and amount_val > 0 and distance_val > 0:
                # Total petrol in liters = Total amount spent / Price per liter
                liters_val = amount_val / price_val
                liters_fueled = round(liters_val, 2)

                # Mileage (km/L) = Total distance / Liters fueled
                mileage_val = distance_val / liters_val
                mileage = round(mileage_val, 2)
            else:
                mileage = "Invalid Input"
                liters_fueled = "N/A"
        except ValueError:
            mileage = "Error"
            liters_fueled = "N/A"

    return render_template(
        'index.html', 
        mileage=mileage, 
        liters_fueled=liters_fueled,
        price=price,
        amount=amount,
        distance=distance
    )

if __name__ == '__main__':
    app.run(debug=True)