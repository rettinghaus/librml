import lxml.etree as ET
import json
import jsonschema
import sys

def verify():
    xml_file = 'examples/restrict.xml'
    xsl_file = 'schema/librml.xsl'
    schema_file = 'schema/librml.json'

    # 1. Transform
    dom = ET.parse(xml_file)
    xslt = ET.parse(xsl_file)
    transform = ET.XSLT(xslt)
    newdom = transform(dom)

    json_str = str(newdom)
    print("Generated JSON:")
    print(json_str)

    try:
        json_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    # 2. Validate
    with open(schema_file, 'r') as f:
        schema = json.load(f)

    try:
        jsonschema.validate(instance=json_data, schema=schema)
        print("Validation successful!")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation error: {e.message}")
        print(f"At: {e.json_path}")
        sys.exit(1)

if __name__ == "__main__":
    verify()
