import click
import scraper as sc

uri_path = 'https://towerofgod.fandom.com/wiki/'

def show_blogpost(parsed_page):
    blogpost = sc.get_blogpost(parsed_page)
    sc.print_blogpost(blogpost)


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
        if volume == 1:
            url = uri_path + 'Ch.' + ('0' + str(chapter) if chapter < 10 else str(chapter))
        else:
            url = uri_path + 'Vol.' + str(volume) + '_Ch.' + ('0' + str(chapter) if chapter < 10 else str(chapter))
        page = sc.get_page(url)
        parsed_page = sc.parse_page(page)
        show_blogpost(parsed_page)


if __name__ == '__main__':
    show_chapter_content()
