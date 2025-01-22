from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_login_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/login")    # We look at the <p> tag
    h1_tag = page.locator("h1")    # We assert that it has the text "This is the homepage."
    expect(h1_tag).to_have_text("Log in to MakersBnB")
    p_tags = page.locator("p")
    expect(p_tags.nth(0)).to_have_text("Enter email:")
    expect(p_tags.nth(1)).to_have_text("Enter password:")

def test_get_index_logged_out(db_connection, page, test_web_address):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/index")
    h1_tag = page.locator("h1")    # We assert that it has the text "This is the homepage."
    expect(h1_tag).to_have_text("Please log in to access your dashboard.")

def test_create_account_get_logged_in(db_connection, page, test_web_address):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/create_account")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Create A MakersBnB Account")
    page.fill("input[name=email]",  "abc@email.com")
    page.fill("input[name=username]",  "abc")
    page.fill("input[name=password]", 'abc')
    page.click("text=Create Account")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Log in to MakersBnB")
    page.fill("input[name=email]",  "abc@email.com") 
    page.fill("input[name=password]", 'abc')
    page.click("text=Login")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Welcome, abc")