import click
import scraper as sc


def show_blogpost(parsed_page):
    blogpost = sc.get_blogpost(parsed_page)
    sc.print_blogpost(blogpost)


@click.command()
@click.option('--volume', type=int, required=True, help="Sets the chapter's volume")
@click.option('--chapter', type=int, required=True, help="Sets the chapter to show")
def show_chapter(volume, chapter):
    if (chapter < 0) or (volume == 1 and chapter > 79) or \
            (volume == 2 and chapter > 337) or (volume == 3 and (chapter < 1 or chapter > 101)):
        print("Chapter doesn't exist :(")
    else:
        if volume == 1:
            url = 'https://towerofgod.fandom.com/wiki/Ch.' + ('0' + str(chapter) if chapter < 10 else str(chapter))
        else:
            url = 'https://towerofgod.fandom.com/wiki/Vol.' + str(volume) + '_Ch.' + ('0' + str(chapter) if chapter < 10 else str(chapter))
        page = sc.get_page(url)
        parsed_page = sc.parse_page(page)
        show_blogpost(parsed_page)


if __name__ == '__main__':
    show_chapter()
