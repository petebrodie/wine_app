from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.wine import producer
from models.producer import wine
import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository

wine_blueprint = Blueprint("wine", __name__)

