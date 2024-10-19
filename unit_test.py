import unittest
from unittest.mock import patch
from io import StringIO
from main import joblink  


class Testjoblink(unittest.TestCase):
    def setUp(self):
        
        self.joblink = joblink()

    def tearDown(self):
        
        pass

    @patch('builtins.input', side_effect=["validusername", "invalidemail", "password", "1234567890", "Country", "School", "Degree"])
    @patch('getpass.getpass', return_value="password")
    def test_sign_up_invalid_email(self, mock_getpass, mock_input):
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.edu_connect.sign_up(self.edu_connect)
            output = fake_out.getvalue().strip()
            self.assertIn("Enter your details", output)
            self.assertIn("Enter Valid Email", output)

   

if __name__ == '__main__':
    unittest.main()
