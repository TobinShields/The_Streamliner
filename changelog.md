# CHANGELOG
All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

    The Streamliner - v1.1.3
    Created by: Tobin Shields
    Other contributors: Trevor Warner, Jacob Bickle

    Github: https://github.com/TobinShields/The_Streamliner

## Types of changes
    [Added] for new features.
    [Changed] for changes in existing functionality.
    [Deprecated] for soon-to-be removed features.
    [Removed] for now removed features.
    [Fixed] for any bug fixes.
    [Security] in case of vulnerabilities.

## [Unreleased] - Upcoming Changes, Current Projects, and 'wish list' items
* Since I am new to Python scripting, I am sure that I am overusing libraries, or that I was not very efficient. I would love a second pair of eyes to make this program and lightweight as possible
* A big future idea would be to somehow spider an entire site and go looking for addresses. This would be a HUGE upgrade, but is also a much larger project that the current application scope. Version 2.0?
* Are there any other file types that are good to export to? I was thinking about an easy to way to then use the exported file to import for something like a mass mailer or store in a DB.
## [1.1.4] - 2018-04-05
### Added
- Error handling for HTTP errors, such as 404 - Page Not Found errors
### Fixed
- Pages without `.html` raising a `URLError` fixed
## [1.1.3] - 2018-04-04
### Added
- Error handling. Added errors for:
  - If the url does not exist
  - If the user did not add http or https to the url
  - If the file does not exist

## [1.1.2] - 2018-04-04
### Added
- New shorter flags (-u, -f, -e) in combination with the existing ones
- Cleaned up some language around file exporting

### Changed
- Removed the need for a temp file by storing the requested URL in memory using a different library (no longer need the is import).

## [1.1.1] - 2018-04-03
### Removed
- Removed all instances of asking the user for prompts, now the program just takes the flags via the command line

## [1.1] - 2018-04-02
### Added
- Flags, use -h or --help to view
### Fixed
- Bug with `restartPrompt` after using the file option fixed
- Bug where site.tmp is not closed before removing, leading to an error fixed
## [1.0] - 2018-03-30
### Added
- Original upload
- Github page built
