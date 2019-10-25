import re
import requests
import os
import threading


def main():
    page_start = int(input('输入起始页码: '))
    page_end = int(input('输入结束页码: '))
    print('------开始下载------')

    for i in range(page_start, page_end):
        if i == 1:
            url = 'http://www.cxdq.com/'
            continue
        else:
            url = 'http://www.cxdq.com/index_%d.htm' % i
    pics_url = get_url(url)


    for i in pics_url:
        t = threading.Thread(target=save_file, args=(i,))
        t.start()


def get_url(url):
    res = requests.get(url)
    # print(res.text)
    html = res.text
    img_url = re.findall(r'http.*?jpg', html)
    return img_url


os.chdir('picsfromweb')


def save_file(url):
    file_name = url.split('/')[-1]

    with open(file_name, 'wb') as f:
        img = requests.get(url, headers={'referer': 'http://m.cxdq.com'})
        f.write(img.content)
        print(file_name, '------下载完成------')


if __name__ == '__main__':
    main()
