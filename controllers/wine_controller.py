from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.wine import Wine
from models.producer import Producer
import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository

wine_blueprint = Blueprint("wines", __name__)

@wine_blueprint.route("/wines")
def wine_index():
    wines = wine_repository.select_all()
    return render_template("wine/index.html", all_wines=wines)


# NEW GET WINE ('/wine/new')
@wine_blueprint.route("/wines/new", methods=["GET"])
def new_wine():
    producers = producer_repository.select_all()
    return render_template("wine/new.html", producers = producers)


# create a route that handles a post request /wines which will create a new wine object and save it to the database

@wine_blueprint.route("/wines", methods=["POST"])
def create_wine():
    producer_id = request.form["producer_id"]
    grape_variety = request.form["grape_variety"]
    description = request.form["description"]
    cost_price = float(request.form["cost_price"])
    retail_price = float(request.form["retail_price"])
    stock = request.form["stock"]

    producer = producer_repository.select(producer_id)
    wine = Wine(
        grape_variety, 
        description, 
        cost_price, 
        retail_price, 
        stock, 
        producer)
    wine_repository.save(wine)
    return redirect("/wines")

@wine_blueprint.route('/wines/<id>/delete', methods=['POST'])
def delete_wine(id):
    wine_repository.delete(id)
    return redirect('/wines')