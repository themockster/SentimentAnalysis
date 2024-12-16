import urllib.request
import csv

def fetch_label_mapping(task):
    """
    Fetch label mapping for a given task from the Cardiff NLP GitHub repository.
    This helps return a text label to associated to the analysis being done. 
    
    """
    mapping_url = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    labels = []
    try:
        with urllib.request.urlopen(mapping_url) as response:
            data = response.read().decode("utf-8").split("\n")
            csv_reader = csv.reader(data, delimiter="\t")
            labels = [row[1] for row in csv_reader if len(row) > 1]
    except Exception as e:
        print(f"Error fetching label mapping: {e}")
    return labels
