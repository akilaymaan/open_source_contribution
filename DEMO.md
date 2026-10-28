# Classroom demonstration and faculty notes

## What was done

The original repository contained `README.md` and `calculator.py`. Its existing Git history was retained. The calculator's missing colons, malformed print calls, and indentation were corrected; its existing addition and subtraction intent was preserved. A main guard now allows tests to import the functions silently.

Nine standard-library unit tests were added. The README now explains setup, terminology, a ten-step contribution workflow, the historical defect, limitations, and a Mermaid diagram with test and review revision loops. A contribution guide, two issue templates, a PR template, and Python ignore rules complete the demonstration. No external Python dependencies were added.

The preparation created a local branch named `fix/calculator-and-contribution-guide`. The project was then prepared for direct publication to the original repository's `main` branch at the owner's request. In the published version, these changes are already committed: use a new, real documentation improvement for the live commit exercise below. No GitHub fork, issue, PR, review, or PR merge is claimed. Check `git status` before presenting.

## Before class

1. Open this prepared repository folder in a terminal. Run `git status`, `git branch --show-current`, and `git remote -v`.
2. Confirm Python and Git work, and run the program and tests once.
3. Keep this guide and the README available offline. Internet is needed only for GitHub actions.
4. Check `git var GIT_AUTHOR_IDENT` before committing. Configure your preferred repository-local name and email if absent; use your exact GitHub no-reply address if desired.
5. For GitHub steps, sign in through a supported authentication method and confirm push permission. Arrange a classmate reviewer if demonstrating independent review.

## Live sequence (about 8–10 minutes)

### 1. Introduce the repository — local

Show the README and small file structure. Explain that the calculator is the sample contribution; the main subject is collaboration using Git and GitHub.

### 2. Explain the original bug — local

Show the historical file without changing the working calculator:

```sh
git show c1d0553:calculator.py
```

This revision exists in the original history. Point out missing colons after both `def` statements, missing commas in the print calls, and incorrect indentation. The original program stops with `SyntaxError: expected ':'` at line 1. Then open today's `calculator.py` and explain the corrections and main guard. There is no need to break the working code live.

### 3. Run the code and tests — local

```sh
python calculator.py
python -m unittest -v
```

Show `Addition: 15`, `Subtraction: 5`, and nine passing tests. Explain why zero, negatives, operand order, and approximate float comparisons matter.

### 4. Create a branch and commit — local

For the first demonstration with the prepared uncommitted files, choose an unused branch name:

```sh
git switch -c demo/contribution-workflow
git diff
git add calculator.py test_calculator.py README.md CONTRIBUTING.md DEMO.md .gitignore .github
git diff --cached --stat
git diff --cached
git commit -m "fix: repair calculator and document contribution workflow"
git status
git log -1 --oneline
```

The branch starts at the current commit and carries the existing uncommitted work. Explain that staging selects changes and committing records a local snapshot. If the prepared work has already been committed, instead make a real small documentation improvement on a fresh branch, inspect it, stage only that file, and use an accurate commit message. Git cannot commit an unchanged working tree. Use a fresh branch name for repeated practice.

### 5. Push and explain the PR — GitHub account and network required

For this prepared clone, `origin` points to the original repository. As its owner, verify that remote before pushing:

```sh
git remote -v
git push -u origin demo/contribution-workflow
```

This publishes a branch and requires write permission. In GitHub, compare that branch against `main`, inspect **Files changed**, and complete the PR template. Describe the actual verification results. Only create a real PR when you intend to submit this work.

For a classmate contribution, follow the README fork procedure in a separate clone: `origin` must point to the classmate's fork and `upstream` to the original. The owner generally cannot fork their repository into the same personal account. Never run a contributor push against the original assuming it is a fork.

### 6. Review, revision, and merge — GitHub permissions required

Show the PR diff and test instructions. A classmate can leave real feedback. Explain that changes requested by review are tested, committed, and pushed to the same branch, updating the PR. The owner cannot approve their own PR. An authorized maintainer merges only when applicable requirements pass. If no review or merge occurs, explain these as remaining steps rather than completed actions.

### 7. Close with the workflow diagram — local or GitHub

Trace identify issue → fork → clone → branch → change → test → commit → push → PR → review → merge. Explain the feedback loop and the difference between a local commit and publication on GitHub.

## Permission boundaries

| Activity | Requirements |
| --- | --- |
| Read files, run Python/tests, create branch, commit | Local Python/Git; commit needs configured author identity. No GitHub account needed. |
| Clone/fetch a public repository | Internet and Git; generally no GitHub account. |
| Fork, report an issue, submit a PR, comment | GitHub account and applicable repository policies. |
| Push a branch | Authentication and write permission to the destination repository. |
| Approve a PR | Eligible reviewer account and repository policies; authors cannot approve their own PR. |
| Merge | Write permission or an authorized maintainer, plus required checks/reviews. |

## Short presentation script

“My project is Open Source Contribution Workflow Using Git and GitHub. It uses a small Python calculator to show how a contributor proposes a reliable change to a shared repository.

The original calculator could not run because function definitions were missing colons and the print statements had syntax and indentation errors. I corrected those errors and added an import guard. Addition and subtraction now run, and nine automated tests check normal inputs and edge cases.

Git tracks changes locally through branches and commits. GitHub hosts repositories and provides forks, issues, pull requests, and review. A fork is an online repository copy; a clone brings a repository to our computer. A branch isolates work, while a commit records a snapshot.

A contributor finds a problem, forks and clones the repository, creates a branch, changes the code, runs tests, commits, and pushes. A pull request asks a maintainer to review the change. Feedback leads to revisions on the same branch, and approved work can then be merged.

I also prepared setup instructions, contribution guidelines, issue and PR templates, and a diagram. The project is deliberately small so the complete workflow is easy to explain. I distinguish the local work actually completed from GitHub steps that still need to be performed.”

## Remaining GitHub steps

For a future contribution, make a real improvement on a new branch, commit and push it, open a real PR, obtain real review if available, address feedback, and merge with authorization. The published project files alone do not demonstrate that a PR was reviewed or merged. Templates are available once the files are on the default branch. Inspect the Mermaid rendering on GitHub after publication. The owner should separately choose a license; none has been selected automatically.
