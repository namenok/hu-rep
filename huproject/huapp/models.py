from django.db import models

# Create your models here.


import pymongo

from django.conf import settings
my_client = pymongo.MongoClient('mongodb+srv://arinaznamenok:rnaoHQ949X22BtQx@cluster0.ltwuzun.mongodb.net/?appName=Cluster0')



dbname = my_client['newww_medicines']

coll_neew_name = dbname["medicinedetails"]


#let's create two documents
medicine_1 = {
    "medicine_id": "RR000123456",
    "common_name" : "Paracetamol",
    "scientific_name" : "",
    "available" : "Y",
    "category": "fever"
}
medicine_2 = {
    "medicine_id": "RR000342522",
    "common_name" : "Metformin",
    "scientific_name" : "",
    "available" : "Y",
    "category" : "type 2 diabetes"
}

medicine_3 = {
    "medicine_id": "kjsglsjgklsrjgn",
    "common_name" : "Metformin",
    "scientific_name" : "",
    "available" : "Y",
    "category" : "type 2 diabetes"
}
# Insert the documents
coll_neew_name.insert_many([medicine_1,medicine_2, medicine_3])


