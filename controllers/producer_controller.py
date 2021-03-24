from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.wine import Wine
from models.producer import Producer
import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository

wine_blueprint = Blueprint("wines", __name__)

@producer_blueprint.route("/producers")
def producer_index():
    producers = producer_repository.select_all()
    return render_template("producer/index.html", all_producers=producers)


# # NEW GET PRODUCER ('/producer/new')
@producer_blueprint.route("/producers/new", methods=["GET"])
def new_producer():
    wines = wine_repository.select_all()
    return render_template("producer/new.html", wines=wines)





# @wine_blueprint.route("/wines/new", methods=["GET"])
# def new_wine():
#     producers = producer_repository.select_all()
#     return render_template("wine/new.html", producers = producers)