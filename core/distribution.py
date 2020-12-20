import random


def distribute(people_wishes: dict) -> dict:
    if len(people_wishes) < 2:
        raise SecretSantaDistributionException("Must be at least 2 people to distribute")
    result_dict = {}
    gift_recipients = set()

    for santa in people_wishes.keys():
        available_people = set(people_wishes.keys()).difference(gift_recipients, {santa})
        if len(available_people) == 0:
            defined_santa = random.choice(list(result_dict.keys()))
            gift_recipient = result_dict[defined_santa][0]
            result_dict[santa] = (gift_recipient, people_wishes[gift_recipient])
            result_dict[defined_santa] = (santa, people_wishes[santa])
            continue
        gift_recipient = random.choice(list(available_people))

        result_dict[santa] = (gift_recipient, people_wishes[gift_recipient])
        gift_recipients.add(gift_recipient)
    return result_dict


class SecretSantaDistributionException(Exception):
    """Raised when illegal arguments are passed or illegal state is achieved"""
    pass
