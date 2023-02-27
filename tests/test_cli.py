"""
kryptoxin basic test module.
This module holds the basic tests for the kryptoxin package.
"""
import unittest
from click.testing import CliRunner
from kryptoxin.core import cli

# Constants
_TEST_TXTFILE_PATH = 'tests/samples/input_file.txt'
_TEST_BINFILE_PATH = 'tests/samples/random.bin'
_TEST_CTTMPFILE_PATH = '/tmp/kryptoxin_test_out.bin'


class TestCli(unittest.TestCase):
    def test_cli_encrypt_basic(self):
        """
        Basic test of the core CLI's 'encrypt' function.
        core.cli.encrypt() has no mandatory arguments, only options.
        """
        in_file = _TEST_TXTFILE_PATH
        key = '12345'

        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', in_file])
        self.assertEqual(
            result.output, "tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=\n")

    def test_cli_encrypt_infile(self):
        """
        Encryption and parameter tests of the core CLI with a
        text file as input. The goal here is to ensure
        command-line options are all correct.
        """
        in_file = _TEST_TXTFILE_PATH
        key = '12345'
        iv = 'A' * 16
        salt = 'B' * 16
        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', in_file,
                               '--alg', 'aes', '--key_size',
                               '128', '--mode', 'cbc', '--iv', iv,
                               '--salt', salt, '--hmac', 'sha256',
                               '--iter', '50000'])
        self.assertEqual(
            result.output, "nY8lsP+MabdA8ErXQP/M3wyuJX4ZaM3GVFEKA2nHOms=\n")

    def test_cli_encrypt_binfile(self):
        """
        Encryption test with a binary file.
        May catch issues with handling of binary file encoding.
        """
        in_file = _TEST_BINFILE_PATH
        key = '12345'
        iv = 'A' * 16
        salt = 'B' * 16
        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', in_file,
                               '--alg', 'aes', '--key_size', '128',
                               '--mode', 'cbc', '--iv', iv,
                               '--salt', salt, '--hmac', 'sha256',
                               '--iter', '50000'])
        self.assertEqual(result.output, "nY8lsP+MabdA8ErXQP/M385ln0QlbcTF/Wa90"
                                        "X4DZLPG5w8308pRq9H72Tg1+hQKuSlJ8YrsQR"
                                        "/oWFkSiCQ8S81MwhOgE1Fc4OjIrrntWsrdqJf"
                                        "v8CwaHnkt339CwmGE\n")

    def test_cli_decrypt_txtfile(self):
        """
        Test decrypt command with a text file.
        """
        in_file = _TEST_TXTFILE_PATH
        ct_file = _TEST_CTTMPFILE_PATH
        key = '12345'
        iv = 'A' * 16
        salt = 'B' * 16
        runner = CliRunner()

        # First perform encryption
        encrypt_res = runner.invoke(cli.encrypt, [
            '--key', key, '--in', in_file,
            '--key_size', '128',
            '--mode', 'cbc', '--iv', iv,
            '--salt', salt, '--hmac', 'sha256',
            '--iter', '50000',
            '--out', ct_file])
        if encrypt_res.exception:
            print(f"{encrypt_res.exception}")

        # Second perform decryption
        decrypt_res = runner.invoke(cli.decrypt, [
            '--key', key, '--in', ct_file,
            '--key_size', '128',
            '--mode', 'cbc', '--iv', iv,
            '--salt', salt, '--hmac', 'sha256',
            '--iter', '50000'])

        print(decrypt_res.output)

        # Check results
        if not decrypt_res.exception:
            # read original input file in non-binary mode
            # close it, and strip the console's new-line char
            # for comparison.
            f = open(_TEST_TXTFILE_PATH, 'r')
            file_pt = f.read()
            f.close()
            self.assertEqual(decrypt_res.output[:-1], file_pt)
        else:
            # if an exception arise during decryption
            # print the error.
            print(f"{decrypt_res.exception}")


if __name__ == '__main__':
    unittest.main()
