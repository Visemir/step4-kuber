# app.py
from flask import Flask, render_template, request, redirect, url_for
from shop import PetShop

app = Flask(__name__)

# Database connection details
host = "mysql-server"
user = "petshop"
password = "12345qazwsxed"

# Initialize PetShop
petshop = PetShop(host, user, password)
petshop.create_shop()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Add pet - show form and handle submission
@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        if not name or not price:
            return render_template('add_pet.html', error="Please provide both name and price.")
        
        ids = petshop.add_item(name, price)
        return render_template('add_pet.html', success=f"Pet added with ID(s): {ids}")

    return render_template('add_pet.html')

# Delete pet by ID - show form and handle submission
@app.route('/delete_pet', methods=['GET', 'POST'])
def delete_pet():
    if request.method == 'POST':
        id = request.form['id']

        if not id:
            return render_template('delete_pet.html', error="Please provide an ID.")

        pet = petshop.delete_item_by_id(id)
        if not pet:
            return render_template('delete_pet.html', error="Pet not found!.")

        # If the pet exists, delete it
        res = petshop.delete_item_by_id(id)
        return render_template('delete_pet.html', success="Pet deleted successfully." if res else "Pet deleted successfully.")


 
    return render_template('delete_pet.html')

# Show list of pets
@app.route('/list_pets')
def list_pets():
    query = "SELECT * FROM pets"
    pets = petshop.query(query)
    return render_template('list_pets.html', pets=pets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


