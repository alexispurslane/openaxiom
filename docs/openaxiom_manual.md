# 1. OpenAxiom Manual

## 1.1. Introduction

OpenAxiom is a free and open source, universal tabletop roleplaying game
(TTRPG) engine inspired by GURPS.

OpenAxiom is called a TTRPG "engine," instead of just a TTRPG, because
it doesn't come with many of the features you'd expect from a
fully-fledged TTRPG, such as lists of predefined gear, monsters,
locations, lore, races, classes, skills, traits, and so on. Instead,
it's *just* the core mechanics, designed to be setting and genre
agnostic. Eventually, modular free and open source "packs" will provide
the various other components you need to play, which you can mix and
match as needed, although a core pack of sensible skills, traits, and
NPCs almost any setting needs is recommended.

OpenAxiom is also explicitly designed to be extremely easy to write
packs for, and easy to adapt material from other games for. This should
mean that things like GURPS sourcebooks will serve nicely with this
system! (Seriously, Steve Jackson Games rocks, give them some love.)

The system is simulationist at its core, meaning that mechanics exist to
directly represent actions and consequences in the game world. There are
no mechanics for the sake of mechanics, seemingly hastily themed after
the fact like in a European boardgame. Instead, everything in the game's
system should feel like it directly corresponds to, and simulates,
something in the game world, in a satisfying and specific way, with real
payoffs and consequences mechanically determined and mechanically
enforced, because the best stories are born from that kind of surprising
story generation that can't just be smoothed away.

OpenAxiom is also designed to ensure your stories have real,
mechanically enforced stakes. This is a game that intends to chew you up
and spit you out if you aren't careful. However, nothing is overly
random: every outcome is either preventable, something you can prepare
for, something you can recover from, or all three. Learn to roll with
the punches, embrace the Dwarf Fortress definition of fun, and you'll
have a blast.

Importantly, however, to avoid the natural baroque complexity that would
result from attempting to be both universal and simulationist, OpenAxiom
tries to focus on providing a complex and powerful engine, a *logic of
action and consequences*, instead of trying to provide rules for all
occasions. It doesn't know, or have to know, about magic or laser
blasters. All it knows is how to simulate an attempt to act, and the
results of that action in the abstract. Players assign names to the
actions and the outcomes, and compose together different tools within
the game's logic of action to construct the simulation they need, and
then the game processes them as it would any other set of actions and
outcomes, producing a result. There's still a direct, one to one
correspondence, but it's made in the space between the game and the
player, as they assign words to things.

Another difference between OpenAxiom and other TTRPGs is in how its
crunch is distributed. Many TTRPGs, even universal ones, spend a lot
more time developing combat mechanics than they do social and story
mechanics. This is understandable, because developing the former is much
easier and more well-understood. But it is also unfortunate, and
undermines the supposed universality of the system, for players that
want to focus on something other than combat. Of course, you can get
around this, as GURPS does, by providing a massive ecosystem of
extensions and optional rules, which has its own benefits, but the
drawback is that it can be very overwhelming, and also difficult to find
things. OpenAxiom seeks to provide mechanical crunch for everything,
across the board, whether it's character development, story beats,
social interactions, politics, or combat.

Despite all of the above, a primary goal for OpenAxiom is to be small,
easy to read, and easy to understand. For this reason, OpenAxiom
attempts to avoid being overly complex by eschewing complex calculations
and multidimensional tables. Everything can and should be able to be
resolved, no matter how complex the situation, by under five additions
or subtractions, and one linear table lookup. Not even any
multiplication needed! Similarly, OpenAxiom is exclusively written in a
special simple prose designed to be easy for anyone to comprehend.

We hope you enjoy!

## 1.2. Table of Contents

1.  [Character Creation](character_creation.md) and [Character
    Mechanics](character_mechanics.md)

    This section describes what player characters are in OpenAxiom and
    how to create them. Player characters are defined by skills and
    traits rather than character classes or traditional attributes. This
    approach allows for flexible and organic character development,
    enabling players to build unique individuals. The rules presented
    here guide the player through each step of character definition,
    from initial concept to fully-realized character.

2.  [Core Game Loop: The Turn System](core_game_loop.md)

    OpenAxiom uses two distinct types of game time to create a dynamic
    and flexible gameplay experience: tactical time and scene time.
    These different pacing mechanisms allow the game to shift between
    intense, structured sequences and free-flowing narrative moments as
    needed. The transition between tactical and scene time is a binary
    decision made by the Game Master based on the needs of the narrative
    and the intensity of the situation.

3.  [Logic of Action: Core Decision Resolution
    Mechanism](logic_of_action.md)

    This section describes the decision resolution mechanism for actions
    in OpenAxiom. When a character attempts an action with a meaningful
    chance of failure, the player and Game Master use the logic of
    action to determine the outcome. This system provides a consistent
    framework for resolving uncertainty while maintaining narrative
    flow. The fundamental mechanic is rolling 3d6 and comparing the
    result to a target number.

4.  [Combat: The Core Mechanics](combat.org)

    Combat situations arise naturally in many genres and settings.
    OpenAxiom recognizes that violence is sometimes necessary in
    fiction, and that in fact it is often a key aspect of why people
    enjoy TTRPGs, and so provides mechanics that make these scenes
    engaging and meaningful. The system uses an Ablative Injury System
    with specific body locations, each with their own pool of Hit
    Points, and models realistic consequences of violence with the Harm
    Tracker system.

5.  [Social Relations: Factions and Reputation](social_relations.md)

    Social interactions form a crucial part of many narratives, and
    OpenAxiom provides a structured system for tracking how characters
    relate to each other and to various factions. This system adds depth
    to roleplaying encounters and provides mechanical weight to social
    dynamics in your game. Characters belong to factions, and each
    character maintains a reputation percentage with every faction
    they've encountered, which affects social interactions and can
    change based on successful or failed social skill checks.

6.  [Game Mastering and Oracle System](game_mastering.md)

    This section serves as a guide for human Game Masters running
    OpenAxiom games, and also provides an oracle system for players who
    wish to play solo or without a human GM. It covers the role of the
    Game Master, encounter creation, NPC generation, and faction
    management.

7.  [Channeling: Extraordinary Abilities Framework](channeling.md)

    Channeling is the universal mechanism for extraordinary abilities.
    This system provides a genre-less and setting-less framework for
    powers like psionics, magic, nanotech manipulation, reality bending,
    or quickhacking. The rules for Channeling are designed to be
    abstract and flexible. This allows Game Masters to adapt them to any
    setting.

8.  [Advanced Rules](advanced.org)

    This chapter is a compendium of extra, optional rules to add on to
    the various modular subsystems of OpenAxiom, for Game Masters who
    want even more tactical choice, mechanical variety, and simulation.

## 1.3. Licensing

The OpenAxiom project uses separate licenses for the rules content and
the code:

- All prose for this TTRPG (the rules, in both org and html form, and
  introductions to those rules, etc.) are licensed under the Creative
  Commons Attribution-ShareAlike 4.0 International License. See
  [LICENSE.rules.txt](LICENSE.rules.txt) for the full license text.

- All code in this project is licensed under the Mozilla Public License
  2.0. See [LICENSE.code.txt](LICENSE.code.txt) for the full license
  text.
