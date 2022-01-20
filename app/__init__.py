from flask import Flask, render_template, request, redirect, url_for, session
import secrets

fapp = Flask(__name__)
fapp.secret_key = 'secret_key_you'

from app import routes

