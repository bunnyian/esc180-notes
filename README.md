# esc180-notes
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://bunnyian.github.io/esc180-notes/)

Link to site = [https://bunnyian.github.io/esc180-notes/](https://bunnyian.github.io/esc180-notes/)

## Prequisites
- [Jupyter Book](https://jupyterbook.org/en/stable/start/overview.html)

```bash
pip install -U jupyter-book
```
Strongly recommended to be able to preview changes locally before pushing to GitHub, but technically not required.

## Making Changes
Any changes to the source files that are pushed to the main branch will automatically be updated on the website via GitHub actions (see `.github/workflows/). (this can take 3-5 mins depend on how many changes are made)

### Reordering Pages
Reorder the lines in notebook>_toc.yml. More instructions at the top of the file.

### Adding Pages
Add content to the folder `notebook`, then add page to `_toc.yml`. **IMPORTANT: the page will not show if there are no headings in the page.**

### Editing Pages
Edit ipynb directly and changes will be reflected when rebuilding the book.

Useful cheatsheet for formatting etc. [MyST syntax cheatsheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html)

## Previewing and Pushing Changes
Open the root directory `esc180-notes` in terminal and run:
```bash
jupyter-book build .
```

Depending on what kind of changes are made, it may be recommended to clear old files beforehand (this will rebuild from scratch).
```bash
jupyter-book clean .
```

When changes are pushed to GitHub, the [deploy.yml](.github/workflows/deploy.yml) file will perform the same compilation, as well as push the changes to the `gh-pages` branch, which is what the website is built from.

You can monitor the progress on the [Actions](https://github.com/bunnyian/esc180-notes/actions) tab of the repo.
