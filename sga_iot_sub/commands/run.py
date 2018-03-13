import click

from sga_iot_sub.cli import pass_context

@click.command()
@click.option('--broker', default='127.0.0.1')
@click.option('--port', default=1883)
@click.option('--topic', default='topic/sga-iot')
@click.option('--username', default='')
@click.option('--password', default='')
@pass_context
def command(ctx, broker, port, topic, username, password):
    """Run sga-iot-sub"""
    ctx.log('Broker on http://%s:%s' % (broker, port))
    ctx.log('Topic on %s' % (topic))

    from sga_iot_sub import App
    app = App(ctx, broker, port, topic, username, password)
    app.run()
