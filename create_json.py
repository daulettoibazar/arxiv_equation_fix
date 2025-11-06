import json
import os
import tqdm

tex_folder = "./equations/tex_files"

tex_files = os.listdir(tex_folder)

final_data = []

for file in tqdm.tqdm(tex_files):
    data = {
        "tex_path": os.path.join("equations/tex_files", file),
        "image_path": os.path.join("equations/images", file.replace(".tex", ".jpeg"))    
    }
    final_data.append(data)
with open("equations_data.json", "w") as json_file:
    json.dump(final_data, json_file, indent=4)