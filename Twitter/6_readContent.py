import json
import re

# Specify the path to the JSON file
file_path = '/home/fish/Documents/Changes/data/search_results/1733173034881316932.json'

# Read the JSON file
with open(file_path, 'r') as file:
    json_data = json.load(file)[0]

def get_keys_architecture(data, prefix=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_prefix = f"{prefix}.{key}" if prefix else key
            get_keys_architecture(value, new_prefix)
    else:
        print(prefix)

# Usage
def get_ID_CONTENT(json_data):
    get_keys_architecture(json_data)
    result = json_data['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
    # Remove links from the result
    result_without_links = re.sub(r'http\S+', '', result)
    rest_id = json_data['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['rest_id']
return rest_id,result_without_links