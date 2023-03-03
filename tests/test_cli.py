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
_TEST_CTTMPFILE_PATH = 'tests/samples/cli_decrypt_enc-out.bin'


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
            result.output, "5bP32GKoJa57IcKL4sWeUQ==\n")

    def test_cli_encrypt_infile(self):
        """
        Encryption and parameter tests of the core CLI with a
        text file as input. The goal here is to ensure
        command-line options are all correct.
        """
        in_file = _TEST_TXTFILE_PATH
        key = '12345'
        iv = 'A' * 32
        salt = 'B' * 32
        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', in_file,
                               '--alg', 'aes', '--key_size',
                               '128', '--mode', 'cbc', '--iv', iv,
                               '--salt', salt, '--hmac', 'sha256',
                               '--iter', '50000'])
        self.assertEqual(
            result.output, "iz+bKSFUYsFoBELwk5Ds5g==\n")

    def test_cli_encrypt_binfile(self):
        """
        Encryption test with a binary file.
        May catch issues with handling of binary file encoding.
        """
        in_file = _TEST_BINFILE_PATH
        key = '12345'
        iv = 'A' * 32
        salt = 'B' * 32
        runner = CliRunner()
        result = runner.invoke(cli.encrypt, [
                               '--key', key, '--in', in_file,
                               '--alg', 'aes', '--key_size', '128',
                               '--mode', 'cbc', '--iv', iv,
                               '--salt', salt, '--hmac', 'sha256',
                               '--iter', '50000'])
        self.assertEqual(result.output, "LoFcYFcRDvcNKHxyJCFBY/Er32HPoiWImRR+"
                                        "VJp4A7punV/DJxLyxESGdoHE8aPD5UKYyJ1Z"
                                        "GIHg8zQBdDVz2OdOsxk19elVTsOYWyr3NEE="
                                        "\n")

    def test_cli_decrypt_txtfile(self):
        """
        Test decrypt command with a text file.
        """
        in_file = _TEST_TXTFILE_PATH
        ct_file = _TEST_CTTMPFILE_PATH
        key = '12345'
        iv = 'A' * 32
        salt = 'B' * 32
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
            raise SystemError


if __name__ == '__main__':
    unittest.main()
