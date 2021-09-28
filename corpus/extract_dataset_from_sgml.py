from os import path
from bs4 import BeautifulSoup

current_directory = path.dirname(path.abspath(__file__))
input_filename = path.join(current_directory, "train.sgml")
generated_train_input_file = path.join(current_directory, "generated_train_input.txt")
generated_train_truth_file = path.join(current_directory, "generated_train_truth.txt")

with open(input_filename) as file:
    input_content = file.read()

soup = BeautifulSoup(input_content,'html.parser')
generated_train_input_content = []
generated_train_truth_content = []
index = 0

for child in soup.children:

	# 空节点直接跳过
	if child == "\n":
		continue

	# 提取文本(text)，错别字位置(locations_list)，和正确的字(corrections_list)
	text = child.contents[1].string
	print(f"index = {index}, text = {text}")
	locations_list = list(e.string for e in child.find_all('location'))
	corrections_list = list(e.string for e in child.find_all('correction'))
	
	# 生成唯一id
	id = "(generated-id=g"+str(index)+")"

	# 将来加入TrainingInputAll.txt，例：
	# (sighan15-id=3171)	虽然家长不能直接打扰老师在教书的时候，可是老师也会有一个默默被主义的压力。
	input_line = id+"\t"+text+"\n"
	generated_train_input_content.append(input_line)

	# 将来加入TrainingTruthAll.txt，例：
	# (sighan15-id=3171), 32, 注, 33, 意
	flattened_locations_corrections = list(item for tuple in list(zip(locations_list,corrections_list)) for item in tuple)
	truth_line = id+', '+', '.join(flattened_locations_corrections)+"\n"
	generated_train_truth_content.append(truth_line)

	index += 1

with open(generated_train_input_file,'w') as file:
    file.writelines(generated_train_input_content)

with open(generated_train_truth_file,'w') as file:
    file.writelines(generated_train_truth_content)

