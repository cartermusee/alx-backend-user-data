#!/usr/bin/env python3
"""module for sesssion auth routes"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    pasword = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pasword:
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(pasword):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)

    ses_name = os.getenv('SESSION_NAME', '_my_session_id')
    resp = jsonify(user.to_json())
    resp.set_cookie(ses_name, session_id)
    return resp


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
