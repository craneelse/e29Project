import re
import sys
import os

input_file_name="{{ cookiecutter.input_data_file}}"
input_data_txt=''
if(os.path.exists(input_file_name)) :
    with open(input_file_name) as f:
        for line in f:
            for words in line.split(","):
                input_data_txt=input_data_txt+"|"+words.strip()
                input_data_txt=input_data_txt+"|"
            input_data_txt=input_data_txt+"\n"

file_name = os.path.join("features", "{{cookiecutter.feature_file}}.feature")

with open(file_name) as t:
    feature_file_readline=t.read()
    replaced_feature_file=feature_file_readline.replace("<input_data_txt>",input_data_txt)

with open(file_name, 'w') as f:
    f.write(replaced_feature_file)

