import os
import json
import re
from tqdm import tqdm

def remove_comments(content):
    """Remove LaTeX comments (% until newline) but preserve escaped percent signs (\%)"""
    # Remove comments
    pattern = r'(?<!\\)%.*?(?=\n|$)'
    cleaned_content = re.sub(pattern, '', content)
    
    # Remove \label{*} patterns
    label_pattern = r'\\label\{[^}]*\}'
    cleaned_content = re.sub(label_pattern, '', cleaned_content)
    
    return cleaned_content

tex_path = "./equations/tex_files"
tex_files = os.listdir(tex_path)
print(f"Total .tex files found: {len(tex_files)}")

processed_files = []

for file in tqdm(tex_files):
    tex_file = os.path.join(tex_path, file)
    with open(tex_file, "r") as f:
        content = f.read()
    
    # Remove comments
    cleaned_content = remove_comments(content)
    cleaned_content = cleaned_content.replace("\n", "").replace("\t", "")
    # Write back to file
    with open(tex_file, "w") as f:
        f.write(cleaned_content)
    
    processed_files.append(file)

print(f"Processed {len(processed_files)} files and removed comments")
    