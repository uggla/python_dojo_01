# Chemin vers le code source
SRC = pokemon

.PHONY: check lint typecheck format tests cov hcov clean

# Tout en un
check: format lint typecheck tests

# Formattage auto avec Ruff
format:
	uv run ruff format --line-length 80 $(SRC)

# Linting (PEP8, imports, etc.)
lint:
	uv run ruff check $(SRC)

# Analyse statique des types
typecheck:
	uv run mypy $(SRC)

# Tests unitaires
tests:
	uv run pytest

# Coverage
cov:
	uv run pytest --cov-report term --cov=pokemon pokemon/tests/

# Html coverage
hcov:
	uv run pytest --cov-report html --cov=pokemon pokemon/tests/

# Remove coverage data
clean:
	rm -rf htmlcov
