from bs4 import BeautifulSoup as bs

def parse_page(page):
    parsed = bs(page.content, "html.parser")
    return parsed

class Element:
    def __init__(self, parsed_page, element_header, element_id):
        self.header = element_header
        element = parsed_page.find(id=element_id)
        element = element.parent.next_sibling
        self.element = element.find_next()

    def show(self):
        print(self.header + '\n')
        print(self.element.text.strip() + '\n')
