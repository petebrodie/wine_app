from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.wine import Wine
from models.producer import Producer
import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository

wine_blueprint = Blueprint("wines", __name__)

@wine_blueprint.route("/wines")
def wine():
    wine = wine_repository.select_all()
    return render_template("wines/index.html", all_wines = wine)


# NEW GET WINE ('/wine/new')
@wines_blueprint.route("/wines/new", methods=["GET"])
def new_wine():
    producer = producer_repository.select_all()
    return render_template("wines/new.html", all_producers = producers)