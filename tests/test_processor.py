import json
from task.processor import process_json

def test_process_json():
    input_json = '{"a": 10, "b": 20, "c": 30}'
    expected_output = json.dumps({
        "total": 60,
        "original_data": {"a": 10, "b": 20, "c": 30}
    })
    
    assert process_json(input_json) == expected_output