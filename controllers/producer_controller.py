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


@producer_blueprint.route("/producers", methods=["POST"])
def create_producer():
    name = request.form["name"]
    phone_number = request.form["phone_number"]
    email = request.form["email"]
    country = request.form["country"]
    region = request.form["region"]

    wine = wine_repository.select(wine_id)
    producer = Producer(
        name,
        phone_number,
        email,
        country,
        region)
    producer_repository.save.(producer)
    return redirect("/producers")




# # create a route that handles a post request /wines which will create a new wine object and save it to the databas

# @wine_blueprint.route('/wines/<id>/delete', methods=['POST'])
# def delete_wine(id):
#     wine_repository.delete(id)
#     return redirect('/wines')

# @wine_blueprint.route('/wines/<id>/edit', methods=['POST'])
# def edit_wine(id):
#     wine =wine_repository.select(id)
#     producers = producer_repository.select_all()
#     return render_template('/wine/edit.html', wine=wine, producers=producers)