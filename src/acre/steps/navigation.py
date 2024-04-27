from radish import when

from acre.controls import Link


@when("I click the link {link:QuotedString}")
def i_click_the_link(step, link):
    link = Link(text=link)
    link.click()
