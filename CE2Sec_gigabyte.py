banner = '''  
ce2团队-病毒木马检测脚本v1.0
'''
print(banner)
import os

def search_file(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


if __name__ == '__main__':
    a = "8ccbee6f7858ac6b92ce23594c9e2563ebcef59414b5ac13ebebde0c715971b2.bin"
    b = "system32\GigabyteUpdateService.exe"
    filename = a
    filename = b
    path = input("请输入你要搜索的路径: ")

    results = search_file(filename, path)

    if len(results) > 0:
        print(f"查找个数 {len(results)} 路径:")
        for r in results:
            print(r)
    else:
        print(f"没有找到 {filename}")