from playwright.sync_api import Page, expect


def test_ui_sum(page: Page):
    page.goto("http://127.0.0.1:8000/ui/sum?a=1&b=2")
    div = page.locator('//div[@id="sum"]')
    expect(div).to_contain_text("3")
    page.wait_for_timeout(3000)


def test_ui_double_sum(page: Page):
    page.goto("http://127.0.0.1:8000/ui/double_sum?a=1&b=2")
    div = page.locator('//div[@id="double_sum"]')
    expect(div).to_contain_text("6")
    page.wait_for_timeout(3000)
