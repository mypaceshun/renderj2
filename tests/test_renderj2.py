from pathlib import Path

from click.testing import CliRunner

from renderj2.renderj2 import cmd


def test_command_help():
    runner = CliRunner()
    result = runner.invoke(cmd, ["--help"])
    assert result.exit_code == 0

    result = runner.invoke(cmd, ["-h"])
    assert result.exit_code == 0


def test_command_version():
    runner = CliRunner()
    result = runner.invoke(cmd, ["--version"])
    assert result.exit_code == 0

    result = runner.invoke(cmd, ["-V"])
    assert result.exit_code == 0


def test_no_exists_template(tmp_path):
    no_exists_template = Path(tmp_path, "no_exists_template.txt")
    assert no_exists_template.exists() is False

    runner = CliRunner()
    result = runner.invoke(cmd, [str(no_exists_template)])
    assert result.exit_code != 0


def test_no_exists_variable(tmp_path):
    template_path = Path(tmp_path, "template.txt")
    template_path.write_text("test")

    variable_path = Path(tmp_path, "no_exists_variables.yml")
    assert template_path.exists() is True
    assert variable_path.exists() is False

    runner = CliRunner()
    result = runner.invoke(cmd, ["-v", str(variable_path), str(template_path)])
    assert result.exit_code != 0


def test_success_tempalte_render(tmp_path):
    template_path = Path(tmp_path, "success_template")
    template_string = "test template string no variables"
    template_path.write_text(template_string)

    runner = CliRunner()
    result = runner.invoke(cmd, [str(template_path)])
    assert result.exit_code == 0
    stdout = result.stdout
    assert stdout.strip() == template_string.strip()


def test_success_template_render_with_one_variable_file(tmp_path):
    template_path = Path(tmp_path, "success_template_with_variables")
    template_string = """test template string with variables
Hello {{ name }}!
"""
    template_path.write_text(template_string)

    variable_path = Path(tmp_path, "variable.yml")
    variable_string = """---
name: shun
"""
    variable_path.write_text(variable_string)

    expect_string = """test template string with variables
Hello shun!
"""

    runner = CliRunner()
    result = runner.invoke(cmd, ["-v", str(variable_path), str(template_path)])
    assert result.exit_code == 0
    stdout = result.stdout
    assert stdout.strip() == expect_string.strip()


def test_success_template_render_with_multi_variable_file(tmp_path):
    template_path = Path(tmp_path, "success_template_with_variables")
    template_string = """test template string with variables
Hello {{ name1 }} and {{ name2 }}!
"""
    template_path.write_text(template_string)

    variable1_path = Path(tmp_path, "variable1.yml")
    variable1_string = """---
name1: shun1
"""
    variable1_path.write_text(variable1_string)

    variable2_path = Path(tmp_path, "variable2.yml")
    variable2_string = """---
name2: shun2
"""
    variable2_path.write_text(variable2_string)

    expect_string = """test template string with variables
Hello shun1 and shun2!
"""

    runner = CliRunner()
    result = runner.invoke(
        cmd, ["-v", str(variable1_path), "-v", str(variable2_path), str(template_path)]
    )
    assert result.exit_code == 0
    stdout = result.stdout
    assert stdout.strip() == expect_string.strip()


def test_success_template_render_output_to_file(tmp_path):
    template_path = Path(tmp_path, "success_template_with_variables")
    template_string = """test template string with variables
Hello {{ name }}!
"""
    template_path.write_text(template_string)

    variable_path = Path(tmp_path, "variable.yml")
    variable_string = """---
name: shun
"""
    variable_path.write_text(variable_string)

    expect_string = """test template string with variables
Hello shun!
"""

    output_path = Path(tmp_path, "success_output")

    runner = CliRunner()
    result = runner.invoke(
        cmd,
        ["-v", str(variable_path), "--output", str(output_path), str(template_path)],
    )
    assert result.exit_code == 0
    stdout = result.stdout
    assert stdout.strip() == ""
    assert output_path.read_text().strip() == expect_string.strip()
