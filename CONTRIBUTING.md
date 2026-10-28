# Contributing

Keep contributions small and easy to explain. Read the README before starting.

## Report bugs and suggest improvements

Search existing issues first. Use the bug report template for reproducible defects: include your command, Python version, expected output, actual output, and relevant error text. Use the feature template to explain a problem, proposed solution, and fit with this teaching project. Do not post credentials or private information.

## Local setup

Install Python 3 and Git. Fork on GitHub, then replace `YOUR_USERNAME`:

```sh
git clone https://github.com/YOUR_USERNAME/open_source_contribution.git
cd open_source_contribution
git remote add upstream https://github.com/akilaymaan/open_source_contribution.git
git switch -c fix/short-description
```

No Python packages need installing. For later contributions, follow the README to sync from `upstream/main` before branching.

## Branch names and coding standards

Use `fix/description`, `feat/description`, `docs/description`, or `test/description`. Use lowercase words separated by hyphens.

Use four-space indentation, meaningful `snake_case` names, and short functions. Comment where a beginner needs an explanation. Keep example output under the main guard. Add or update tests for behavior changes and documentation for changed commands. Prefer the standard library and avoid unrelated changes.

## Test and commit

From the repository root:

```sh
python calculator.py
python -m unittest -v
git diff --check
git diff
```

Substitute `py` or `python3` if appropriate for your system. Stage only relevant files with `git add FILE_NAME` (replace the placeholder), then inspect `git diff --cached`. Configure your Git author identity if necessary.

Use concise imperative commit messages with prefixes, such as `fix: correct subtraction behavior`, `test: cover zero operands`, or `docs: clarify setup`. Never commit secrets.

## Submit a pull request

Commit, then push your branch (substitute your branch name):

```sh
git push -u origin fix/short-description
```

Open a PR from your fork's branch to `akilaymaan/open_source_contribution:main`. Complete summary, changes, testing, and checklist sections. Link only real related issues. Give actual test results and request review. Apply revisions on the same branch, test, commit, and push again.

## Maintainer review before merging

- Confirm the defect and keep the solution within project scope.
- Inspect the full diff for correctness, clarity, unrelated edits, and secrets.
- Run the calculator and tests; check relevant edge cases.
- Check documentation commands, links, and templates.
- Resolve feedback and conflicts before merging.
- Merge only with repository permission and after applicable review requirements pass.

A PR is a proposal, not proof of approval or merge. There is no license file yet; the owner must decide licensing terms.
