# OpenAxiom TTRPG

OpenAxiom is a free and open source tabletop roleplaying game (TTRPG) engine inspired by GURPS. OpenAxiom has a few features:

## A Universal Engine

OpenAxiom is called a TTRPG "engine," instead of just a TTRPG, because it doesn't come with many of the features you'd expect from a fully-fledged TTRPG, such as lists of predefined gear, monsters, locations, lore, races, classes, skills, traits, and so on. Instead, it's /just/ the core mechanics, designed to be setting and genre agnostic.

Eventually, modular free and open source "packs" will provide the various other components you need to play, which you can mix and match as needed, although a core pack of sensible skills, traits, and NPCs almost any setting needs is recommended.

OpenAxiom is also explicitly designed to be extremely easy to write packs for, and easy to adapt material from other games for. This should mean that things like GURPS sourcebooks will serve nicely with this system! (Seriously, Steve Jackson Games rocks, give them some love.)

## Simulationist

OpenAxiom also attempts to be simulationist: there are no mechanics for the sake of mechanics, seemingly hastily themed after the fact like in a European boardgame. Instead, everything in the game's system should feel like it directly corresponds to, and simulates, something in the game world, in a satisfying and specific way, with real payoffs and consequences mechanically determined and mechanically enforced, because the best stories are born from that kind of surprising story generation that can't just be smoothed away.

Importantly, however, to avoid overly baroque complexity while trying to be genreless, OpenAxiom provides an engine for a /logic of action and consequences/, of /means and ends/, and that's it. It doesn't know, or have to know, about magic or laser blasters. All it knows is how to simulate an attempt to act, and the results of that action in the abstract. Players assign names to the actions and the outcomes, and the game processes them as it would any other set of actions and outcomes, producing a result. There's still a direct, one to one correspondence, but it's made in the space between the game and the player, as they assign words to things. It's like a logic programming language: it doesn't know what the words actually mean, but it can still simulate things anyway.

## Crunchy Across the Board

A lot of TTRPGs, even universal ones, spend a lot more time developing combat mechanics than they do social and story mechanics. This is understandable, because developing the former is much easier and more well-understood, but also unfortunate, and undermines the supposed universality of the system. OpenAxiom seeks to provide mechanical crunch for everything, across the board, whether it's character development, story beats, social interactions, politics, or combat.

This means that OpenAxiom respects your story, characters, and their social interactions just as much as their combat prowess. This is not just a game for wargamers and murder hobos, it is also a game for those who want to explore the politics of taking state power through long political intrigue, or toppling a rogue nation, or resolving a harem situation.

## Harsh but Fair

Stories only matter when they have stakes. OpenAxiom is designed to ensure you have those stakes. This is a game that will rough you up, that intends to chew you up and spit you out if you aren't careful. However, nothing is overly random: every risk is a choice, every outcome preventable or something you can prepare for, and every bad outcome this side of death is recoverable, even if the road is long and hard. Learn to roll with the punches, embrace the Dwarf Fortress definition of fun, and grin and laugh in the face of death.

## Easy to Understand

Despite its depth, a primary goal for OpenAxiom is to be small, easy to read, and easy to understand.

For this reason, OpenAxiom attempts to avoid being overly complex by eschewing complex calculations and multidimensional tables. Everything can and should be able to be resolved, no matter how complex the situation, by under five additions or subtractions, and one linear table lookup. Not even any multiplication needed!

Similarly, OpenAxiom is exclusively written in a special simple prose designed to be easy for anyone to comprehend --- to never trip you up with an unexpected subclause.

## Licensing

The OpenAxiom project uses separate licenses for the rules content and the code:

- All prose for this TTRPG (the rules, in both org and html form, and introductions to those rules, etc.) are licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See [LICENSE.rules.txt](LICENSE.rules.txt) for the full license text.

- All code in this project is licensed under the Mozilla Public License 2.0. See [LICENSE.code.txt](LICENSE.code.txt) for the full license text.

## Social Relations System

This repository includes a new chapter on Social Relations, which adds depth to roleplaying encounters and provides mechanical weight to social dynamics in your game. The system features:

- **Factions**: Every character belongs to a faction representing their affiliations, organizations, or cultural groups
- **Reputation Tracking**: Characters maintain reputation percentages with factions they've encountered, affecting social interactions
- **Reputation Changes**: Reputation shifts based on the outcomes of social skill checks, with different modifiers for exceptional/critical successes and failures
- **Mechanical Effects**: Reputation provides bonuses or penalties to social skill checks and can influence NPC behavior

The Social Relations system is fully integrated with the existing OpenAxiom mechanics and follows the same design principles of being simulationist, crunchy across the board, and easy to understand.

## Manual Server

This repository also includes a Flask-based server for serving the OpenAxiom TTRPG manual with live reloading capabilities.

### Features

- Serves HTML files generated from Org-mode documents
- Live reloading when Org files or CSS are modified
- Automatic generation of HTML files from Org files using Pandoc
- File listing and navigation interface
- Full-text search functionality

### Requirements

- Python 3.8+
- Pandoc
- UV (for dependency management)

### Installation

1. Install the required dependencies using UV:
   ```
   uv pip install flask flask-socketio watchdog pandoc whoosh
   ```

   Or if you prefer to use the pyproject.toml file:
   ```
   uv pip install .
   ```

### Usage

Run the server using UV:
```
uv run app/server.py
```

The server will:
1. Generate HTML files from all Org files in the current directory
2. Start a web server on http://localhost:8000
3. Automatically open the default browser
4. Watch for changes to Org files and CSS, rebuilding and reloading as needed

### Directory Structure

- `app/templates/` - Flask templates
- `app/static/` - Static files (CSS, JS, images)
- `app/html/` - Generated HTML files (created automatically)
- `*.org` - Source Org files in the root directory

### How It Works

1. When the server starts, it processes all Org files in the root directory using Pandoc to generate HTML files in `app/html/`
2. The main page (`/`) shows a file listing and embeds the selected HTML file in an iframe
3. File watcher monitors for changes to Org files and CSS
4. When an Org file is modified, it's reprocessed with Pandoc
5. When CSS is modified, the page is reloaded
6. WebSocket connection provides live reloading in the browser
7. Whoosh search index is automatically updated when Org files change

### Customization

You can modify the following variables in `app/server.py`:
- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: localhost)