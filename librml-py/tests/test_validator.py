import pytest
from pathlib import Path
from librml.validator import LibRMLValidator

@pytest.fixture
def validator():
    return LibRMLValidator()

@pytest.fixture
def examples_dir():
    return Path(__file__).parent / "data"

def test_validate_xml_minimal(validator, examples_dir):
    xml_path = examples_dir / "minimal.xml"
    # version 0.4 in minimal.xml might fail if XSD expects 0.5.0, let's check
    # The XSD I saw had version="0.5.0" but libRML element has version attribute (string)
    # The XSD says: <xs:attribute type="xs:string" name="version" />
    valid, error = validator.validate_xml(xml_path)
    assert valid, f"Validation failed for minimal.xml: {error}"

def test_validate_xml_readonly(validator, examples_dir):
    xml_path = examples_dir / "readonly.xml"
    valid, error = validator.validate_xml(xml_path)
    assert valid, f"Validation failed for readonly.xml: {error}"

def test_validate_xml_invalid():
    v = LibRMLValidator()
    invalid_xml = "<libRML xmlns='http://librml.org/schema'><invalid/></libRML>"
    valid, error = v.validate_xml(invalid_xml)
    assert not valid
    assert error is not None

def test_validate_json_valid(validator):
    valid_json = {
        "id": "test-1",
        "actions": [
            {
                "type": "read",
                "permission": True,
                "restrictions": [
                    {"type": "age", "minage": 18}
                ]
            }
        ]
    }
    valid, error = validator.validate_json(valid_json)
    assert valid, error

def test_validate_json_invalid(validator):
    invalid_json = {
        "actions": [
            {
                "type": "nonexistent",
                "permission": "not-a-bool"
            }
        ]
    }
    valid, error = validator.validate_json(invalid_json)
    assert not valid
