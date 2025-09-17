# 10. Appendix I - Advanced Rules

This chapter is a compendium of extra, optional rules to add on to the
various modular subsystems of OpenAxiom, for Game Masters who want even
more tactical choice, mechanical variety, and simulation.

## 10.1. Advanced Combat Rules

The following are an optional toolkit of combat rules that GMs can
assemble in order to account for various different situations or
preferred combat playstyles, or use as references for designing their
own optional combat mechanics for their own setting packs.

### 10.1.1. Spatial Relations

<img src="static/spatial_relations.svg" class="section-icon" />

More advanced players who want more interesting tactical opportunities
may introduce a hexagonal grid when players enter combat to structure
character, NPC, and enemy spatial relations. This optional system adds
tactical depth by making positioning and movement important factors in
combat. This set of rules is an example of how totally new dimensions of
combat can be modularly added to the game and well-integrated with
existing systems.

#### 10.1.1.1. Setting Up the Battlefield

In hex-based tactical combat, the battlefield is divided into hexagonal
tiles, with each tile representing a specific type of terrain. Players,
NPCs, and enemies are represented by counters or miniatures that are
placed on these hex tiles. Each hex tile has a terrain type that affects
movement costs and combat, as detailed in the terrain table below.

All players must start wherever the Game Master decides they should
start on the grid. The Game Master also places all non-player characters
and enemies on the grid according to the tactical situation. Each hex on
the map can be one of several terrain types, each with different
properties:

| Terrain Type | Movement Cost | Combat Effects | Description |
|----|----|----|----|
| Floor | Normal | None | Standard terrain with no special properties |
| Wall | Impassable | Blocks movement and line of sight | Solid barriers that cannot be moved through |
| Difficult Terrain | +1 to +3 movement | As determined by the Game Master | Environmental features like trees, bushes, water, etc. |
| High Ground | Normal | +1 to +3 bonus to ranged combat skills | Elevated positions that grant tactical advantages |
| Cover | Normal | -1 penalty to ranged attacks through it | Provides partial protection without blocking movement or line of sight |
| Unstable Terrain | Normal | Requires Physical (Acrobatics) check to avoid falling prone | Surfaces that are slippery, loose, or otherwise unstable. The Physical (Acrobatics) check must be made whenever a character moves into a hex of this type. |
| Damaging Terrain | Normal | Causes fixed HP damage to both legs | Surfaces that cause damage. Fixed HP damage is applied to both legs whenever a character moves into a hex of this type. |

Note that posture and cover penalties stack. For example, a character
laying down (-2 penalty) behind cover (-1 penalty) would have a total -3
penalty to ranged attacks targeting them.

Specific examples of all types of terrain (both special and not) are
determined automatically by the setting and location, but all
conceivable types of gameplay-relevant terrain should fall into one of
these categories.

#### 10.1.1.2. Posture System

Characters can adopt different postures during combat to gain defensive
advantages at the cost of mobility. The posture system provides tactical
options for players who want to trade movement for protection:

| Posture | Movement Restriction | Ranged Combat Defense Bonus | Description |
|----|----|----|----|
| Standing | Normal movement | None | Standard posture with no restrictions or bonuses |
| Crouching | Only one hex per turn | -1 modifier to hit | Lower profile provides minor protection against ranged attacks |
| Laying Down | Cannot move | -2 modifier to hit | Maximum protection against ranged attacks at the cost of mobility |

Characters can change their posture as a minor action on their turn.
This allows them to adapt their tactics based on the current situation,
such as taking cover when under heavy ranged fire or standing up to move
more freely.

#### 10.1.1.3. Movement

Moving is considered a minor action that costs 3 action points. Players
may move up to their best fleetness/quickness related **Physical** skill
(such as **Physical (Running)** or **Physical (Acrobatics)**) minus 5
(minimum of 1) as their movement distance. Since moving is a minor
action, players with sufficient action points could potentially move
multiple times during their turn, or move and still take a major action.
Moving through difficult terrain costs additional movement points as
determined by the terrain table above.

#### 10.1.1.4. Line of Sight

Players who use ranged weapons must have a **line of sight** to the
opponents they wish to attack. Only walls block movement and line of
sight. Trees, bushes, and other environmental features count as walls in
outdoor settings for the purpose of blocking line of sight. Characters
can see and attack through other characters, but must make their combat
skill check at a -2 disadvantage per character they're attacking
through.

#### 10.1.1.5. Range

Any ranged item designed to be used with the spatial relations rules
should come with a specified range. Players only need line of sight and
a successful skill check to hit something within the range of their
ranged weapon. **For targets beyond the weapon's range, players get a -1
penalty to their skill check for every hex beyond their range they
aim.**

#### 10.1.1.6. Flanking

When attacking an enemy in melee combat, positioning can provide
significant tactical advantages. If one or more of a character's allies
are adjacent to an enemy that the character is attacking, this is
considered **flanking**.

Flanking provides the following benefits:

