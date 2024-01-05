
import zipfile
import io
import requests
import os

from elliot.run import run_experiment

ratings = []

# Uncomment this block to use ml1 dataset (and comment the other one)
for line in open("./data/movielens_1m/ratings_gender.dat"):
    ratings.append(line.replace(";", "\t"))

print("Printing ratings.tsv to data/movielens_1m/ ..")
os.makedirs("data/movielens_1m", exist_ok=True)

with open("data/movielens_1m/dataset_gender.tsv", "w") as f:
    f.writelines(ratings)

# Uncomment this block to use coco dataset (and comment the other one)
#for line in open("./data/coco/interactions_gender.dat"):
#    ml_1m_ratings.append(line.replace(";", "\t"))

#print("Printing ratings.tsv to data/coco/ ..")
#os.makedirs("data/coco", exist_ok=True)
#with open("data/coco/dataset_gender.tsv", "w") as f:
#    f.writelines(ml_1m_ratings)


print("Done! We are now starting the Elliot's experiment")
run_experiment("config_files/configuration.yml")

