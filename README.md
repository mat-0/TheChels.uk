# Site

A blog hosted on GitHub available at TheChels.uk. The site uses Jekyll, a static site generator, on Ruby. DNS and SSL by Cloudflare. It also uses GitHub actions, GitHub issues, and Python for extensive automation.

It is called "weak notes" as play on words of the popular "week notes" [blogging style](https://weeknot.es/) - 
due to the likelihood I will be inconsistent and non-regular.

## Badges

<details><summary><code>Quality Control</code></summary>

  [![Run tests](https://github.com/Mat-0/TheChels.uk/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/python-ci.yml)
  [![CodeQL](https://github.com/Mat-0/TheChels.uk/actions/workflows/codeql.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/codeql.yml) 
  [![Lighthouse](https://github.com/Mat-0/TheChels.uk/actions/workflows/lighthouse.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/lighthouse.yml) 
  [![Link Checker](https://github.com/Mat-0/TheChels.uk/actions/workflows/link-checker.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/link-checker.yml) 
  [![Linter](https://github.com/Mat-0/TheChels.uk/actions/workflows/linter.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/linter.yml) 
  [![Clear Cache](https://github.com/Mat-0/TheChels.uk/actions/workflows/clear-cache.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/clear-cache.yml) 
  [![Pages](https://github.com/Mat-0/TheChels.uk/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/pages/pages-build-deployment) 
</details>


<details><summary><code>Content Management</code></summary>
  
  [![Add Book](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-book.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-book.yml) 
  [![Add Now and Next](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-next.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-next.yml) 
  [![Add Offers](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-offers.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-offers.yml) 
  [![Add Post](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-post.yml/badge.svg?event=issues)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-post.yml) 
  [![Add Podcast](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-podcast.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-podcast.yml) 
  [![Add Quotes](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-quotes.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-quotes.yml) 
  [![Add Stock](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-stock.yml/badge.svg)](https://github.com/Mat-0/TheChels.uk/actions/workflows/add-stock.yml) 
</details>

## Morning

In order for the page to work you need to enter some secrets for the repository. There are also a bunch of config files (json) that need updating to suit your needs.

1. An open weather API key - you can register for a free account on their website.
2. Latitude and Longitude for the weather API.
3. Update stocks.json with the ticker ids for the stocks you want prices for.
4. Update comps.json with the list of competition slugs used by the BBC in order to get the relevant football fixtures 
5. Update quotes.json with your favourite quotes.


## Configuration
There are a number of optional settings for you to configure. Use the example `_config.yml` file in the repo and use the documentation below to configure your site:

<details><summary><code>Config</code></summary>
  
  ### Using includes
  There are 2 main includes: one for the header and one for the footer, largely to minimise repetititon.
  
  ### Using layouts
  
  Layouts exist on an almost one-to-one relationship with pages, handling any page specifics, `post.html` is the layout used for every blog post. There also default templates and an empty template used for `scss` and other special pages such as `humans.txt`
  
  ### Using Data
  
  Many aspects of the site are powered by data files and these are updating via issues and GitHub Actions, including most of the content on the `Morning` page.
  
  ### Site navigation
  
  Using configuration yml, navigation is provided by three collections for `header`, `footer`, and `around_the_web` (on the about page) and are fairly self-explanatory.
</details>
