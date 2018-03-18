"""Custom expected conditions."""

from utils import utils as ut

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
        """Init expected condition."""
        self.table = table

    def __call__(self, driver):
        """Test if table has more than one column."""
        tds = self.table.find_elements_by_tag_name('td')

        return len(tds) > 1

class element_is_clickable:  # noqa
    """Wait element is clickable."""

    def __init__(self, element):
        """Init expected condition."""
        self.element = element

    def __call__(self, driver):
        """Test if element is clickable."""
        return all([self.element.is_enabled(), self.element.is_displayed()])

class table_cell_updated: # noqa
    """Wait until cell data has updated."""

    def __init__(self, table, header, expected, table_attr, row_number):
        """Init expected condition.

        :table: Table component
        :header: Name of the table header
        :expected: Expected value cell value should be
        :table_attr: Name of the attr of table reference, usually 'table'
        :row_number: Row number to retrieve
        """
        self.table = table
        self.header = header
        self.expected = expected
        self.table_attr = table_attr
        self.row_number = row_number

    def __call__(self, driver):
        """Test if col value has updated."""
        row = ut.get_table_row(
            self.table,
            self.table_attr,
            row_number=self.row_number
        )

        actual = getattr(row, self.header)

        return actual == self.expected
