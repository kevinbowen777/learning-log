"""Nox sessions."""
import tempfile

import nox

nox.options.sessions = "lint", "safety", "tests"
locations = "accounts", "config", "learning_logs", "pages", "./noxfile.py"


def install_with_constraints(session, *args, **kwargs):
    """Install packages constrained by Poetry's lock file."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.10", "3.9"])
def black(session):
    """Run black code formatter."""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python=["3.10", "3.9"])
def docs(session):
    """Build the documentation."""
    install_with_constraints(session, "sphinx")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python=["3.10", "3.9"])
def lint(session):
    """Lint using flake8."""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=["3.10", "3.9"])
def safety(session):
    """Scan dependencies for insecure packages."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run(
            "safety", "check", f"--file={requirements.name}", "--full-report"
        )


@nox.session(python=["3.10", "3.9"])
def tests(session):
    """Run the test suite."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session,
        "coverage[toml]",
        "django-coverage-plugin",
        "factory-boy",
        "pytest",
        "pytest-cov",
        "pytest-django",
    )
    session.run("pytest", *args)
