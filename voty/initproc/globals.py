from datetime import date


class NOTIFICATIONS:
    """
    All internal notifications
    """
    class INVITE:
        SEND = "inivited"
        ACCEPTED = "invite_accepted"
        REJECTED = "invite_rejected"

    class INITIATIVE:
        EDITED = "init_edited"
        SUBMITTED = "init_submitted"
        PUBLISHED = "init_published"
        WENT_TO_DISCUSSION = "init_discussion"
        DISCUSSION_CLOSED = "init_discussion_closed"
        WENT_TO_VOTE = 'init_vote'
        COMPLETED = 'init_completed'
        ACCEPTED = 'init_accepted'
        REJECTED = 'init_rejected'
        NEW_ARGUMENT = 'init_new_arg'


class STATES:
    """
    The states an initiative can have
    """
    PREPARE = 'p'
    INCOMING = 'i'
    SEEKING_SUPPORT = 's'
    DISCUSSION = 'd'
    FINAL_EDIT = 'e'
    MODERATION = 'm'
    HIDDEN = 'h'
    VOTING = 'v'
    COMPLETED = 'c'
    ACCEPTED = 'a'
    REJECTED = 'r'


PUBLIC_STATES = [STATES.SEEKING_SUPPORT,
                 STATES.DISCUSSION,
                 STATES.FINAL_EDIT,
                 STATES.VOTING,
                 STATES.COMPLETED,
                 STATES.ACCEPTED,
                 STATES.REJECTED]

TEAM_ONLY_STATES = [STATES.INCOMING,
                    STATES.MODERATION,
                    STATES.HIDDEN]

class VOTY_TYPES:
    Einzelinitiative = 'initiative'
    PolicyChange = 'ao-aenderung'
    BallotVote = 'urabstimmung'
    PlenumVote = 'plenumsentscheidung'
    PlenumOptions = 'plenumsabwaegung'

class VOTED:
    """
    The possibilities for casting a vote
    """
    NO = 0
    YES = 1
    ABSTAIN = 2


COMPARING_FIELDS = [
    'title', 'subtitle',  "summary", "problem", "forderung", "kosten",
    "fin_vorschlag", "arbeitsweise", "init_argument",
    "einordnung", "ebene", "bereich",
]

SUBJECT_CATEGORIES = [
    'Globale Politik & internationale Zusammenarbeit',
    'Bildung, Forschung & Kultur',
    'Innenpolitik',
    'Netz- & Medienpolitik',
    'Geschlechtergerechtigkeit',
    'Vielfalt & Integration',
    'Demokratie & Transparenz',
    'Gesundheit, Ernährung & Verbraucher*innenschutz',
    'Umwelt, Mobilität, Infrastruktur & Strukturentwicklung',
    'Soziale Gerechtigkeit, Wirtschaft, Arbeit & Finanzen',
    'Anderes'
]

ABSTENTION_START = date(2017, 12, 1) # Everything published after this has abstentions
SPEED_PHASE_END = date(2017, 8, 21) # Everything published before this has speed phase
INITIATORS_COUNT = 3

MINIMUM_MODERATOR_VOTES = 5
MINIMUM_FEMALE_MODERATOR_VOTES = 3
MINIMUM_DIVERSE_MODERATOR_VOTES = 2

BOARD_GROUP = "Bundesvorstand"