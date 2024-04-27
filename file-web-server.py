#!/usr/bin/python3
from src import app
from os.path import abspath 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")