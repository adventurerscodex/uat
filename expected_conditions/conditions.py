class url_in_new_tab_matches:  # noqa
    """Wait until new tab contains redirected url."""

    def __init__(self, url):
        """Init escpected condition."""
        self.url = url

    def __call__(self, driver):
        """Test if url matches."""
        return driver.current_url == self.url
