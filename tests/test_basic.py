import unittest
from click.testing import CliRunner

from kryptoxin.core import cli, TEST_TXTFILE_PATH


class TestCli(unittest.TestCase):
    def test_cli_in_basic(self):
        """
        Basic test of the core CLI's 'encrypt' function.
        core.cli.encrypt() has no mandatory arguments, only options.
        """
        key = '12345'

        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', TEST_TXTFILE_PATH])
        self.assertEqual(
            result.output, "tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=\n")

    def test_cli_in_crypto(self):
        """
        Encryption and parameter tests of the core CLI with a text file as input.
        The goal here is to ensure command-line options are all correct.
        """
        key = '12345'
        iv = 'A'*16
        salt = 'B'*16
        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', TEST_TXTFILE_PATH,
                               '--alg', 'aes', '--key_size', '128', '--mode', 'cbc', '--iv', iv,
                               '--salt', salt, '--hmac', 'sha256', '--iter', '50000'])
        print(f"Test result is: {result.output}")
        self.assertEqual(
            result.output, "nY8lsP+MabdA8ErXQP/M3wyuJX4ZaM3GVFEKA2nHOms=\n")

    def test_cli_in_random(self):
        """
        Encryption test with a random binary file.
        May catch issues with handling of binary file encoding.
        """
        in_file = 'tests/samples/random.bin'
        key = '12345'
        iv = 'A'*16
        salt = 'B'*16
        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', in_file,
                               '--alg', 'aes', '--key_size', '128', '--mode', 'cbc', '--iv', iv,
                               '--salt', salt, '--hmac', 'sha256', '--iter', '50000'])
        print(f"Test result is: {result.output}")
        self.assertEqual(
            result.output, "nY8lsP+MabdA8ErXQP/M385ln0QlbcTF/Wa90X4DZLPG5w8308pRq9H72Tg1+hQKuSlJ8YrsQR/oWFkSiCQ8S81MwhOgE1Fc4OjIrrntWsrdqJfv8CwaHnkt339CwmGE\n")


if __name__ == '__main__':
    unittest.main()
