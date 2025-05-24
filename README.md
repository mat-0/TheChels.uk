# Site

A blog hosted on GitHub is available at TheChels.uk. The site uses Jekyll, a static site generator, on Ruby. DNS and SSL by Cloudflare. It also uses GitHub actions, GitHub issues, and Python for extensive automation.

It is called "weak notes" as a play on words of the popular "week notes" [blogging style](https://weeknot.es/) -
due to the likelihood, I will have an inconsistent and irregular cadence for posting.

## Badges

<details><summary><code>Quality Control</code></summary>

  [![Run tests](https://github.com/Mat-0/TheChels.uk/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/python-ci.yml)
  [![CodeQL](https://github.com/mat-0/TheChels.uk/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/mat-0/TheChels.uk/actions/workflows/codeql-analysis.yml)
  [![Lighthouse](https://github.com/Mat-0/TheChels.uk/actions/workflows/lighthouse.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/lighthouse.yml)
  [![Link Checker](https://github.com/Mat-0/TheChels.uk/actions/workflows/link-checker.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/link-checker.yml)
  [![Linter](https://github.com/Mat-0/TheChels.uk/actions/workflows/linter.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/linter.yml)
  [![Clear Cache](https://github.com/Mat-0/TheChels.uk/actions/workflows/clear-cache.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/clear-cache.yml)
  [![Pages](https://github.com/Mat-0/TheChels.uk/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/pages/pages-build-deployment)
</details>

<details><summary><code>Content Management</code></summary>

  [![Add Book](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-book.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-book.yml)
  [![Add Film](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-film.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-film.yml)
  [![Add Offers](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-offers.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-offers.yml)
  [![Add Post](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-post.yml/badge.svg?event=issues)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-post.yml)
  [![Add Podcast](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-podcast.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-podcast.yml)
  [![Add Quotes](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-quotes.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-quotes.yml)
  [![Add Stock](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-stock.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-stock.yml)
</details>

## Configuration

There are several optional settings for you to configure. Use the example `_config.yml` file in the repo and use the documentation below to configure your site:

<details><summary><code>Config</code></summary>

### Using includes

  There are 2 main includes: one for the header and one for the footer, largely to minimise repetition.

### Using layouts

  Layouts are almost one-to-one with pages, handling any page specifics. `post.html` is the layout used for every blog post. There are also default templates and an empty template used for `scss` and other special pages such as `humans.txt`

### Using Data

  Data files power many aspects of the site and these are updated via issues and GitHub Actions.

### Site navigation

  Using configuration yml, navigation is provided by three collections for `header`, `footer`, and `around_the_web` (on the about page) and are fairly self-explanatory.
</details>

## Post Types

<details><summary><code>Postings</code></summary>

### Mixtape Monthly Guide

- Monthly, create a mixtape running the shortcut
- Open the produced and resize to 832px width
- Copy the image to the`image/mixtapes/` folder ensuring the name matches the format `yyyy-MM.png`
- Push a commit to Prod

### Add a Film

- Run the python script typing in a Film title and a Rating. Or;
- Run a workflow dispatch - entering the inputs Film and Rating

### Add a Book

- Run a workflow dispatch - entering the ISBN
- Download the cover image
- Resize to a height of 183px
- Save the cover image into the `images/books` folder ensuring the name matches the format `book-[isbn].png`
- Push a commit to Prod

### Quote posts

- Capture the selection on a page in safari
- Share to Drafts and click Save
- In Drafts run the `cite to blog` if it's a quotable post. Or;
- In Drafts run the `post to blog` if it's a regular post

</details>

### How to Run the Site Locally

<details><summary><code>Local Development</code></summary>

- Clone the repository:

   ```bash
   git clone https://github.com/Mat-0/TheChels.uk.git
   ```

- Navigate into the project directory:

   ```bash
   cd TheChels.uk
   ```

- Install the required dependencies:

   ```bash
   bundle install
   ```

- Build and serve the site locally:

   ```bash
   bundle exec jekyll serve --watch
   ```

- Open your browser and go to `http://localhost:4000` to see your site.

  <http://localhost:4000>

</details>
