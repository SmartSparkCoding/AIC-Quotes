# An Inspector Calls Quotes API

## What

Well, its an API! You use `/quote` to get a random quote! There is also a basic website, with a custom font. There is a total of 18 quotes that the API can choose from!

## Why?

Well, its a joke. While being on lots of `#hippogriff-tinkering` huddles, I noticed that it was a running joke about An Inspector Calls, a text we do for GCSE in the UK!

And so, here we are!!

## Info

The info on how the API works is all in the docs part of the site! There are 18 quotes total, and the API is served (alongside the webiste) using Flask for Python.

There are also filter parameters for each of the characters and three acts. You cannot use more than one filter at the time.

I might add multi-filters, more quotes etc in the future!

## Examples

Here are some examples of the API to use! 

`https://aic.navaratne.uk/quote?filter=act&act=3`
`https://aic.navaratne.uk/quote?filter=act&act=1`
`https://aic.navaratne.uk/quote?filter=character&character=arthur`
`https://aic.navaratne.uk/quote?filter=character&character=sybil`

The following will test various features and fallbacks of the API: 

`https://aic.navaratne.uk/quote?filter=quote` - this should error
`https://aic.navaratne.uk/quote` - this should give a quote from any act or any character

## Local Development

1. Open your terminal.
2. Run the command `git clone https://github.com/smartsparkcoding/aic-quotes/`
3. Run the command `cd ~/aic-quotes`
4. On Mac or Linux, run `python3 -m venv .venv`. On Windows, run `python -m venv .venv` (make sure python is already installed)
5. On Mac or Linux, run `source .venv/bin/activate`. On Windows, run `.venv\Scripts\activate`
6. On Mac or Linux, run `python3 -m pip install Flask`. On Windows, run `python -m pip install Flask`
7. On Mac or Linux, run `python3 app.py`. On Windows, run `python app.py` 
8. The site is live, locally! Open in your browser: `localhost:1234/` and the site will appear (with the API running too :) )
