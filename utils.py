# utility functions go here
import random
from uuid import uuid4

import constants
from models import Raffle, User


def generate_raffles(count):
    for i in xrange(count):
        colour = constants.COLORS[i % constants.COLORS_LEN]
        uniq = uuid4().hex
        uniq_p1, uniq_p2 = uniq[:4], uniq[4:8]
        yield (colour, uniq_p1, uniq_p2)


def seed_raffles_into_db(max_raffles=constants.MAX_RAFFLES):
    for raffle_colour, raffle_up1, raffle_up2 in generate_raffles(max_raffles):
        raffle = Raffle(
            colour=raffle_colour,
            up1=raffle_up1,
            up2=raffle_up2,
        )
        print "Adding", raffle
        db.session.add(raffle)

    db.session.commit()
    return True


def get_unused_raffles(raffle_count):
    return (
        Raffle.query.filter_by(
            user=None
        ).limit(
            constants.RAFFLE_PADDING + raffle_count
        )
    ).all()


def assign_raffles_to_user(raffle_count, user):
    from app import db
    raffles = get_unused_raffles(raffle_count)
    for raffle in random.sample(raffles, raffle_count):
        print "Assigning {0} to {1}".format(raffle, user)
        raffle.user = user

    db.session.commit()
    return True