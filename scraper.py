from bs4 import BeautifulSoup


def parse_page(page):
    parsed = BeautifulSoup(page.content, "html.parser")
    return parsed

def get_naver_endnote(parsed_page):
    header = parsed_page.find(id="Naver_Endnote")
    header = header.parent.next_sibling
    return header.find_next()

def get_blogpost(parsed_page):
    header = parsed_page.find(id="Blog_Post")
    header = header.parent.next_sibling
    return header.find_next()

def print_endnote(endnote):
    print("Naver Endnote:\n")
    print(endnote.text.strip() + '\n')

def print_blogpost(blogpost):
    print("SIU's Blogpost:\n")
    print(blogpost.text.strip() + '\n')
