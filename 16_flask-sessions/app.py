from flask import Flask, request, render_template, redirect, url_for, flash, session
import os


app = Flask(__name__)

secret_key = os.urandom(32)
app.secret_key = secret_key

