from ankaboot import get_site, make_soup, get_tag

url = "https://divar.ir/s/rasht/bike-skate-scooter"

d = get_site(url)
s = make_soup(d)
tags = get_tag(s, 'div', 'kt-post-card__top-description kt-post-card-description')

for tag in tags:
    print(tag)
