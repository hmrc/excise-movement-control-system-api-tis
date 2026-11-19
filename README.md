# Excise Movement Control System  - Technical Interface Specification

In the period before a new version of EMCS is released, third-party developers
need to be able to reference both the current version and the upcoming version
at the same time. Because of this we have documentation repos with the version
included in the repo name as a suffix (eg
`excise-movement-control-system-api-tis-4-2`). This repo (which doesn't have a
version number in its name) exists so we can provide stable links to pages in
the documentation which don't need to be updated every time a new version is
released. It also means we don't break links that end users have already
bookmarked. The logic for this redirection behaviour is in [config.rb](config.rb)

## Getting started

To preview or build the website, we need to use the terminal.

Install Ruby 2.7.x with Rubygems, preferably with a [Ruby version manager][rvm],
and the [Bundler gem][bundler].

In the application folder type the following to install the required gems:

```
bundle install
```

## Preview

Whilst writing documentation we can run a middleman server to preview how the
published version will look in the browser. After saving a change the preview in
the browser will automatically refresh.

The preview is only available on our own computer. Others won't be able to
access it if they are given the link.

Type the following to start the server:

```
bundle exec middleman server
```

If all goes well something like the following output will be displayed:

```
== The Middleman is loading
== LiveReload accepting connections from ws://192.168.0.8:35729
== View your site at "http://Laptop.local:4567", "http://192.168.0.8:4567"
== Inspect your site configuration at "http://Laptop.local:4567/__middleman", "http://192.168.0.8:4567/__middleman"
```

You should now be able to view a live preview at http://localhost:4567.

## Build

If you want to publish the website without using a build script you may need to
build the static HTML files.

Type the following to build the HTML:

```
bundle exec middleman build
```

This will create a `build` subfolder in the application folder which contains
the HTML and asset files ready to be published.

[rvm]: https://www.ruby-lang.org/en/documentation/installation/#managers
[bundler]: http://bundler.io/

### License

This code is open source software licensed under the [Apache 2.0 License]("http://www.apache.org/licenses/LICENSE-2.0.html").
