import pymongo
import pandas
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = 'sensor'

if __name__ == '__main__':
    df = pandas.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns : {df.shape}")

    # convert Dataframe into JSON format
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[3])


    # insert converted json to Mongo Db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
