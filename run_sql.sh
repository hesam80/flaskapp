#!/bin/bash
python app.py
sqlite3 database.db < schema.sql