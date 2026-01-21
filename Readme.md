# YallaKora Web Scraping & Match Analysis Automation 

This project is python-based web scraping and automation tool designed to extract football match data from **YallaKora**, process and analyze the data, and export it in multiple useable formats 

The goal of the project isto  demonstrate a complete data pipline :
    scraping --> cleaning --> analysis --> visualiztion --> cloud integration 

## Features 

- Scrapes football match data from Yallakora 
- Cleans and Structures the extracted data 
- Saves the result to CSV files 
- Generates analytical charts (using matplotlib) 
- uploads the final dataset to Google Sheets
- Centralized logging system for monitoring and debugging  
- Modular and reusable project structure 

## Technologies Used 

- python
- requests
- Beautifulsoup
- pandas 
- Google Sheets API (gspread)
- logging module  


## Google Sheet integration 

The project supports exporting the scraped data directly to **Google Sheet** using a Google Service Account.
This allows the data to be easy to shared, reviewed, or reused without manual file handling.

## Logging 

A centralized logging system is implemented to track:
    - Scraping progress 
    - Errors and exceptions 
    - Execution flow  

Logs are saved to :
    match.log 

This makes debugging and monitoring easier during longor repeated runs 

---

## Output 

- CSV file containing all scraped match data 
- Analytincal charts (png)
- pdf for chrats 
- Google Sheet containing the final dataset (https://docs.google.com/spreadsheets/d/17IH8ILWmOqWRBDKBNCJTQCQ9HEFx_oQGTkLla7qJ-Jw/edit?gid=0#gid=0)

## How to Run 

1.Install dependencies :
    pip install -r requirements.txt 

2.Configure Google Service Account credentials (if using Google Sheets)

3.Run the project:
    python project2.py