- The attacking character receives a +1 bonus to all attack skill checks
  against the flanked enemy
- The flanked enemy receives a -1 penalty to all of their attack skill
  checks

Flanking represents the tactical advantage of having multiple attackers
positioned around an enemy, making it difficult for the target to defend
against attacks from multiple directions simultaneously. This bonus
applies to all melee attacks, and the penalty applies to all attacks
made by the flanked character until the flanking conditions change
(either the allies move away or the target moves).

#### 10.1.1.7. Zone of Control

Each character exerts control over the area immediately surrounding
them. The six hexes adjacent to any character constitute their **zone of
control**. This represents the area that a character can effectively
threaten with their presence and weapons.

When an opponent enters a character's zone of control, that opponent is
considered **engaged** with the character. If the opponent attempts to
leave the zone of control without first knocking the controlling
character unconscious or killing them, the controlling character may
make a free attack against the fleeing opponent as they attempt to
escape.

This free attack:

- Is made immediately when the opponent attempts to leave the zone of
  control
- Does not consume the controlling character's major or minor action
- Must be declared before the opponent's movement is resolved
- Uses the controlling character's relevant combat skill
- Is resolved as a normal attack sequence (declare, roll, determine,
  damage, armor, apply)

This rule represents how difficult it is to simply walk away from an
armed opponent without dealing with them first. The zone of control
mechanic adds tactical depth to positioning and makes retreats more
strategically meaningful.

### 10.1.2. Vehicles

<img src="static/vehicles.svg" class="section-icon" />

This advanced combat rule requires the <span class="spurious-link"
target="* Spatial Relations">*Spatial Relations*</span> rules to be in
use.

Vehicles add a new layer of tactical complexity to combat encounters.
Whether it's a high-speed chase through a futuristic city or a naval
battle between warships, vehicles require different handling than
regular characters.

#### 10.1.2.1. Vehicle Statistics

Every vehicle has several key statistics:

- **Size**: Determines how many characters a vehicle can hold:

  - Small (S): One character riding on the outside
  - Medium (M): One character riding on the inside
  - Large (L): Four characters riding on the inside
  - Extra Large (XL): Six characters riding on the inside

- **Acceleration Rate**: A constant value measured in hexes,
  representing how many hexes the vehicle can add to its current speed
  each turn. This value also determines how many hexes the vehicle can
  subtract from its current speed each turn when braking. For example, a
  vehicle with an acceleration rate of 2 can increase or decrease its
  speed by up to 2 hexes per turn.

- **Maneuverability**: A constant rating that determines how many hex
  sides the vehicle can turn each turn. For example, a vehicle with a
  maneuverability of 2 can change its facing by up to 2 hex sides per
  turn.

- **Damage Resistance (DR)**: A constant value that reduces damage taken
  by anyone inside the vehicle. Characters riding inside a vehicle apply
  this DR in addition to any armor they are wearing when determining
  damage taken from attacks.

Vehicles also have variable values that are tracked during play:

- **Speed**: A variable value that changes over time and represents the
  number of hexes a vehicle moves on its turn, as long as this value is
  greater than zero. Vehicles must move this many hexes in the direction
  they are currently facing. Represented using a d100.

- **Facing**: The current hex side the vehicle is pointed, which
  determines the direction of movement. Represented by the direction the
  vehicle token or mini is pointing in.

#### 10.1.2.2. Steering and Movement

Vehicles have two primary movement actions that each cost 3 Action
Points:

- **Accelerating or Braking**: Vehicles can accelerate or brake by up to
  their acceleration rate in hexes per turn. Acceleration increases the
  vehicle's speed, while braking decreases it. A vehicle's speed can
  never be reduced below zero.

- **Turning**: Vehicles can change their facing by up to their
  maneuverability rating in hex sides per turn.

When steering, the vehicle's facing changes first, and then the vehicle
moves in that new direction. This means that players can plan their
turns by first deciding how much to turn, then moving the appropriate
number of hexes in that direction.

Vehicles must move a number of hexes equal to their current speed on
each turn, as long as their speed is greater than zero. This movement is
mandatory and must be in the direction the vehicle is currently facing.
Players cannot choose to move fewer hexes than their current speed.

#### 10.1.2.3. Using Vehicles in Combat

Characters operating vehicles use the vehicle's movement rules instead
of their own. Any characters riding in the vehicle move with it
automatically.

Attacks against vehicles directly are not possible in this system.
Instead, characters must target those inside the vehicle, and vehicles
act as simple pieces of armor for the characters inside the vehicle, but
not outside.

Vehicles can be used to ram enemies. This does an amount of damage
points determined by the vehicle's size plus its current speed, where
Small=5, Medium=10, Large=15, XL=20. The target can make a defense roll
(such as a skill check against **Physical (Dodge)**) as normal, even
though the vehicle does not make a combat roll or roll for damage.

XL vehicles can also be used to knock down walls, but this reduces the
speed of that vehicle back down to one.
