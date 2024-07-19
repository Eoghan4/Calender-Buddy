# This should allow a colleague's name and email to be added to and read from the database (csv)
import csv

def add_colleague(name, email):
    with open('db.csv', mode = 'a') as csvfile:
        fields = ["name", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writerow({"name" : name , "email" : email})
        csvfile.close

def read_colleagues():
    names = []
    emails = []
    with open('db.csv', mode = 'r') as csvfile:
        fields = ["name", "email"]
        reader = csv.DictReader(csvfile, fieldnames=fields)
        for row in reader:
            names.append(row["name"])
            emails.append(row["email"])
        return names, emails
