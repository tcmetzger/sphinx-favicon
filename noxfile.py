"""Test process to run in isolated environments."""

import nox


@nox.session(python=["3.7", "3.8", "3.9"], reuse_venv=True)
def test(session):
    """Apply the tests on the lib."""
    session.install(".[test]")
    session.run("pytest", "--color=yes", "tests")


@nox.session(name="mypy", reuse_venv=True)
def mypy(session):
    """Run the mypy evaluation of the lib."""
    session.install(".")
    session.install("mypy")
    test_files = session.posargs or ["sphinx_favicon"]
    session.run(
        "mypy",
        "--ignore-missing-imports",
        "--install-types",
        "--non-interactive",
        *test_files,
    )
