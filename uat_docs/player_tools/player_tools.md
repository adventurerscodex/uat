Stats
=====

All fields for hit points, hit dice, ability scores, savings throws, and other stats persist
Hit points stepper is functional and hit points bar increases and decreases accordingly
Hit points bar changes color at certain intervals as hit points decrease
Hit dice are clickable and images change when clicked
Hit dice changes persist
When level is increased or decreased, the number of hit dice match the level number
Death save successes and failures are clickable and images change when clicked
Death save changes persist
Armor class is correctly calculated
Initiative is correctly calculated
Proficiency bonus is correctly calculated
Popovers showing calculations are available for AC, Initiative, and Proficiency Bonus
Modifiers in AC, Initiative, and Proficiency bonus are reflected
If inspiration is greater than 0, status line should indicate character is inspired
Savings throws can be checked as proficient and a checkbox denotes this in table
Savings throws modifier is functional for both positive and negative numbers

Skills
======

All fields for features, feats, traits, proficiencies, tracking, and skills persist after page refresh
Feature name field auto-completes with OGL data and the remaining fields pre-populate
Feats name field auto-completes with OGL data and the remaining fields pre-populate
Trait name field auto-completes with OGL data and the remaining fields pre-populate
Proficiencies and Languages name field auto-completes with OGL data and the remaining fields pre-populate
Features can be added, deleted, and edited
Feats can be added, deleted, and edited
Traits can be added, deleted, and edited
Proficiencies and Languages can be added, deleted, and edited
Features, Feats, Traits, Proficiencies and Languages include checkbox for tracked and can be set to reset on short or long rest
In the tracker, item may be set to short or long rest, and the table should show appropriate icon
Tracked items can be refreshed by clicking on the refresh icon in the table
The stepper is functional in the tracked table and bar is increased and decreased accordingly
Skills marked as none, half, proficient, or expertise are calculated correctly
Passive score is calculated correctly for skills

Spells
======

All fields for spell slots, spell stats, and spells persist after page refresh
Spell name field auto-completes with OGL data and the remaining fields pre-populate
Spells can be added, deleted, and edited
Spell slots can be added, deleted, and edited
Spell stats can be added, deleted, and edited
If no spells are in table, clicking the first row will trigger add modal
Spells may be prepared by clicking in the checkbox, and prepared spells persist
If a spell is always prepared, the prepared checkbox in the table is not clickable
In the modal if a spell is always prepared, the prepared checkbox is disabled
In the modal if a spell is prepared, the always prepared checkbox is disabled
The preview modal for spells displays the data correctly and includes a watermark denoting the correct spell school
Spell casting ability auto-completes in spell stats modal
Spell slots can be refreshed by clicking on the refresh icon in the table
Spell slots can be assigned to reset on short or long rests
The stepper is functional in the spell slots table
If the spell is a ritual, the text ritual is displayed in the spell name in the table
If the spell is level 0, the spell is denoted in the table as a cantrip and there is no checkbox to prepare the spell
In the spells modal footer, total spells and spells prepared are calculated correctly


Equipment
=========

All fields for weapons and armor persist after page refresh
Weapons name field auto-completes with OGL data and the remaining fields pre-populate
Armor items name field auto-completes with OGL data and the remaining fields pre-populate
Weapons can be added, deleted, and edited
Armor can be added, deleted, and edited
If no weapons are in table, clicking the first row will trigger add modal
If no armor are in table, clicking the first row will trigger add modal
In the weapons table, total weight is calculated correctly
In the armor table, total weight is calculated correctly
Armor don and doff is working, and the checkbox appears when armor is donned
If weapons or armor are magical, a badge indicating the modifier is present

Inventory
=========

All fields for coins, magic items, Inventory persist after page refresh
Total weight calculated correctly for magic items, inventory, and coinsl
Magic items name field auto-completes with OGL data and the remaining fields pre-populate
Inventory items name field auto-completes with OGL data and the remaining fields pre-populate
Magic items can be added, deleted, and edited
Inventory items can be added, deleted, and edited
If no magic items are in table, clicking the first row will trigger add modal
If no inventory items are in table, clicking the first row will trigger add modal

Notes
=====

Notes can be added, deleted, and edited
The preview tab displays text in the edit tab as markdown
The link to markdown guide is functional

Profile
=======

All fields are editable and persist after refreshing the page
Race, Class, and Background fields auto-complete with OGL data

Global Page
===========

Images may be added and displayed by URL
Images may be added and displayed via Gravatar
User should be able to log in
User should be able to sign up for a new account
New/Import link is functional
A new character can be imported from dropbox
Characters and Games link is functional
Characters and Games should be able to be deleted from modal
Remaining storage space is displayed in the modal and increases and decreases accordingly
Switching between characters is functional
More info on storage link is functional
Export link is functional
Manage party link is functional
Actions button is functional
Long and short resting is functional including toastr notifications
A previously saved .json character should import the saved data elements
All imported data elements should include unicode and there should be no html entities
A character export should save all data elements in a .json format
Unicode characters should be saved
Status line is functional and displays weight, inspiration, heathiness, features, spells
Navbar header links to blog, newsletter, patreon, and website
Navbar footer links to facebook, twitter, google +, github, reddit, rss feed, contact page, and ogl license

Calculations
============

When level is altered, verify the following:

Proficiency calculation reflects the change

When Strength modifier if altered, verify the following are calculated correctly:

Skills bound to strength
Savings throws bound to strength
Encumbrance
To hit modifier

When Dexterity modifier is altered, verify the following are calculated correctly:

Skills bound to dexterity
Savings throws bound to dexterity
Initiative
Armor class (Pro tip: if the armor is heavy, dex modifier is not used for positive or negative numbers)
To hit bonus uses the higher of strength or dexterity if the weapon is of type finesse

When Con, Int, Wis, Cha modifiers are altered, verify the following are calculated correctly:

Skills bound to their reflective modifier
Savings throws bound to their reflective modifier

Wizard
======

The wizard can be completed [complete]
Character name and player name are marked as required [complete]
When character name and player name are entered, the required notice is no longer visible [complete]
All fields persist
Alignment auto-completes with OGL data
Race auto-completes with OGL data
Class auto-completes with OGL data
Background auto-completes with OGL data
All ability scores persist
All ability scores are shown as required
When ability scores are entered, the required notice is no longer visible
All data completed in the wizard is displayed in the stats and profile modules



