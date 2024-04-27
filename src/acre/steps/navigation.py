from radish import when

from acre import controls


@when("I click the link {link:QuotedString}")
def i_click_the_link(step, link):
    link = controls.Link(text=link)
    link.click()
