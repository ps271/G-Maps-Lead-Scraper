import pandas as pd
from utils.runtime_json_data import file


def create_excel(data):
    df = pd.DataFrame().from_dict(data, orient='index')

    # Name the index/link column
    df.index.name = "Source Link"

    # Rename the data columns
    df = df.rename(columns={
        "name" : "Name",
        "rating" : "Rating",
        "details_fetched" : "Fetch Status",
        "phone" : "Phone Number",
        "website" : "Website",
    })
    df = df[['Name','Phone Number', 'Website', 'Rating', 'Fetch Status']]
    df.to_excel(f"{file}.xlsx", index=True)
