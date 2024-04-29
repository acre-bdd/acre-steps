# -*- coding: utf-8 -*-
from radish import given, then, when, step
from radish import world

from acre.lib import log, retry

from acre.playwright import Browser


@given("I start the browser")
def i_start_the_browser(step):
    Browser.start()


@step("I close the browser")
def i_close_the_browser(step):
    Browser.stop()


@when('I navigate to "{url}"')
def i_navigate_to(step, url):
    if not world.page:
        world.page = world.context.new_page()
    log.note(f"opening url '{url}'")
    world.page.goto(url)


@then('the page title contains {text:QuotedString}')
def page_title_contains(step, text):

    def title_matches():
        pagetitle = world.page.title()
        return text in pagetitle

    retry(title_matches, timeout=30, message=f"page title is {text}")
