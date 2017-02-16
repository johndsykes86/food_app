from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connection=sqlite3.connect('database.db')
print('Database opened successfully')


connection.execute('CREATE TABLE IF NOT EXISTS posts(name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
print('Table created successfully')
connection.close()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/enternew')
def enter_new():
    return render_template('food.html')

@app.route('/addfood', methods=["POST"])
def addfood():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()

    try:
        food_name = request.form['name']
        food_cuisine = request.form['cuisine']
        food_calories = request.form['calories']
        food_is_vegan = request.form['is_vegetarian']
        food_is_gluten_free = request.form['is_gluten_free']
        cursor.execute('INSERT INTO posts (name, cuisine, calories, is_vegetarian, is_gluten_free) VALUES(?,?,?,?,?)',(food_name,food_cuisine,food_calories,food_is_vegan,food_is_gluten_free))
        connection.commit()
        message = "Data written successfully"
    except:
        connection.rollback()
        message = 'Error in insert operation'
    finally:
        return render_template('result.html', message = message)
        connection.close()
