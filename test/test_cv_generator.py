import pytest
from cv_generator.cv_generator import read_template, parse_template, merge

def test_read_template_returns_stripped_string():
    actual = read_template("./assest/personal_summary.txt")
    expected = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    assert actual == expected

def test_parse_template():
    template_string = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    actual_stripped, actual_parts = parse_template(template_string)
    expected_stripped = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    expected_parts = ("Name", "major", "job_title", "company_name")
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge():
    template = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    values = ("john", "CS", "developer", "ABCIT")
    actual = merge(template, values)
    expected = "I'm john and I have Bachelor's degree in CS and Currently working as a developer  -  at ABCIT."
    assert actual == expected

def test_read_template_raises_exception_with_bad_path():
    path = "missing.txt"
    with pytest.raises(FileNotFoundError):
        read_template(path)

# Additional Test Cases

def test_parse_template_no_placeholders():
    template_string = "This is a string with no placeholders."
    actual_stripped, actual_parts = parse_template(template_string)
    expected_stripped = "This is a string with no placeholders."
    expected_parts = ()
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge_with_empty_values():
    template = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    values = ("", "", "", "")
    actual = merge(template, values)
    expected = "I'm  and I have Bachelor's degree in  and Currently working as a   -  at ."
    assert actual == expected

def test_merge_with_partial_values():
    template = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    values = ("john", "CS")
    with pytest.raises(IndexError):
        merge(template, values)

def test_parse_template_with_special_characters():
    template_string = "I'm {Name} and I have a degree in {major}! Currently working as a {job_title} @ {company_name}."
    actual_stripped, actual_parts = parse_template(template_string)
    expected_stripped = "I'm {} and I have a degree in {}! Currently working as a {} @ {}."
    expected_parts = ("Name", "major", "job_title", "company_name")
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts
