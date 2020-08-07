import autobahn
from autobahn.asyncio.component import Component
from autobahn.asyncio.component import run

import asyncio

from behave import given, when, then # pylint: disable=no-name-in-module
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DEFAULT_TIMEOUT = 2 #seconds

@given('the user has loaded the diagnostic page')
def given_diagnostics_loaded(context):
    context.browser.get("http://webapp/diagnostics.html")
    assert "404" not in context.browser.title

@given('the pitch axis positive limit switch is activated')
def given_pos_lim_switch_activated_step(context):
    comp = Component(transports='ws://crossbar:8080/ws', realm='realm1')

    @comp.on_join
    async def _(session: autobahn.asyncio.component.Session, details):
        await session.call('nl.matthijsbos.nerdrage.set_poslim', True)
        await session.leave()

    asyncio.get_event_loop().run_until_complete(comp.start())
    

@given('the pitch axis positive limit switch is deactivated')
def given_pos_lim_switch_deactivated_step(context):
    comp = Component(transports='ws://crossbar:8080/ws', realm='realm1')

    @comp.on_join
    async def _(session: autobahn.asyncio.component.Session, details):
        await session.call('nl.matthijsbos.nerdrage.set_poslim', False)
        await session.leave()

    asyncio.get_event_loop().run_until_complete(comp.start())

@given(u'the pitch axis negative limit switch is activated')
def step_impl(context):
    comp = Component(transports='ws://crossbar:8080/ws', realm='realm1')

    @comp.on_join
    async def _(session: autobahn.asyncio.component.Session, details):
        await session.call('nl.matthijsbos.nerdrage.set_neglim', False)
        await session.leave()

    asyncio.get_event_loop().run_until_complete(comp.start())

@then(u'the pitch axis negative limit switch indicator is enabled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the pitch axis negative limit switch indicator is enabled')


@given(u'the pitch axis negative limit switch is deactivated')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the pitch axis negative limit switch is deactivated')


@then(u'the pitch axis negative limit switch indicator is disabled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the pitch axis negative limit switch indicator is disabled')


@when(u'the pitch axis negative limit switch is activated')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the pitch axis negative limit switch is activated')


@when(u'the pitch axis negative limit switch is deactivated')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the pitch axis negative limit switch is deactivated')

@when('the pitch axis positive limit switch is activated')
def when_pos_lim_switch_activated_step(context):
    comp = Component(transports='ws://crossbar:8080/ws', realm='realm1')

    @comp.on_join
    async def _(session: autobahn.asyncio.component.Session, details):
        await session.call('nl.matthijsbos.nerdrage.set_poslim', True)
        await session.leave()

    asyncio.get_event_loop().run_until_complete(comp.start())

@when('the pitch axis positive limit switch is deactivated')
def when_pos_lim_switch_deactivated_step(context):
    comp = Component(transports='ws://crossbar:8080/ws', realm='realm1')

    @comp.on_join
    async def _(session: autobahn.asyncio.component.Session, details):
        await session.call('nl.matthijsbos.nerdrage.set_poslim', False)
        await session.leave()

    asyncio.get_event_loop().run_until_complete(comp.start())


@then('the pitch axis positive limit switch indicator is enabled')
def then_pos_lim_switch_indicator_enabled(context):
    WebDriverWait(context.browser, DEFAULT_TIMEOUT).until(
        ec.element_located_to_be_selected((By.ID, 'poslim'))
    )

@then('the pitch axis positive limit switch indicator is disabled')
def then_pos_lim_switch_indicator_diabled(context):
    WebDriverWait(context.browser, DEFAULT_TIMEOUT).until_not(
        ec.element_located_to_be_selected((By.ID, 'poslim'))
    )


@then('the connection indicator must be visible')
def then_connection_indicator_visible(context):
    WebDriverWait(context.browser, DEFAULT_TIMEOUT).until(
        ec.text_to_be_present_in_element((By.ID, 'myspan'), 'connected')
    )

@given(u'the turret light is emitting a red light')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the turret light is emitting a red light')


@then(u'the light color indicator is colored red')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the light color indicator is colored red')


@given(u'the turret light is emitting a blue light')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the turret light is emitting a blue light')


@then(u'the light color indicator is colored blue')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the light color indicator is colored blue')


@given(u'the light color indicator is colored red')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the light color indicator is colored red')


@when(u'the turret light is emitting a green light')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the turret light is emitting a green light')


@then(u'the light color indicator is colored green')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the light color indicator is colored green')