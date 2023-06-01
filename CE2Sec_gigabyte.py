banner = '''  
ce2团队-病毒木马检测脚本v1.0


免责声明
「由于传播、利用本工具及ce2团队所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，本团队及作者不为此承担任何责任，一旦造成后果请自行承担！」

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
    a = 'GigabyteUpdateService.exe'
    b = "8ccbee6f7858ac6b92ce23594c9e2563ebcef59414b5ac13ebebde0c715971b2.bin"
    filename = a or b
    path = input("请输入你要搜索的路径: ")

    results = search_file(filename,path)

    if len(results) > 0:
        print(f"查找个数 {len(results)} 路径:")
        for r in results:
            print(r)
            print("输出结果仅供参考")
    else:
        print(f"没有找到 {filename}")
        print("输出结果仅供参考")
