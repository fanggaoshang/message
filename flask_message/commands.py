import click
from flask_message import db, app
from flask_message.models import Message


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    from faker import Faker
    # db.drop_all()
    db.create_all()
    fake = Faker("zh-cn")
    click.echo("Working...")
    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo("Create %d fake message." % count)
