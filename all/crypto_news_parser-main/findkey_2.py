from main import get_titles
from keys import keys




def find_string_with_key(keys):
    titles = get_titles()
    for title in titles:
        title = title.split()
        for i in keys:
            if i in title:
                print(*title)



find_string_with_key(keys)