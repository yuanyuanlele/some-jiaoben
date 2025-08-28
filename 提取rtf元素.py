import re
import pandas as pd
import os


def extract_data_from_rtf(rtf_file_path):
    """
    从 RTF 文件中提取数据，严格按照原文件内容，不修改任何数据
    """
    # 检查文件是否存在
    if not os.path.exists(rtf_file_path):
        print(f"错误: 文件 '{rtf_file_path}' 不存在")
        return []

    # 读取 RTF 文件内容
    try:
        with open(rtf_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        # 如果 UTF-8 解码失败，尝试使用其他编码
        try:
            with open(rtf_file_path, 'r', encoding='gbk') as file:
                content = file.read()
        except Exception as e:
            print(f"读取文件时出错: {e}")
            return []
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return []

    # 使用正则表达式查找所有匹配的记录
    # 修改模式以处理自闭合标签和空内容标签
    pattern = r'<subdoc_title>(.*?)</subdoc_title>\s*<class>(.*?)</class>\s*<cur_time>(.*?)</cur_time>\s*<operator>(.*?)</operator>\s*(?:<signer>(.*?)</signer>|<signer/>)?'

    matches = re.findall(pattern, content, re.DOTALL)

    # 将匹配结果转换为字典列表
    records = []
    for match in matches:
        # 只处理subdoc_title为"首次病程记录"的记录
        if match[0] == "首次病程记录":
            # 处理signer字段 - 如果有第5个匹配组且不为空
            signer_value = ""
            if len(match) > 4:
                signer_value = match[4] if match[4] else ""

            record = {
                'subdoc_title': match[0],
                'class': match[1] if match[1] else "",
                'cur_time': match[2] if match[2] else "",
                'operator': match[3] if match[3] else "",
                'signer': signer_value
            }
            records.append(record)

    return records


def save_to_excel(records, excel_file_path):
    """
    将记录保存到 Excel 文件
    """
    if not records:
        print("没有数据可保存")
        return False

    try:
        # 创建 DataFrame
        df = pd.DataFrame(records)

        # 保存到 Excel
        df.to_excel(excel_file_path, index=False)
        print(f"数据已保存到 {excel_file_path}")
        return True
    except Exception as e:
        print(f"保存Excel文件时出错: {e}")
        return False


def main():
    # 固定文件路径 - 请根据需要修改这些路径
    rtf_file_path = "D:/临时保存/SMSboom-HXCZ-main/SMSboom-HXCZ-main/病程记录log.rtf"  # 请修改为您的RTF文件路径
    excel_file_path = "D:/临时保存/SMSboom-HXCZ-main/SMSboom-HXCZ-main/第一次病程记录文件首次病程记录提取.xlsx"  # 请修改为您想保存的Excel文件路径

    # 提取数据
    print(f"正在从 RTF 文件中提取数据: {rtf_file_path}")
    records = extract_data_from_rtf(rtf_file_path)

    if not records:
        print("未找到符合条件的记录")
        return

    print(f"找到 {len(records)} 条符合条件的记录")

    # 显示前几条记录作为预览
    print("\n前几条记录预览:")
    for i, record in enumerate(records[:3]):  # 显示前3条记录
        print(f"记录 {i + 1}: {record}")

    if len(records) > 3:
        print("... (还有更多记录)")

    # 保存到 Excel
    success = save_to_excel(records, excel_file_path)

    if success:
        print("\n处理完成!")
    else:
        print("\n处理过程中出现错误!")


if __name__ == "__main__":
    main()


