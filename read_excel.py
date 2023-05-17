import pandas as pd
import json

# 파일명
file_name = '명언.xlsx'
file_path = "./sample.json"

# Daraframe형식으로 엑셀 파일 읽기
df = pd.read_excel(file_name, sheet_name="sheet1")

# 데이터 프레임 출력
# print(df)

data = {}
data['quotes'] = []
for idx in range(len(df)): 
    data['quotes'].append({
        "content" : (df["내용"][idx])
    })

with open(file_path, 'w', encoding="UTF-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)