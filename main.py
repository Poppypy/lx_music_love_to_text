import json


def extract_name_and_singer(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # 解析 JSON 数据
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"JSON 解析错误: {e}")
            return

        # 提取 name 和 singer
        if 'data' in data and 'list' in data['data']:
            for item in data['data']['list']:
                name = item.get('name')
                singer = item.get('singer')
                if name and singer:
                    print(f"{name} - {singer}")
        else:
            print("数据结构不符合预期")


# 调用函数，传入文件路径
extract_name_and_singer('歌单.txt')
