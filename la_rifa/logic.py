import la_rifa.models as models


def check_for_bet(raffle, bet):
    return models.Chance.objects.filter(raffle=raffle, raffle__chance__selection=bet)


def assign_bet(raffle, bet):
    return models.Chance.objects.create(selection=bet, raffle=raffle)
