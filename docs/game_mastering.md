# 9. Game Mastering

```{=org}
#+ATTR_HTML: :class section-icon
```
This chapter serves a dual purpose: it provides guidance for human Game
Masters running OpenAxiom games, and it offers an oracle system for
players who wish to play solo.

## 9.1. The Role of the Game Master

<img src="static/oracle.svg" class="section-icon" />

The Game Master (GM) in OpenAxiom has a fairly typical role. The GM's
primary responsibilities include:

1.  **Describing the World**: The GM presents the game world to the
    players, describing environments, non-player characters (NPCs), and
    events in a way that engages the players' imaginations.

2.  **Adjudicating Rules**: When questions arise about how rules apply
    to specific situations, the GM makes final decisions. These
    decisions should be consistent with the game's logic and the
    established fiction.

3.  **Controlling NPCs**: The GM plays all non-player characters,
    controlling their actions, motivations, and (in concert with the
    social rules) responses to player actions.

4.  **Managing Pacing**: The GM determines when to shift between
    tactical time and scene time, when to allow rests, and when to award
    story points, controlling the flow of the game to maintain
    engagement and dramatic tension.

5.  **Creating Challenges**: The GM designs encounters, obstacles, and
    situations that challenge the players while remaining fair and
    interesting.

6.  **Ensuring Fun**: Most importantly, the GM works to ensure that
    everyone at the table, including themselves, is having an enjoyable
    experience.

## 9.2. Using the Oracle System

For solo play or as an aid to a human GM, OpenAxiom includes an oracle
system that can make decisions in place of a human GM. This system uses
a combination of random tables and procedural generation to create
dynamic, unpredictable responses to player actions.

The oracle system is designed to preserve the core experience of playing
OpenAxiom by maintaining the same logical consistency that a skilled
human GM would provide, while introducing the element of surprise that
makes the game exciting.

### 9.2.1. Oracle Basics

When using the oracle system, players will often need to roll on various
tables to determine outcomes. These rolls should be made honestly,
without rerolling or selecting preferred results. The oracle works best
when it can surprise you.

The oracle system uses 3d6 for most rolls, just like the core game
mechanics. This maintains consistency with the rest of the system and
ensures that outcomes have the same probability distribution.

### 9.2.2. When to Consult the Oracle

Players should consult the oracle in the following situations:

1.  **World Details**: When you need information about the environment,
    NPCs, or background elements that haven't been established yet.

2.  **NPC Reactions**: When an NPC's response to player actions isn't
    obvious or predetermined.

3.  **Random Events**: When you want to introduce unexpected
    complications or opportunities.

4.  **Plot Development**: When you're unsure how to advance the story or
    what challenges to present next.

5.  **Skill Check Consequences**: When determining the specific results
    of a successful or failed skill check.

In some cases, such as with NPC reactions and skill checks in general,
OpenAxiom already provides some specific mechanical consequences and
decisions. What the Oracle is here to do is to work *with* those
systems, to help you add more imaginative flair.

### 9.2.3. Oracle Tables

The following tables can be used with the oracle system to generate
responses to common questions. For a generalized oracle that can answer
any yes/no question, see the Core Oracle Table section.

#### 9.2.3.1. Core Oracle Table

When you need to answer a yes/no question about the game world, you can
use this core oracle table. This is especially useful for solo play or
when you want to introduce uncertainty into your game.

To use this table:

1.  Determine the likelihood that what you're asking is true using these
    qualitative levels:
    - Critically Unlikely
    - Exceptionally Unlikely
    - Standard Unlikely
    - Standard Likely
    - Exceptionally Likely
    - Critically Likely
2.  Roll 3d6 and consult the table below, cross-referencing your
    likelihood assessment:

