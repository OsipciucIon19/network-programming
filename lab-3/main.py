from lxml import etree
import requests
import re


proxies = {
    'http': 'http://dcRezG:kjrDLs@193.7.199.142:8000',
    'https': 'http://dcRezG:kjrDLs@193.7.199.142:8000',
}


def get_page():
    url = 'https://www.reddit.com/'
    response = requests.get(url, proxies=proxies)
    print(response.text)
    print("Status code:", response.status_code)


def get_links_by_search():
    url = 'https://www.reddit.com/search/?q=test'
    response = requests.get(url, proxies=proxies)
    text = re.sub('\s+', ' ', response.text)
    print(text)
    search_results = re.findall("<span (.*?)>Posted by(.*?)href=\"(.*?)\"", text)
    print("\nLinks by search:")
    for link in search_results:
        print(f" - {link[2]}")


def login():
    with requests.Session() as session:
        url = "https://www.reddit.com/login"
        email = "iosipciuc"
        password = "osipciuctest1234"
        tree = etree.HTML(session.get(url).content)
        csrf = tree.xpath('//input[@name="csrf_token"]/@value')[0]
        session.get(url)
        form_data = dict(csrf_token=csrf, username=email, password=password)
        headers = {
            'referer': url,
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = session.post(url, data=form_data, headers=headers)
        print(response.content)
        print('Status code:', response.status_code)


def options():
    url = 'https://www.reddit.com/search/?q=test'
    resp = requests.options(url, proxies=proxies)
    print(resp.headers)


if __name__ == "__main__":
    print(
        "\n## List of commands: ##\n"
        + "1. Get Page\n2. Get Links By Search\n"
        + "3. Login\n4. Options"
    )
    command = input("Enter the option: ")

    while command != "exit":
        if command == "1":
            get_page()
        elif command == "2":
            get_links_by_search()
        elif command == "3":
            login()
        elif command == "4":
            options()
        else:
            print("There is no such command")

        print(
            "\n## List of commands: ##\n"
            + "1. Get Page\n2. Get Links By Search\n"
            + "3. Login\n4. Options"
        )
        command = input("Enter the next command: ")
