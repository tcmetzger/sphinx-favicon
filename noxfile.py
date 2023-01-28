"""Test process to run in isolated environments."""

import nox


@nox.session(reuse_venv=True)
def test(session):
    """Apply the tests on the lib."""
    session.install(".[test]")
    test_files = session.posargs or ["tests"]
    session.run("pytest", "--color=yes", *test_files)


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


@nox.session(name="docs", reuse_venv=True)
def docs(session):
    """Build the docs."""
    session.install(".[doc]")
    session.run(
        "sphinx-build", "-b=html", *session.posargs, "docs/source", "docs/build/html"
    )


@nox.session(reuse_venv=True)
def lint(session):
    """Run pre-commit linting checks."""
    session.install(".[test]")
    session.run("pre-commit", "run", "--all-files", external=True)
