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
        else:
            url = 'http://www.cxdq.com/index_%d.htm' % i
    pics_url = get_url(url)

    sub_thread = []
    for i in range(len(pics_url)):
        t = threading.Thread(target=save_file, args=(pics_url[i],))
        t.start()
        sub_thread.append(t)
        for t in sub_thread:
            t.join()


def get_url(url):
    res = requests.get(url)
    # print(res.text)
    html = res.text
    img_url = re.findall(r'http.*?jpg', html)
    return img_url


def save_file(url):
    file_name = url.split('/')[-1]

    with open(file_name, 'wb') as f:
        img = requests.get(url, headers={'referer': 'http://m.cxdq.com'})
        f.write(img.content)
        print(file_name, '------下载完成------')


if __name__ == '__main__':
    if os.path.exists('picsfromweb'):
        os.chdir('picsfromweb')
    else:
        os.mkdir('picsfromweb')
    main()
