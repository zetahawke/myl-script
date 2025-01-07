from request_structure import structure
from api_connector import get_edition_cards, get_profiles_from_cards


def capture_info(response, first, last):
    races = response['races']
    rarities = response['rarities']
    card_types = response['types']
    current_edition_details = response['edition']
    cards = response['cards']

    return get_profiles_from_cards(cards)



def extract_edition(edition):
    edition_name = edition['name']
    first_card, last_card = edition['amount'].split(',')
    response = get_edition_cards(edition_name)

    if response['status'] == 'OK' and response['code'] == 200:
        capture_info(response, first_card, last_card)

def iterate_editions(editions):    
    for edition in editions:
        extract_edition(edition)

def main():
    iterate_editions(structure())

if __name__ == '__main__':
    main()