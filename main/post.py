from flask.ext import wtf
import wtforms
import flask
import auth
import model
from main import app


class PostUpdateForm(wtf.Form):
  title = wtforms.StringField('Title', [wtforms.validators.required()])
  date = wtforms.StringField('Fecha', [wtforms.validators.optional()])
  body = wtforms.StringField('Body', [wtforms.validators.optional()])

@app.route('/post/create/', methods=['GET', 'POST'])
@auth.login_required
def post_create():
  form = PostUpdateForm()
  if form.validate_on_submit():
    post_db = model.Post(
        user_key=auth.current_user_key(),
        title=form.title.data,
        date=form.date.data,
        body=form.body.data,
      )
    post_db.put()
    return flask.redirect(flask.url_for('welcome'))
  return flask.render_template(
      'post_create.html',
      html_class='post-create',
      title='Create Post',
      form=form,
    )