| 3d6 Roll | Critically Unlikely | Exceptionally Unlikely | Standard Unlikely | Standard Likely | Exceptionally Likely | Critically Likely |
|----|----|----|----|----|----|----|
| 3 | No, but… | Yes, but… | Yes | Yes, and… | Yes, and… | Yes, and… |
| 4 | No, but… | Yes, but… | Yes | Yes, and… | Yes, and… | Yes, and… |
| 5 | No | No, but… | Yes, but… | Yes | Yes, and… | Yes, and… |
| 6 | No | No, but… | Yes, but… | Yes | Yes, and… | Yes, and… |
| 7 | No | No | No, but… | Yes | Yes | Yes, and… |
| 8 | No | No | No, but… | Yes | Yes | Yes, and… |
| 9 | No | No | No, but… | Yes | Yes | Yes |
| 10 | No | No | No | Yes | Yes | Yes |
| 11 | No | No | No | Yes | Yes | Yes |
| 12 | No | No | No | Yes, but… | Yes | Yes |
| 13 | No, and… | No | No | Yes, but… | Yes | Yes |
| 14 | No, and… | No | No | Yes, but… | Yes | Yes |
| 15 | No, and… | No, and… | No | No, but… | Yes, but… | Yes |
| 16 | No, and… | No, and… | No | No, but… | Yes, but… | Yes |
| 17 | No, and… | No, and… | No, and… | No | No, but… | Yes, but… |
| 18 | No, and… | No, and… | No, and… | No | No, but… | Yes, but… |

##### 9.2.3.1.1. Using the Core Oracle Table

The results are interpreted as follows:

- **Yes**: The answer to your question is yes.
- **No**: The answer to your question is no.
- **Yes, but…**: The answer is yes, but with a complicating factor.
- **No, but…**: The answer is no, but with a silver lining.
- **Yes, and…**: The answer is yes, and something additional beneficial
  happens.
- **No, and…**: The answer is no, and something additional detrimental
  happens.

#### 9.2.3.2. NPC Reactions

When you need to determine how an NPC reacts to the players, consult
this 2D table that cross-references the result of the social skill check
with the 3d6 roll:

| 3d6 Roll | Critical Success | Exceptional Success | Standard Success | Marginal Failure | Exceptional Failure | Critical Failure |
|----|----|----|----|----|----|----|
| 3 | Enthusiastic | Enthusiastic | Enthusiastic | Enthusiastic | Helpful | Cold |
| 4-5 | Enthusiastic | Enthusiastic | Helpful | Helpful | Helpful | Unfriendly |
| 6-8 | Enthusiastic | Helpful | Helpful | Helpful | Neutral | Unfriendly |
| 9-12 | Helpful | Helpful | Neutral | Cool | Cool | Unfriendly |
| 13-15 | Helpful | Cool | Cool | Cold | Unfriendly | Unfriendly |
| 16-17 | Cool | Cool | Cold | Unfriendly | Hostile | Hostile |
| 18 | Neutral | Cold | Unfriendly | Hostile | Hostile | Hostile |

The degree of success is determined by consulting the Degrees of Success
and Failure table in the Logic of Action chapter:

| Degree of Success/Failure | Roll Result                         |
|---------------------------|-------------------------------------|
| Critical Success          | 3 or 4                              |
| Exceptional Success       | 5 or more below target number       |
| Standard Success          | Equal to target or 1-4 below target |
| Marginal Failure          | 1-4 above target number             |
| Exceptional Failure       | 5 or more above target number       |
| Critical Failure          | 17 or 18                            |

NPC Reaction Descriptions:

- **Hostile**: The NPC is actively opposed to the players and may attack
  or sabotage their efforts
- **Unfriendly**: The NPC is suspicious, uncooperative, or actively
  working against the players' interests
- **Cold**: The NPC is distant and unhelpful, barely tolerating the
  players' presence
- **Neutral**: The NPC is indifferent to the players, neither helping
  nor hindering them
- **Cool**: The NPC is somewhat helpful but reserved, offering minimal
  assistance
- **Helpful**: The NPC is actively supportive of the players' goals and
  may provide significant aid
- **Enthusiastic**: The NPC is extremely helpful and may become a
  valuable ally or follower

#### 9.2.3.3. Random Events

When you want to introduce a random event, follow this three-step
process:

1.  **Determine the Event Type**: Roll 3d6 and consult the Event Types
    table below.
2.  **Determine the Circumstance Type**: Roll 3d6 and consult the
    Circumstance Types table below.
