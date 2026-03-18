import os
import re

def sort_attributes(tag_match):
    tag_name = tag_match.group(1)
    attrs_str = tag_match.group(2)
    trailing = tag_match.group(3) # / or ? or empty

    # Regex to find attributes: key="value" or key='value'
    attr_pattern = re.compile(r'([a-zA-Z0-9:-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')')

    attrs = []
    for m in attr_pattern.finditer(attrs_str):
        name = m.group(1)
        value = m.group(2) if m.group(2) is not None else m.group(3)
        quote = '"' if m.group(2) is not None else "'"
        attrs.append((name, value, quote))

    if not attrs:
        return f'<{tag_name}{attrs_str}{trailing}>'

    # Sort attributes by name
    attrs.sort(key=lambda x: x[0])

    sorted_attrs_str = ""
    for name, value, quote in attrs:
        sorted_attrs_str += f' {name}={quote}{value}{quote}'

    return f'<{tag_name}{sorted_attrs_str}{trailing}>'

def process_xml_block(xml_block):
    # Tag regex for <item ...> or <libRML:item ...>
    # We only want to target 'item' elements as requested.
    # Group 1: tag name (must contain 'item')
    # Group 2: attributes string
    # Group 3: trailing / or ?
    tag_pattern = re.compile(r'<([a-zA-Z0-9:]*item)([^>]*?)([/?]?)>')

    def replace_tag(match):
        full_tag = match.group(0)
        # Skip closing tags
        if full_tag.startswith('</'):
            return full_tag
        return sort_attributes(match)

    return tag_pattern.sub(replace_tag, xml_block)

def main():
    md_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    for filepath in md_files:
        if '/.git/' in filepath:
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # XML block regex: ```xml ... ```
        xml_block_pattern = re.compile(r'(```xml\s*\n)(.*?)(\n```)', re.DOTALL)

        new_content = xml_block_pattern.sub(lambda m: m.group(1) + process_xml_block(m.group(2)) + m.group(3), content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Processed {filepath}")

if __name__ == "__main__":
    main()
