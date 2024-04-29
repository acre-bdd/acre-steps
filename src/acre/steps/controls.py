from radish import when, then, custom_type

from acre.controls import factory


@custom_type("Control", r"[\w\.]+")
def control(name):
    return name


@when("I click the {control:Control}")
def i_click_the_control(step, control: str):
    """ Click on the *first* control of type **controltype**.

        Args:
            controltype:
                The type of control to click to. See <def:control type}
                for details.
    """
    link = factory.create(control)
    link.first.click()


@when("I click the {control:Control} {text:QuotedString}")
def i_click_the_conrol_with_text(step, control: str, text: str):
    """ Click on the *first* control of type **control**
        with the given **text**.

        Args:
            control:
                The type of control to click to. See <def:control type}
                for details.
            text:
                The text of the control type to click to. If the text
                begins with a "*", then a partial match search is done.
    """
    link = factory.create(control, _=text)
    link.first.click()


@when('I enter {text:QuotedString} to the {control:Control}')
def i_enter_text(step, text, control):
    ctrl = factory.create(control)
    ctrl.fill(text)


@then('I see the {control:Control} {text:QuotedString}')
def i_see_control_with_text(step, control, text):
    ctrl = factory.create(control, _=text)
    ctrl.first.wait_for()
