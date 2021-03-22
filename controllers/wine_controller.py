from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.wine import producer
from models.producer import wine




wine_blueprint = Blueprint("wine", __name__)