3.  **Determine the Affected Party**: Roll 3d6 and consult the Affected
    Parties table below.

Combine the results to create a specific event. For example, if you roll
"Crisis" for event type, "Social" for circumstance type, and "Player
Characters" for affected party, you might have a crisis involving a key
relationship or alliance that affects the player characters. If the
affected party is a faction, consider how the event affects that
faction's relationships, resources, or position.

##### 9.2.3.3.1. Event Types

| Roll | Event Type | Description |
|----|----|----|
| 3 | Crisis | A sudden emergency that requires immediate attention |
| 4-5 | Obstacle | A new challenge or barrier that complicates the players' plans |
| 6-8 | Discovery | The players find something useful, interesting, or valuable |
| 9-12 | Opportunity | A chance to advance goals or gain an advantage |
| 13-15 | Encounter | Meeting with an NPC or creature that may be friend or foe |
| 16-18 | Boon | A significant benefit or advantage that improves the situation |

##### 9.2.3.3.2. Circumstance Types

| Roll | Circumstance Type | Description |
|----|----|----|
| 3-6 | Physical | Events affecting the material world, bodies, or physical objects |
| 7-12 | Social | Events affecting relationships, alliances, or social structures |
| 13-18 | Mental | Events affecting thoughts, emotions, or psychological state |

##### 9.2.3.3.3. Affected Parties

| Roll | Affected Party | Description |
|----|----|----|
| 3-5 | Player Factions | Factions that the player characters belong to or are highly regarded by |
| 6-8 | Friendly NPC Factions | Factions of the friendly NPCs that are affected by the event |
| 9-12 | Player Characters | The player characters themselves are directly affected by the event |
| 13-15 | Friendly NPCs | Friendly NPCs are directly affected by the event |
| 16-18 | Neutral NPCs | Neutral or unaligned NPCs are directly affected by the event |

#### 9.2.3.4. Plot Development

When determining how to advance the story, follow this three-step
process:

1.  **Determine the Development Type**: Roll 3d6 and consult the
    Development Types table below.
2.  **Determine the Circumstance Type**: Roll 3d6 and consult the
    Circumstance Types table (from the Random Events section above).
3.  **Determine the Affected Party**: Roll 3d6 and consult the Affected
    Parties table (from the Random Events section above).

Combine the results to create a specific plot development. For example,
if you roll "Revelation" for development type, "Social" for circumstance
type, and "Player Characters" for affected party, you might have a
revelation about a key relationship or alliance that directly affects
the player characters.

##### 9.2.3.4.1. Development Types

| Roll | Development | Description |
|----|----|----|
| 3 | Setback | A major complication that significantly hinders progress |
| 4-5 | Complication | A new factor that makes the situation more complex |
| 6-8 | Progress | The players make meaningful advancement toward their goals |
| 9-12 | Revelation | Important information is discovered that changes understanding |
| 13-15 | Twist | An unexpected turn of events that changes the direction of the story |
| 16-18 | Breakthrough | A major success that significantly advances the players' position |

## 9.3. Creating Encounters

Whether you're a human GM or using the oracle system, creating engaging
encounters is crucial to a successful OpenAxiom game. Encounters should
challenge the players without being impossible, and should offer
meaningful choices in how to approach them.

### 9.3.1. Encounter Design Principles

When designing encounters, keep these principles in mind:

1.  **Multiple Solutions**: Good encounters can be resolved in several
    different ways, allowing players to use their unique skills and
    creativity.

2.  **Meaningful Consequences**: Player choices should have real impact
    on the outcome and future events.

3.  **Appropriate Challenge**: Encounters should be challenging but not
    overwhelming for the player characters' capabilities.

4.  **Narrative Integration**: Encounters should feel like a natural
    part of the story and world, not artificially inserted obstacles.

### 9.3.2. Using the Oracle for Encounter Creation

The oracle system can help generate encounter elements when you're not
sure what to include:

#### 9.3.2.1. Encounter Type

Roll 3d6 to determine the primary type of encounter:

