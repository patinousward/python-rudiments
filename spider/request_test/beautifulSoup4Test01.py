from bs4 import BeautifulSoup


if __name__ == '__main__':
    # 第一个参数传入的应该是html的内容，所以需要读取文件成string
    soup = BeautifulSoup('<div>df</div>', 'html.parser')
    print(soup.find('div'))