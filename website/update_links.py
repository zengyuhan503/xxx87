import re

file_path = r'd:\PROJECT-ZENGYUHAN\老郭的项目\XXX87\website\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def add_target(match):
    tag = match.group(0)
    if 'target=' in tag:
        return tag
    return tag.replace('<a', '<a target="_blank"', 1)

# Regex to match <a ... > (including multiline attributes)
# We use a non-greedy match for attributes
new_content = re.sub(r'<a\s+[^>]*>', add_target, content, flags=re.IGNORECASE | re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
