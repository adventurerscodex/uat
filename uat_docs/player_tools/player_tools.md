Stats
=====

As a player, all changes I make to hit points, hit dice, ability scores, savings throws, and other stats persist after I refresh the browser

As a player, I can increase or decrease my hit points via the stepper widget

As a player, I can see the hit points bar change colors at certain intervals as hit points decrease

As a player, hit dice are clickable and images change when clicked

As a player, if I click on a hit die, the changes persist after I refresh the browser

As a player, if I change the value in the level field, the number of hit dice match the level number

As a player, death save successes and failures are clickable and images change when clicked

As a player, death save changes persist after I refresh the browser

As a player, armor class is correctly calculated

As a player, initiative is correctly calculated

As a player, proficiency bonus is correctly calculated

As a player, I can can click on a popover showing the calculation for Armor Class

As a player, I can can click on a popover showing the calculation for Initiative

As a player, I can can click on a popover showing the calculation for Proficiency Bonus

As a player, I can increase or decrease my calculated armor class via a modifier field and this is reflected in the label

As a player, I can increase or decrease my calculated initiative via a modifier field and this is reflected in the label

As a player, I can increase or decrease my calculated proficiency via a modifier field and this is reflected in the label

As a player, if I am inspired, the status line should indicate this

As a player, I can select to become proficient in a savings throw, and this can be
viewed in the table via in icon

As a player, I can select to become half-proficient in a savings throw, and this can be
viewed in the table via in icon

As a player, I can select to become expertise in a savings throw, and this can be
viewed in the table via in icon

As a player, I can increase or decrease my savings throws via a modifier field

Skills
======

All fields for features, feats, traits, proficiencies, tracking, and skills persist after page refresh

Feature name field auto-completes with OGL data and the remaining fields pre-populate

Feats name field auto-completes with OGL data and the remaining fields pre-populate

Trait name field auto-completes with OGL data and the remaining fields pre-populate

Proficiencies and Languages name field auto-completes with OGL data and the remaining fields
pre-populate

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

As a player, I can add a note

As a player, I can delete a note

As a player, I can edit a note

As a player, I can view markdown in the edit tab

As a player, I can click on the link to the markdown guide

Profile
=======

As a player, all fields are editable and persist after refreshing the browser

As a player, if I start typing in the race field, OGL data auto-completes

As a player, if I start typing in the class field, OGL data auto-completes

As a player, if I start typing in the background field, OGL data auto-completes

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

As a player, I must add a character and player name to progress in the character creation wizard [complete]

As a player, when I start typing in the alignment field, OGL data auto-completes

As a player, when I start typing in the race field, OGL data auto-completes

As a player, when I start typing in the class field, OGL data auto-completes

As a player, when I starting typing in the background field, OGL data auto-completes

As a player, I can add values to all my ability scores

As a player, I am required to add values to all ability scores before progressing in the character creation wizard

As a player, I can navigate and complete the character creation wizard [complete]

As a player, after creating a character via the character creation wizard, I can view all the data entered in the stats and profile modules




