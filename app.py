import os, gzip, bs4, selenium.webdriver as sel, keyboard, time, requests
def get_mod(mod):
    url = 'https://www.curseforge.com/minecraft/mc-mods/' + mod + '/download'
    r = sel.Chrome('/Users/mark/Downloads/chromedriver 4')
    keyboard.send('command+tab')
    r.get(url)
    time.sleep(7)
    url = r.page_source
    url = bs4.BeautifulSoup(url)
    url = 'https://curseforge.com' + str(url.find('a', class_='alink underline').get('href'))
    r.get('archive.org')
    r.quit()
    return url
print(get_mod('create'))