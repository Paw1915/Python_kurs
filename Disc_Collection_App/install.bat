@echo off
title Instalator
python get-pip.py
pip install -r requirements.txt
flask run