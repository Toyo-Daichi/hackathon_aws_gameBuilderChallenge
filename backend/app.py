#-*- coding: utf-8 -*-
"""
Created on 2024.01.13
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from flask import Flask, request, jsonify

class App:
    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run(port=5000, debug=True)

if __name__ == '__main__':
    app = App()
    app.run()
