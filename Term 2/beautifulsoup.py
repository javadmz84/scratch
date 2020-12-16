from ankaboot import get_site, make_soup, get_tag

url = "https://bama.ir/car/peykan/all-models/all-trims?page=1"

d = get_site(url)
s = make_soup(d)
tags = get_tag(s, 'h2', 'persianOrder')

for tag in tags:
    print(tag)
