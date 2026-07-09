import requests
import pandas as pd

def fetch_sample_data(project_id):
    # رابط البحث عن العينات في قاعدة بيانات GDC
    url = "https://api.gdc.cancer.gov/cases"
    
    # تحديد الفلاتر (نريد فقط عينات هذا المشروع المحدد)
    filters = {
        "op": "in",
        "content": {
            "field": "project.project_id",
            "value": [project_id]
        }
    }
    
    params = {
        "filters": json.dumps(filters) if 'json' in globals() else str(filters).replace("'", '"'),
        "fields": "case_id,primary_site,disease_type,submitter_id",
        "format": "JSON",
        "size": "10"
    }
    
    import json # للتأكد من التحويل
    params["filters"] = json.dumps(filters)

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json()["data"]["hits"]
        df = pd.DataFrame(results)
        print("Successfully fetched sample metadata:")
        print(df.head())
        return df
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    fetch_sample_data("TCGA-LAML")
