import glob
import boto3
import json

client = boto3.client('rekognition')
combined = []
for filename in glob.glob('../exercise-rekognition/public/photos/*.jpeg'):
    with open(filename, 'rb') as fd:
        response = client.detect_labels(Image={'Bytes': fd.read()})
        entry = {  "Filename": filename.replace("public/", "") }
        entry["Labels"] = response["Labels"]
        combined.append(entry)

print(json.dumps(combined, indent=2))
