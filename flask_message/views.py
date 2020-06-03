from flask import flash, redirect, render_template, url_for
from flask_message import db, app
from flask_message.models import Message
from flask_message.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index1.html', form=form, messages=messages)
