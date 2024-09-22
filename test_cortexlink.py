import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import CortexLink


class TestCortexLink(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('CortexLink.search')
    def test_perform_search_with_proxy(self, mock_search, mock_file):
        # Mock search results
        mock_search.return_value = ['http://example.com', 'http://example.org']
        
        # Call perform_search with test parameters
        with patch('sys.stdout', new=StringIO()) as fake_out:
            CortexLink.perform_search(query="test", proxy="http://user:pass@proxy.com", use_table=False)
            # Check if the results are printed correctly
            self.assertIn('http://example.com', fake_out.getvalue())
            self.assertIn('http://example.org', fake_out.getvalue())
        
        # Check if the results were written to file
        mock_file().write.assert_any_call('http://example.com\n')
        mock_file().write.assert_any_call('http://example.org\n')
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('CortexLink.search')
    def test_perform_search_without_proxy(self, mock_search, mock_file):
        # Mock search results
        mock_search.return_value = ['http://example.com', 'http://example.org']
        
        # Call perform_search without proxy
        with patch('sys.stdout', new=StringIO()) as fake_out:
            CortexLink.perform_search(query="test", use_table=False)
            # Check if the results are printed correctly
            self.assertIn('http://example.com', fake_out.getvalue())
            self.assertIn('http://example.org', fake_out.getvalue())
        
        # Check if the results were written to file
        mock_file().write.assert_any_call('http://example.com\n')
        mock_file().write.assert_any_call('http://example.org\n')
    
    @patch('CortexLink.search')
    @patch('sys.stdout', new_callable=StringIO)
    def test_perform_search_with_table(self, mock_stdout, mock_search):
        # Mock search results
        mock_search.return_value = ['http://example.com', 'http://example.org']
        
        # Call perform_search with use_table=True
        CortexLink.perform_search(query="test", use_table=True)
        
        # Check if table format is printed
        output = mock_stdout.getvalue()
        self.assertIn("No", output)
        self.assertIn("URL", output)
        self.assertIn("http://example.com", output)
        self.assertIn("http://example.org", output)
    
    @patch('CortexLink.search')
    @patch('sys.stdout', new_callable=StringIO)
    def test_perform_search_without_color(self, mock_stdout, mock_search):
        # Mock search results
        mock_search.return_value = ['http://example.com', 'http://example.org']
        
        # Call perform_search with no_color=True
        CortexLink.perform_search(query="test", use_table=False, no_color=True)
        
        # Check if output is printed without color
        output = mock_stdout.getvalue()
        self.assertIn('http://example.com', output)
        self.assertIn('http://example.org', output)
    
    @patch('CortexLink.search')
    @patch('sys.stdout', new_callable=StringIO)
    def test_perform_search_with_language_and_region(self, mock_stdout, mock_search):
        # Mock search results
        mock_search.return_value = ['http://example.com', 'http://example.org']
        
        # Call perform_search with language and region specified
        CortexLink.perform_search(query="test", region="us", lang="fr")
        
        # Check if results are printed
        output = mock_stdout.getvalue()
        self.assertIn('http://example.com', output)
        self.assertIn('http://example.org', output)
    
    @patch('CortexLink.perform_search')
    def test_main_cve_search(self, mock_perform_search):
        # Simulate argument parsing for a CVE search
        test_args = ['CortexLink.py', '-query', 'splunk', '-cve']
        with patch('sys.argv', test_args):
            CortexLink.main()
            mock_perform_search.assert_called_with(
                query="splunk CVE list",
                num_results=10,
                region=None,
                lang="en",
                output_file="Cortex-Link-Result.txt",
                use_table=False,
                no_color=False,
                proxy=None,
                ssl_verify=True,
                sleep_interval=0
            )
    
    @patch('CortexLink.perform_search')
    def test_main_exploit_search(self, mock_perform_search):
        # Simulate argument parsing for an exploit search
        test_args = ['CortexLink.py', '-query', 'splunk', '-exploit']
        with patch('sys.argv', test_args):
            CortexLink.main()
            mock_perform_search.assert_called_with(
                query="splunk exploits download",
                num_results=10,
                region=None,
                lang="en",
                output_file="Cortex-Link-Result.txt",
                use_table=False,
                no_color=False,
                proxy=None,
                ssl_verify=True,
                sleep_interval=0
            )


if __name__ == '__main__':
    unittest.main()
