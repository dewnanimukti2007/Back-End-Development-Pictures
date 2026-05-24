import os
import sys
import logging
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_cors import CORS
from . import app

# Data source
data = [
    {
        "id": "1",
        "version": "1.0.0",
        "author": "Albert Einstein",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg"
    },
    {
        "id": "2",
        "version": "1.0.0",
        "author": "Isaac Newton",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/39/GodfreyKneller-IsaacNewton-1689.jpg"
    },
    {
        "id": "3",
        "version": "1.0.0",
        "author": "Marie Curie",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Marie_Curie_c1900.jpg"
    },
    {
        "id": "4",
        "version": "1.0.0",
        "author": "Nikola Tesla",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/Tesla_circa_1890.jpeg"
    },
    {
        "id": "5",
        "version": "1.0.0",
        "author": "Charles Darwin",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Charles_Darwin_seated_crop.jpg"
    },
    {
        "id": "6",
        "version": "1.0.0",
        "author": "Galileo Galilei",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Justus_Sustermans_-_Portrait_of_Galileo_Galilei%2C_1636.jpg"
    },
    {
        "id": "7",
        "version": "1.0.0",
        "author": "Ada Lovelace",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Ada_Lovelace_portrait.jpg"
    },
    {
        "id": "8",
        "version": "1.0.0",
        "author": "Alan Turing",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Alan_Turing_Aged_16.jpg"
    },
    {
        "id": "9",
        "version": "1.0.0",
        "author": "Thomas Edison",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Thomas_Edison2.jpg"
    },
    {
        "id": "10",
        "version": "1.0.0",
        "author": "Louis Pasteur",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Louis_Pasteur%2C_by_Albert_Edelfelt_b.jpg"
    }
]

######################################################################
# HEALTH & COUNT ENDPOINTS
######################################################################

@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200
    return {"message": "Internal server error"}, 500

######################################################################
# GET ALL PICTURES (Exercise 2)
######################################################################

@app.route("/picture", methods=["GET"])
def get_pictures():
    if not data:
        return jsonify({"message": "No pictures found"}), 404
    return jsonify(data)

######################################################################
# GET A PICTURE BY ID (Exercise 3 Placeholder)
######################################################################

@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    pass

######################################################################
# CREATE A PICTURE (Exercise 4 Placeholder)
######################################################################

@app.route("/picture", methods=["POST"])
def create_picture():
    pass

######################################################################
# UPDATE A PICTURE (Exercise 5 Placeholder)
######################################################################

@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    pass

######################################################################
# DELETE A PICTURE (Exercise 6 Placeholder)
######################################################################

@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    pass