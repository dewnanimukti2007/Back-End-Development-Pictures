import os
import sys
import logging
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_cors import CORS
from . import app

# Data source
data = [
    {"id": 1, "version": "1.0.0", "author": "Albert Einstein",
     "url": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg"},
    {"id": 2, "version": "1.0.0", "author": "Isaac Newton",
     "url": "https://upload.wikimedia.org/wikipedia/commons/3/39/GodfreyKneller-IsaacNewton-1689.jpg",
     "event_country": "United States",
     "event_state": "California",
     "event_city": "Fremont",
     "event_date": "11/2/2030"},
    {"id": 3, "version": "1.0.0", "author": "Marie Curie",
     "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Marie_Curie_c1900.jpg"},
    {"id": 4, "version": "1.0.0", "author": "Nikola Tesla",
     "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/Tesla_circa_1890.jpeg"},
    {"id": 5, "version": "1.0.0", "author": "Charles Darwin",
     "url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Charles_Darwin_seated_crop.jpg"},
    {"id": 6, "version": "1.0.0", "author": "Galileo Galilei",
     "url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Justus_Sustermans_-_Portrait_of_Galileo_Galilei%2C_1636.jpg"},
    {"id": 7, "version": "1.0.0", "author": "Ada Lovelace",
     "url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Ada_Lovelace_portrait.jpg"},
    {"id": 8, "version": "1.0.0", "author": "Alan Turing",
     "url": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Alan_Turing_Aged_16.jpg"},
    {"id": 9, "version": "1.0.0", "author": "Thomas Edison",
     "url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Thomas_Edison2.jpg"},
    {"id": 10, "version": "1.0.0", "author": "Louis Pasteur",
     "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Louis_Pasteur%2C_by_Albert_Edelfelt_b.jpg"}
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
# GET A PICTURE BY ID
######################################################################
@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture = next((item for item in data if item["id"] == id), None)
    if not picture:
        return jsonify({"message": "picture not found"}), 404
    return jsonify(picture), 200

######################################################################
# CREATE A PICTURE (Exercise 4 Placeholder)
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    # Extract picture data from the request body
    new_picture = request.get_json()
    
    if not new_picture:
        return jsonify({"message": "Invalid data"}), 400

    # Check if a picture with the same ID already exists
    picture = next((item for item in data if item["id"] == new_picture["id"]), None)
    
    # Lab specific requirement: return "Message" and 302 status code
    if picture:
        return jsonify({"Message": f"picture with id {new_picture['id']} already present"}), 302

    # Append the new picture data to our list
    data.append(new_picture)
    return jsonify(new_picture), 201

######################################################################
# UPDATE A PICTURE (Exercise 5)
######################################################################
@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture_by_id(id):
    picture = next((item for item in data if item["id"] == id), None)

    if not picture:
        return jsonify({"message": "picture not found"}), 404

    updated_data = request.get_json()
    if not updated_data:
        return jsonify({"message": "Invalid data"}), 400

    for key, value in updated_data.items():
        picture[key] = value

    return jsonify(picture), 200

######################################################################
# DELETE A PICTURE (Exercise 6)
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    picture = next((item for item in data if item["id"] == id), None)

    if not picture:
        return jsonify({"message": "picture not found"}), 404

    data.remove(picture)

    return "", 204