import json

def process_json(input_json):
    data = json.loads(input_json)
    total = sum(data.values())
    output_data = {
        "total": total,
        "original_data": data
    }
    return json.dumps(output_data)
