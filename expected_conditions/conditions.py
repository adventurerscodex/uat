class url_in_new_tab_matches:  # noqa
    """Wait until new tab contains redirected url."""

    def __init__(self, url):
        """Init escpected condition."""
        self.url = url

    def __call__(self, driver):
        """Test if url matches."""
        return driver.current_url == self.url

class table_has_data:  # noqa
    """Wait until table has data."""

    def __init__(self, table):
        """Init escpected condition."""
        self.table = table

    def __call__(self, driver):
        """Test if table has more than one column."""
        tds = self.table.find_elements_by_tag_name('td')

        return len(tds) > 1
