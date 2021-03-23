from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.wine import Wine
from models.producer import Producer
import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository

wine_blueprint = Blueprint("wines", __name__)

@wine_blueprint.route("/wines")
def wine_index():
    wine = wine_repository.select_all()
    return render_template("wines/index.html", all_wines = wine)


# NEW GET WINE ('/wine/new')
@wine_blueprint.route("/wines/new", methods=["GET"])
def new_wine():
    producers = producer_repository.select_all()
    return render_template("wines/new.html", all_producers = producers)


# create a route that handles a post request /wines which will create a new wine object and save it to the database
