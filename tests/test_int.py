def test_empty_validation(self):
        self.submit_input('')
        self.assertIn(url_for('index'), self.driver.current_url)

        text = self.driver.find_element_by_xpath('<XPath>').text
        self.assertIn("The name field can't be empty!", text)

        entries = Games.query.all()
        self.assertEqual(len(entries), 0) # database should be empty
