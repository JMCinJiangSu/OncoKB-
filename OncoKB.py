# ! /usr/bin/python3
# -*- coding = utf-8 -*-

import pandas as pd
import numpy as np

# 读取txt内容
def readcontent(filename):
	cont = []
	with open(filename) as f:
		for line in f:
			line = line.strip()
			cont.append(line)
	return cont

colname = ['Gene', 'Alteration', 'Oncogenic', 'Mutation Effect', 'Citation']
Oncokb = pd.DataFrame(columns = colname)

genes = readcontent('Oncokb注释基因.txt')

for i in genes:
	try:
		alt = readcontent(i + '.txt')
		# 拆分时注意原始文件中是否存在不符合4列内容的行
		alt_new = [alt[i:i+4] for i in range(0, len(alt), 4)]
	except:
		pass
	else:
		df = pd.DataFrame(columns = colname)
		m = 0
		for j in range(len(alt_new)):
			print(alt_new[j])
			df.loc[m, 'Gene'] = i
			df.loc[m, 'Alteration'] = alt_new[j][0]
			df.loc[m, 'Oncogenic'] = alt_new[j][1]
			df.loc[m, 'Mutation Effect'] = alt_new[j][2]
			df.loc[m, 'Citation'] = alt_new[j][3]
			m += 1
		Oncokb = Oncokb.append(df)

writer = pd.ExcelWriter('Oncokbdatabase.xlsx', engine = 'openpyxl')
Oncokb.to_excel(writer, index = False)
writer.save()


