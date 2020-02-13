import logging

from typing import Tuple

from jinja2 import Environment, FileSystemLoader
from jinja2.environment import Template

from settings import TEMPLATES_DIR, TEMPLATE_NAME, TODAY_DATETIME
from entities import FeedEntity
from feeds import FEEDS


def _get_html_template() -> Template:
    env_template = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=True
    )

    return env_template.get_template(TEMPLATE_NAME)


def render_html_email(feeds: Tuple[FeedEntity]) -> str:
    template = _get_html_template()

    short_email_date = TODAY_DATETIME.strftime('%d %b %Y')
    full_email_date = TODAY_DATETIME.strftime('%d %B %Y, %a')

    email = template.render(
        email_title=short_email_date,
        email_date=full_email_date,
        feeds=FEEDS
    )

    logging.info('Email feed was prepared.')

    return email
