"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#
db.define_table(
    'game',
    ### TODO: define the fields that are in the json.
    Field('steam_appid'),
    Field('name'),
    Field('developer'),
    Field('owners'),
    Field('genre'),
)
db.define_table(
    'gamedata',
    ### TODO: define the fields that are in the json.
    Field('steam_appid'),
    Field('name'),
    Field('developers'),
    Field('metacritic'),
    Field('reccomendations'),

)
db.define_table(
    'appdata',
    ### TODO: define the fields that are in the json.
    Field('steam_appid'),
    Field('timestamp_created'),
    Field('timestamp_updated'),
    Field('voted_up'),
    Field('votes_up'),
    Field('votes_funny'),
    Field('weighted_vote_score'),
    Field('comment_count'),



    

)
db.define_table(
    'reviewdata',
    ### TODO: define the fields that are in the json.
    Field('steam_appid'),
    Field('review_score'),
    Field('review_score_desc'),
    Field('total_positive'),
    Field('total_negative'),
    Field('total_reviews'),


)
db.commit()
