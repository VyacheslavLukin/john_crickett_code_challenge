from ccwc import cli
from click.testing import CliRunner

# Tests were written in a TDD manner

def test_should_return_zero_bytes_and_filename_for_empty_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('empty.txt', 'w') as f:
            f.write('')
        
        result = runner.invoke(cli, ['-c','empty.txt'])
        assert result.exit_code == 0
        assert result.output == "0 empty.txt\n"

def test_should_return_bytes_and_filename_for_non_empty_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('ten_bytes.txt', 'w') as f:
            f.write('1234567890')
        
        result = runner.invoke(cli, ['-c', 'ten_bytes.txt'])
        assert result.exit_code == 0
        assert result.output == "10 ten_bytes.txt\n"

def test_should_return_zero_lines_for_empty_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('empty.txt', 'w') as f:
            f.write('')
        
        result = runner.invoke(cli, ['-l','empty.txt'])
        assert result.exit_code == 0
        assert result.output == "0 empty.txt\n"

def test_should_return_number_of_lines_for_non_empty_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('ten_lines.txt', 'w') as f:
            f.write('1\n2\n3\n4\n5\n6\n7\n8\n9\n10')
        
        result = runner.invoke(cli, ['-l','ten_lines.txt'])
        assert result.exit_code == 0
        assert result.output == "10 ten_lines.txt\n"

def test_should_return_zero_character_for_empty_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('empty.txt', 'w') as f:
            f.write('')
        
        result = runner.invoke(cli, ['-m','empty.txt'])
        assert result.exit_code == 0
        assert result.output == "0 empty.txt\n"

def test_should_return_number_of_characters_for_non_empty_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('ten_char.txt', 'w') as f:
            f.write('1234567890')
        
        result = runner.invoke(cli, ['-m','ten_char.txt'])
        assert result.exit_code == 0
        assert result.output == "10 ten_char.txt\n"

def test_should_return_bytes_lines_chars_when_no_option():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('ten_char.txt', 'w') as f:
            f.write('1234567890')
        
        result = runner.invoke(cli, ['ten_char.txt'])
        assert result.exit_code == 0
        assert result.output == "1 1 10 ten_char.txt\n"