| Roll | Type | Description |
|----|----|----|
| 3-5 | Combat | A physical confrontation with enemies or dangerous creatures |
| 6-8 | Social | An interaction with NPCs that requires negotiation, deception, or persuasion |
| 9-12 | Exploration | Investigating a location, solving puzzles, or navigating hazards |
| 13-15 | Mystery | Gathering information, solving crimes, or uncovering secrets |
| 16-18 | Chase | A pursuit or evasion scenario requiring quick thinking and movement |

#### 9.3.2.2. Enemy Strength

When determining how powerful enemies should be, roll 3d6:

| Roll | Strength | Description |
|----|----|----|
| 3-5 | Weak | Enemies are significantly below the players' capabilities |
| 6-8 | Matched | Enemies are roughly equal to the players' capabilities |
| 9-12 | Strong | Enemies are somewhat more powerful than the players |
| 13-15 | Formidable | Enemies are significantly more powerful than the players |
| 16-18 | Overwhelming | Enemies are far beyond what the players can handle |

## 9.4. Creating NPCs

Creating compelling NPCs is essential for both human GMs and players
using the oracle system. NPCs should feel like real people with their
own motivations, goals, and personalities.

### 9.4.1. NPC Templates

When creating NPCs, you can use these templates as starting points:

1.  **Role**: What function does this NPC serve in the world?
2.  **Motivation**: What drives this NPC to act?
3.  **Personality Trait**: What defining characteristic shapes this
    NPC's behavior?
4.  **Power and Influence**: How much sway does this NPC have in their
    environment?

#### 9.4.1.1. Role

Roll 3d6 to determine an NPC's primary role:

| Roll | Role | Description |
|----|----|----|
| 3 | Criminal | An outlaw, thief, or other lawbreaker |
| 4-5 | Merchant | A trader, shopkeeper, or businessperson |
| 6-8 | Official | A government representative, bureaucrat, or authority figure |
| 9-12 | Expert | A skilled professional or knowledgeable individual |
| 13-15 | Laborer | A worker, craftsman, or service provider |
| 16-18 | Leader | A person of influence, authority, or command |

#### 9.4.1.2. Motivation

Roll 3d6 to determine what primarily drives an NPC:

| Roll  | Motivation  | Description                                     |
|-------|-------------|-------------------------------------------------|
| 3     | Revenge     | Seeking payback for a real or perceived wrong   |
| 4-5   | Power       | Desiring control, influence, or authority       |
| 6-8   | Security    | Wanting safety, stability, or protection        |
| 9-12  | Recognition | Seeking respect, fame, or validation            |
| 13-15 | Wealth      | Pursuing money, resources, or material gain     |
| 16-18 | Ideals      | Following a moral code, belief system, or cause |

#### 9.4.1.3. Personality Trait

Roll 3d6 to determine a key personality trait:

| Roll  | Trait         | Description                                      |
|-------|---------------|--------------------------------------------------|
| 3     | Paranoid      | Suspicious and distrustful of others             |
| 4-5   | Greedy        | Always looking for personal gain                 |
| 6-8   | Loyal         | Faithful to friends, family, or organizations    |
| 9-12  | Honest        | Direct and truthful in dealings with others      |
| 13-15 | Compassionate | Showing empathy and concern for others           |
| 16-18 | Ruthless      | Willing to do whatever it takes to achieve goals |

#### 9.4.1.4. Power and Influence

Roll 3d6 to determine an NPC's power and influence level:

| Roll | Level | Description |
|----|----|----|
| 3 | Powerless | Has no real influence or authority |
| 4-5 | Marginal | Has very limited influence in a small circle |
| 6-8 | Minor | Has some influence in a local area or small organization |
| 9-12 | Moderate | Has notable influence in a region or medium-sized organization |
| 13-15 | Significant | Has substantial influence in a large area or major organization |
| 16-18 | Pervasive | Has overwhelming influence across vast areas or multiple organizations |

When creating NPCs, consider how their power and influence level affects
their ability to affect the story, resources they can access, and how
other NPCs and factions respond to them. A powerful NPC might be able to
call upon significant resources or have far-reaching effects on the
campaign, while a powerless NPC might be easily dismissed or ignored by
other characters.
