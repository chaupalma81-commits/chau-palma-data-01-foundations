# datafun-01-foundations

> Professional Python project: creating variables and running code.

## Project Planning

Think about different kinds of data - real or fictional.
Then think about a good name to hold that value in code.

1. A **True or False** value (e.g. `isWorking`, `isParent`, `hasPet`)
2. An **integer** (e.g. `year_starting_grad_school`)
3. A **floating point number** (e.g. `experience_factor`)
4. A **string of characters (text)** (e.g. `city`, `company_name`, `analytic_specialty`)
5. A **list of strings** (e.g., `skills`, `interests`, `favorite_teams`)

Following the example ([`app_case.py`](./src/datafun_01_foundations/app_case.py)),
decide on a name for each type of variable.

In this project, you will:

- choose variable names according to Python conventions.
- signal the **type** of value each variable holds by using `type hints`.
- **initialize** each variable to a value.
- use Python **f-strings** (formatted strings) to display information.

Important: <mark>Git add-commit-push **project.log**</mark> (along with other project files).
---

## Three Workflows

There are three workflows for analytics projects.

- 01: Set Up Machine (Once Per Machine)
- 02: Set Up Project (Once Per Project)
- 03: Daily Workflow (Working With Python Project Code)

## 01: Set Up Machine (Once Per Machine)

Follow the detailed instructions at:
[**01. Set Up Your Machine**](https://denisecase.github.io/pro-analytics-02/01-set-up-machine/)

🛑 All steps must be completed and verified successfully.

## 02: Set Up Project (Once Per Project)

Start with the list below. If you would like more detailed instructions on any step, see the pro guide at:
[**02. Set Up Your Project**](https://denisecase.github.io/pro-analytics-02/02-set-up-project/)

Start here:

1. Sign in to GitHub, open this repository in your browser, and click **Copy this template** to get a copy in **YOURACCOUNT**.
2. Enable GitHub Pages.
3. Open a **machine terminal** in your `Repos` folder and clone your new repo.
4. Change directory into the repo, open the project in VS Code, and install recommended extensions.
5. Set up a project Python environment (managed by `uv`) and align VS Code with it.

Use the instructions above to get it ALL set up correctly.
Most people open a terminal on their machine (not VS Code), open in their Repos folder and run:

```shell
git clone https://github.com/YOURACCOUNT/datafun-01-foundations

cd datafun-01-foundations
code .
```

When VS Code opens, accept the Extension Recommendations (click **`Install All`** or similar when asked).

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal** in the root project folder.
Run the following commands, one at a time, hitting ENTER after each:

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

If asked: "We noticed a new environment has been created. Do you want to select it for the workspace folder?" Click **"Yes"**.

If successful, you'll see a new `.venv` folder appear in the root project folder.

Optional (recommended): install and run pre-commit checks (repeat the git `add` and `commit` twice if needed):

```shell
uvx pre-commit install
git add -A
uvx pre-commit run --all-files
git add -A
uvx pre-commit run --all-files
```

🛑 Do not continue until all REQUIRED steps are complete and verified.

## 03: Daily Workflow (Working With Python Project Code)

Follow the detailed instructions at:
[**03. Daily Workflow**](https://denisecase.github.io/pro-analytics-02/03-daily-workflow/)

Commands are provided below to:

1. Git pull
2. Run and check the Python files
3. Build and serve docs
4. Save progress with Git add-commit-push
5. Update project files

VS Code should have only this project (datafun-01-foundations) open.
Use VS Code menu option `Terminal` / `New Terminal` and run the following commands:

```shell
git pull
```

In the same VS Code terminal, run any Python source files:

```shell
uv run python src/datafun_01_foundations/app_case.py
uv run python src/datafun_01_foundations/app_chaupalma.py
```

If a command fails, verify:

- Only this project is open in VS Code.
- The terminal is open in the project root folder.
- The `uv sync --extra dev --extra docs --upgrade` command completed successfully.

Hint: if you run `ls` in the terminal, you should see files including `pyproject.toml`, `README.md`, and `uv.lock`.

Run Python checks and tests (as available):

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

Build and serve docs (hit **CTRL+c** in the VS Code terminal to quit serving):

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

While editing project code and docs, repeat the commands above to run files, check them, and rebuild docs as needed.

Save progress frequently (some tools may make changes; you may need to **re-run git `add` and `commit`** to ensure everything gets committed before pushing):

```shell
git add -A
git commit -m "update"
git push -u origin main
```

Additional details and troubleshooting are available in the [Pro-Analytics-02 Documentation](https://denisecase.github.io/pro-analytics-02/).

---

## Project Objectives

### Project Task 1. Personalize Your Documentation Links

Open [mkdocs.yaml](./mkdocs.yaml).
This file configures the associated project documentation website (powered by MkDocs)
Use CTRL+f to find each occurrence of the source GitHub account (e.g. `denisecase`).
Change each occurrence to point to your GitHub account instead (spacing and capitalization MUST match the URL of your GitHub account **exactly**.)

### Project Task 2. Personalize Your Python File

1. Rename `app_chaupalma.py` to reflect your name or alias.

- Find the file the file in the VS Code Explorer window (top icon on the left).
- Right-click / Rename.
- Follow conventions: name Python files in lower_snake_case, words joined with underscores, and using `.py` extension.

2. Edit this README.md file to change the run command to call your file instead.
   Use CTRL+f to search for `app_chaupalma.py` and replace all occurrences exactly.
3. Preview this README.md to make sure it still appears correctly.
   - Find README.md in the VS Code Explorer window (top icon on the left)
   - Right-click / Preview
   - Fix any issues.
4. Run the updated command to execute **your** Python script.

### Project Task 3. Implement Your Python File

1. Read the example code carefully **before** starting.
2. Open your file. Search for "TODO" items. VS Code has icons down the left. Use either TODO Tree (tree, at the bottom) or Search (second from top).
3. Complete each TODO carefully, one at a time.
4. After implementing a TODO, paste your run command in the terminal and hit Enter to re-run it.
5. When it runs without errors, delete the associated TODO command.
6. Keep working through each TODO.
7. When you finish, there should be **zero TODO occurrences** in your project.

**Save often**: After making any useful progress, follow the steps to git add-commit-push.

---

## Notes

- You do not need to add to or modify `tests/`. They are provided for example only.
- You do not need to view or modify any of the supporting **config files**.
- Many of the repo files are silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything. Understanding builds naturally over time.
- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) with in a file.

## Troubleshooting >>> or ...

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Resources

- [Pro-Analytics-02](<[./docs/pro-tips.md](https://denisecase.github.io/pro-analytics-02/)>) - guide to professional Python
- [ANNOTATIONS.md](./ANNOTATIONS.md) - REQ/WHY/OBS annotations used
- [INSTRUCTORS.md](./docs/root/INSTRUCTORS.md) - guidance and notes for instructors and maintainers
- [POLICIES.md](./docs/root/POLICIES.md) - project rules and expectations that apply to all contributors
- [SKILLS.md](./docs/root/SKILLS.md) - skills, concepts, and professional practices (there are many)
- [SE_MANIFEST.toml](./SE_MANIFEST.toml) - project intent, scope, and role

## Citation

[CITATION.cff](./CITATION.cff) - TODO: update author and repository fields to reflect your creative work

<!--
WHY: Support correct citation and attribution.
-->

## License

[MIT](./LICENSE)

<!--
WHY: Provide terms of reuse and limits of liability.
-->
