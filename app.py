from flask import Flask, render_template, request, redirect, url_for
from models import db, Appointment

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    # Try to fetch existing appointments to verify connection
    appointments = Appointment.query.all()
    print(appointments)  # This should print a list of existing appointments (empty if none)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        department = request.form['department']
        doctor = request.form['doctor']

        # Create new appointment and add to database
        new_appointment = Appointment(name=name, email=email, phone=phone, date=date, department=department, doctor=doctor)
        db.session.add(new_appointment)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
