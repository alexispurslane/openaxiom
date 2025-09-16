# 4. Core Game Loop

OpenAxiom uses two distinct types of game time to create a dynamic and
flexible gameplay experience: tactical time and scene time. These
different pacing mechanisms allow the game to shift between intense,
structured sequences and free-flowing narrative moments as needed.

The transition between tactical and scene time is a binary decision made
by the Game Master based on the needs of the narrative and the intensity
of the situation.

## 4.1. Units of Time

There are five main units of time in OpenAxiom. Here they are, in order
of granularity:

1.  **Turn**: a unit of time comprising a participant spending their
    action points on various actions before other participants get to
    act.
2.  **Round**: a unit of time comprising one iteration through each
    player (and NPC and enemy) getting their turn.
3.  **Scene**: a continuous period of gameplay that uses a single type
    of time. A new scene begins whenever the Game Master switches
    between tactical time and scene time. For example, an entire combat
    encounter run using tactical time is one scene. The period of
    free-flowing roleplaying that happens in scene time right after that
    combat is another scene.
4.  **Session**: a session of play for the day/week/month.
5.  **Campaign**: a full narrative with a beginning, middle, and end,
    composed of sessions.

## 4.2. Tactical Time

Tactical time is used during combat encounters, chases, or any situation
where precise timing and turn order are important. During tactical time,
all participants (players, NPCs, and enemies) take turns in a specific
order determined by initiative rolls.

### 4.2.1. Initiative

At the start of tactical time, all participants roll 3d6. Turns are
taken in order from lowest to highest roll. In the case of ties,
participants with the same roll go in clockwise order from the Game
Master.

Each full cycle through all participants constitutes one round of
tactical time. Participants retain their initiative order throughout the
encounter unless specific game effects modify it.

### 4.2.2. Action Points

In tactical time, each participant has a pool of action points (AP) they
can spend on various actions during their turn. Characters start each
turn with action points equal to their best Physical skill related to
dexterity or speed (default value of 9). As characters improve their
skills through story point expenditure, their action point pool
increases accordingly, allowing for more tactical options during combat.

Participants can spend their action points on any combination of actions
that they can afford. Actions have varying costs:

1.  **Minor Actions** (3 AP)
    1.  Moving up to their normal movement speed
    2.  Speaking a few words or short phrases
    3.  Interacting with a mundane object (opening a door, picking up an
        item)
    4.  Taking cover or changing position
    5.  Dropping an item or drawing a readily accessible item
2.  **Major Actions** (6 AP base cost)
    1.  Attacking an opponent with a weapon (base cost 6 AP + variable
        cost based on weapon skill requirements)
    2.  Using a skill that requires a check
    3.  Activating a special ability
    4.  Casting a spell or using advanced technology
    5.  Performing a complex task

Participants can spend any or all of their action points during their
turn. Unused action points are normally lost at the end of the turn and
do not carry over to future turns.

For example, a character with 9 action points could:

1.  Take one major action (6 AP) and one minor action (3 AP) for a total
    of 9 AP
2.  Take three minor actions (3 AP each) for a total of 9 AP
3.  Take one major action (6 AP) and have 3 AP remaining that would be
    lost

Players who wish to set triggers (see Triggers section) must
deliberately take fewer actions during their turn to maintain a reserve
of unused AP that can be used for triggered actions.

### 4.2.3. Triggers

Players can specify triggers for their actions. A trigger is an if-else
condition where if the condition is met, the player's character takes an
action before anyone else can act.

The "if" part of a trigger condition must be a specific skill check,
attack, movement, or posture change by another participant. This ensures
triggers are tied to concrete, observable game mechanics rather than
subjective interpretations.

Valid trigger conditions include:

1.  When a specific enemy makes a particular skill check (e.g., "If the
    guard makes a Perception (Visual) check")
2.  When a specific enemy makes an attack (e.g., "If the orc attacks
    me")
3.  When a specific enemy moves (e.g., "If the thief moves within 5
    meters of the chest")
4.  When a specific enemy changes posture (e.g., "If the knight stands
    up from prone")

When setting a trigger, players must reserve a pool of unused action
points (AP) from their previous turn. This reserved pool is used to
execute the triggered action when the trigger condition is met. Players
must deliberately take fewer actions during their turn to maintain this
reserve, effectively "banking" AP for potential triggers.

1.  Trigger mechanics:
    1.  Players must declare triggers and the AP pool reserved for them
        at the start of their turn
    2.  The reserved AP pool must be sufficient to cover the cost of the
        triggered action
    3.  If a trigger activates but there aren't enough reserved AP to
        cover its cost, the trigger fails
    4.  Reserved AP that isn't used by triggered actions is lost at the
        end of the round
    5.  Players can adjust their reserved AP pools and triggers at the
        start of each turn
2.  When multiple trigger actions are activated simultaneously:
    1.  They resolve in the order they were specified to the Game Master
    2.  Each triggered action consumes the appropriate action points
        from the character's reserved pool

## 4.3. Scene Time

Scene time is used for exploration, roleplaying, investigation, and
other non-combat situations. During scene time, gameplay is completely
free-flowing:

1.  Players act when they want to act
2.  There is no turn order or initiative
3.  Players can take as many actions as appropriate to the narrative
4.  The Game Master manages the flow of events and time naturally

Scene time is ideal for conversations, exploration, research, and other
activities where the structured pace of tactical time would be
unnecessarily restrictive.

## 4.4. Rests

Rests represent periods when characters take time to recover from
exertion, heal injuries, and restore their mental and physical
well-being. The Game Master decides when rests occur based on the
narrative flow and the characters' needs.

Rests can only happen during scene time. This means that characters
cannot rest during active combat encounters or other situations
requiring tactical time. The Game Master may call for a rest when:

1.  Characters have had a particularly challenging encounter or series
    of encounters
2.  The narrative naturally provides a safe space for recovery
3.  Characters express a need to recuperate from injuries or exhaustion
4.  A significant amount of time has passed in the game world

During a rest, characters may recover from harm through natural recovery
methods. A character can reduce one harm tracker by one level whenever
they get adequate long rest and recuperation, allowing their body, mind,
or social standing to heal naturally.

The Game Master determines the specific benefits of a rest based on its
duration and conditions. A brief respite might provide minor benefits,
while an extended period of rest in comfortable conditions could provide
more substantial recovery.
