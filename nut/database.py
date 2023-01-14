import json

artworks_file = 'data_files/artworks.json'

def create_artwork_table():
    with open(artworks_file, 'w') as file:
        json.dump([], file)


def add_artwork(name,author):
    artworks = get_all_artworks()
    artworks.append({'name': name, 'author': author, 'finished': False})
    _save_all_artworks(artworks)


def get_all_artworks():
    with open(artworks_file, 'r') as file:
       return json.load(file)


def _save_all_artworks(artworks):
    with open(artworks_file,'w') as file:
            json.dump(artworks, file)


def mark_artwork_as_finished(name):
    artworks = get_all_artworks()
    for artwork in artworks:
        if artwork['name'] == name:
            artwork['finished'] = True
    _save_all_artworks(artworks)


def delete_artwork(name):
    artworks = get_all_artworks()
    artworks = [artwork for artwork in artworks if artwork['name'] != name]
    _save_all_artworks(artworks)