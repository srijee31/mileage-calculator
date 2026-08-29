from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mileage_calculator():
    mileage = None
    liters_fueled = None
    cost_per_km = None
    health_status = None
    health_color = None
    price = ""
    amount = ""
    distance = ""

    if request.method == 'POST':
        try:
            price_val = float(request.form.get('price', 0))
            amount_val = float(request.form.get('amount', 0))
            distance_val = float(request.form.get('distance', 0))

            price = request.form.get('price', '')
            amount = request.form.get('amount', '')
            distance = request.form.get('distance', '')

            if price_val > 0 and amount_val > 0 and distance_val > 0:
                # Total petrol in liters
                liters_val = amount_val / price_val
                liters_fueled = round(liters_val, 2)

                # Mileage (km/L)
                mileage_val = distance_val / liters_val
                mileage = round(mileage_val, 2)

                # Cost per kilometer (₹ / km)
                cost_val = amount_val / distance_val
                cost_per_km = round(cost_val, 2)

                # Mileage Health Tag Logic
                if mileage_val > 40:
                    health_status = "Excellent Efficiency"
                    health_color = "green"
                elif 35 <= mileage_val <= 40:
                    health_status = "Moderate Efficiency"
                    health_color = "yellow"
                else:
                    health_status = "Low Efficiency"
                    health_color = "red"
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
        cost_per_km=cost_per_km,
        health_status=health_status,
        health_color=health_color,
        price=price,
        amount=amount,
        distance=distance
    )

if __name__ == '__main__':
    app.run(debug=True)