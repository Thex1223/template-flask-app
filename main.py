from flask import Flask, render_template, redirect, url_for, jsonify
import json

env_data = None

with open("env.json", "r") as file:
    env_data = json.load(file)

# Cria o App
app = Flask(__name__)
app.secret_key = env_data['APP_SECRET_KEY']