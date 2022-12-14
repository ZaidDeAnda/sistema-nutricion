import pandas as pd
import pymongo
import urllib
import streamlit as st
from datetime import datetime

@st.cache(allow_output_mutation=True)
def get_mongo_client(config):
    """Get the mongo client and store it in cache.

        Params
        ------
        config : Config
            Configuration object containing email details.
        
        Returns
        -------
        client
            The mongo client connected to the database.
        """
    db_mongo = config.get_config()['db_mongo']
    user = db_mongo["user"]
    password = urllib.parse.quote_plus(db_mongo["password"])
    cluster = db_mongo["cluster"]
    client = pymongo.MongoClient(
        f"mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority"
    )
    return client

def create_dataframe_from_cursor(cursor):
    """Transform the cursor from mongo into a dataframe

        Params
        ------
        cursor : cursor
            Cursor pointing to a mongo collection.
        
        Returns
        -------
        df
            The dataframe made from the mongo cursor.
        """
    df = None
    for document in cursor:
        if df is not None:
            df = df.append(document, ignore_index=True)
        else:
            df = pd.DataFrame(document, index=[0])
    df.drop("_id", axis=1, inplace=True)
    return df

def change_date_format(date):
    return date[-2:] + date [-6:-2] + date[:-6]

def change_dict_format(dict):
    new_dict = {}
    for key in dict.keys():
        if dict[key]["nombre"] not in new_dict.keys():
            new_dict[dict[key]["nombre"]] = dict[key]
            new_dict[dict[key]["nombre"]].pop("nombre")
        else:
            old_date = datetime.strptime(new_dict[dict[key]["nombre"]]["fecha"], '%d-%m-%Y')
            new_date = datetime.strptime(dict[key]["fecha"], '%d-%m-%Y')
            if old_date < new_date:
                new_dict[dict[key]["nombre"]] = dict[key]
                new_dict[dict[key]["nombre"]].pop("nombre")
    return new_dict
