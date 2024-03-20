from collections import OrderedDict
from more_itertools import bucket, unique_everseen

class Df_Container:
    def __init__(self, city_name, county_name, agency_name, doc_file_name, doc_path, link, df, server_gdf):
        self.city_name = city_name
        self.county_name = county_name
        self.agency_name = agency_name
        self.doc_file_name = doc_file_name
        self.doc_path = doc_path
        self.link = link
        self.df = df
        self.server_gdf = server_gdf
    
    def shapefile_output_dir(self):
        return self.doc_path / "misc"
    
    @classmethod
    def generate_data_for_markdown(cls, df_containers):
        data_for_markdown = []
        s = bucket(df_containers, key=lambda x: x.city_name)
        s_list = list(s)
        for i, key in enumerate( s_list ):
            # print(key)
            df_containers_by_city= list( s[key] )

            orderedDict = OrderedDict({
                "": i + 1,
                "city": key,
                "documents": len(df_containers_by_city),
                "tables": 0,
                "apns": 0,
                "parcels": 0,
                "agency": "",
                "county": "",
                "link": "",
            })

            for df_container in df_containers_by_city:
                local_df = df_container.df
                server_df = df_container.server_gdf

                # print(df_container['doc_file_name'])
                # print(server_df)
                if "table_order" in server_df.columns:
                    orderedDict["tables"] += server_df["table_order"].nunique()
                orderedDict["apns"] += cls.count_apns(local_df)
                orderedDict["parcels"] += len(server_df)
                orderedDict["agency"] = df_container.agency_name
                orderedDict["county"] = df_container.county_name
                orderedDict["link"] = df_container.link
                
                # print(df_container['county_name'])
            data_for_markdown.append(orderedDict)

        return data_for_markdown
    
    @classmethod
    def count_apns(cls, df):
        count_of_apns = df['table_rows'].apply(lambda x: len(x)).sum()
        return count_of_apns