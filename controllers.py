"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""
from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.form import Form, FormStyleBulma
from pydal.validators import IS_NOT_EMPTY

from py4web.utils.url_signer import URLSigner

from .common import Field


from py4web.utils.grid import Grid, GridClassStyleBulma


@unauthenticated("index", "index.html")
def index():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    return dict(message=message)

@unauthenticated("graph", "graph.html")
def rt():
    return dict()

@action('insert', method=["GET", "POST"])
@action.uses(db, session, 'insert.html')
def insert():
    form = Form(db.game,
                csrf_session=session, formstyle=FormStyleBulma)
    if form.accepted:
        redirect(URL('index'))
    return dict(form=form)

@action('delete', method=["GET", "POST"])
@action.uses(db, session, 'delete.html')
def delete():
    #db(db.game.steam_appid == app_id).delete()
    #redirect(URL('index'))
    form = Form(        [
        Field('steamApp_id', requires=IS_NOT_EMPTY()),
    ]
)

    if form.accepted:
        #if there are some rows that are equal to app_id, delete it, if not move on
        if db(db.game.steam_appid == form.vars['steamApp_id']).select().as_list() is not None:
            db(db.game.steam_appid == form.vars['steamApp_id']).delete()
        redirect(URL('index'))
    return dict(form=form)

@action('update', method=["GET", "POST"])
@action.uses(db, session, 'update.html')
def update():
    #db(db.game.steam_appid == app_id).delete()
    #redirect(URL('index'))
    rows=[]
    form = Form([
        Field('steamApp_id', requires=IS_NOT_EMPTY(), label='Steam App Id to Update'),
        Field('owners', requires=IS_NOT_EMPTY()),
    ]
)

    if form.accepted:
        #if there are some rows that are equal to app_id, delete it, if not move on
        if db(db.game.steam_appid == form.vars['steamApp_id']).select().as_list() is not None:
            (db(db.game.steam_appid == form.vars['steamApp_id'])._update(owners=form.vars['owners']))

    return dict(form=form, rows=rows)
@action('read', method=["GET", "POST"])
@action.uses(db, session, 'read.html')
def read():
    #db(db.game.steam_appid == app_id).delete()
    #redirect(URL('index'))
    rows=[]
    form = Form([
        Field('steamApp_id', requires=IS_NOT_EMPTY()),
    ]
)

    if form.accepted:
        #if there are some rows that are equal to app_id, delete it, if not move on
        if db(db.game.steam_appid == form.vars['steamApp_id']).select().as_list() is not None:
           rows = db(db.game.steam_appid == form.vars['steamApp_id']).select().as_list()
    return dict(form=form, rows=rows)
