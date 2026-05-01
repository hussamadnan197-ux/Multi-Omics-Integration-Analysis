import requests
import json

def get_cancer_project_stats(project_id):
    """جلب إحصائيات عينات السرطان من قاعدة بيانات GDC"""
    url = f"https://api.gdc.cancer.gov/projects/{project_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()['data']
        print(f"Project ID: {data['project_id']}")
        print(f"Disease Type: {data['disease_type']}")
        print(f"Total Cases: {data['summary']['case_count']}")
        print(f"Total Files: {data['summary']['file_count']}")
    else:
        print("Error fetching data.")

if __name__ == "__main__":
    # سنبدأ بتجربة سرطان الدم بما أنك تعمل في مختبر باثولوجي
    get_cancer_project_stats("TCGA-LAML") 
