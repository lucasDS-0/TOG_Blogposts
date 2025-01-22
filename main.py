import click
import scraper as sc
import requests

def get_page(url_path):
    return requests.get(url_path)

def show_elements(parsed_page):
    endnote = sc.Element(parsed_page, "Naver Endnote", "Naver_Endnote")
    blogpost = sc.Element(parsed_page, "SIU's Blogpost", "Blog_Post")
    endnote.show()
    blogpost.show()

@click.command()
@click.option('--volume', type=int, required=True, help="Sets the chapter's volume")
@click.option('--chapter', type=int, required=True, help="Sets the chapter to show")
def show_chapter_content(volume, chapter):
    """Simple program to read SIU's Naver endnotes and blogposts."""
    if volume not in [1,2,3]:
        print(f'Volume {volume} doesn\'t exists :(.')
    elif chapter < 0:
        print(f'Chapter {chapter} doesn\'t exists :(.')
    elif (volume == 1 and chapter > 79) or (volume == 2 and chapter > 337):
        print(f'Volume {volume} doesn\'t have chapter {chapter} :(.')
    else:
        uri_path = 'https://towerofgod.fandom.com/wiki/'
        shift = '0' if chapter < 10 else ''
        if volume == 1:
            url = f'{uri_path}Ch.{shift}{chapter}'
        else:
            url = f'{uri_path}Vol.{volume}_Ch.{shift}{chapter}'
        page = get_page(url)
        parsed_page = sc.parse_page(page)
        show_elements(parsed_page)

if __name__ == '__main__':
    show_chapter_content()
