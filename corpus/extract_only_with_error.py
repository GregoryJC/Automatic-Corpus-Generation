from os import path

current_directory = path.dirname(path.abspath(__file__))

# 输入文件
generated_train_input_file = path.join(current_directory, "generated_train_input.txt")
generated_train_truth_file = path.join(current_directory, "generated_train_truth.txt")

# 输入文件内容
with open(generated_train_input_file) as file:
    generated_train_input_content = file.readlines()
with open(generated_train_truth_file) as file:
    generated_train_truth_content = file.readlines()

# 输出文件
TestTruth_file = path.join(current_directory, "TestTruth.txt")
TestInputWithError_file = path.join(current_directory, "TestInputWithError.txt")
TestTruthWithError_file = path.join(current_directory, "TestTruthWithError.txt")


# 输出文件内容
TestTruth_content = []
TestInputWithError_content = []
TestTruthWithError_content = []

# 没有错别字的gid名单
no_error_gid_list = []

with open(TestTruth_file) as file:
	TestTruth_content = file.readlines()

for line in TestTruth_content:
	if line.endswith("0\n"):
		gid = line.split(", ")[0]
		no_error_gid_list.append(gid)

no_error_gid_set = set(no_error_gid_list)


'''
改变generated_train_truth.txt格式

有错别字的：
before:	(generated-id=g0), 14, 基, 29, 在, 34, 后
after:	g0, 14, 基, 29, 在, 34, 后

before:	(generated-id=g1), 24, 的, 25, 精
after:	g1, 24, 的, 25, 精

没有错别字的：
before:	(generated-id=g839), 
after:	g839, 0
'''
# for line in generated_train_truth_content:
# 	line = line.strip()
# 	gid,_,error_info = line.partition("(generated-id=")[2].partition("), ")
# 	# print(f"gid = {gid}, error_info = {error_info}")

# 	# 有错别字的，加入到TestTruthWithError和TestTruth
# 	if len(error_info) > 0:
# 		new_line = gid + ", " + error_info + "\n"
# 		TestTruth_content.append(new_line)
# 		TestTruthWithError_content.append(new_line)

# 	# 没错别字的，gid后面的错误信息为“0”，只加入到TestTruth
# 	else:
# 		TestTruth_content.append(gid + ", 0\n")
# 		no_error_gid_list.append(gid)


# # 写文件
# # 有错别字的错别字信息
# with open(TestTruthWithError_file,'w') as file:
# 	file.writelines(TestTruthWithError_content)

# # 完整输入
# with open(TestTruth_file,'w') as file:
# 	file.writelines(TestTruth_content)	


# 把TestInput中没有错别字的行删掉，然后保存为TestInputWithError
# line: (generated-id=g12)	阿加迪助理说，它们的部队己由坎达哈与史宾波达克之...
for line in generated_train_input_content:
	gid = line.partition("(generated-id=")[2].partition(")	")[0]
	if gid in no_error_gid_set:
		continue
	else:
		TestInputWithError_content.append(line)

# 有错别字的输入
with open(TestInputWithError_file,'w') as file:
	file.writelines(TestInputWithError_content)		


