"""
Title: Database Updater
Author: Ethan Dinh
Date: 10/25/2023
"""

# Importing Libraries
from SQLconnect import update_table, update_locations
from UOScraper import scrapeData
import os

def main():
    update_locations()
    # scrapeData()
    # update_table()
    # os.remove(CourseData.csv")

if __name__ == "__main__":
    main()