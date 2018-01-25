"""UAT test file for Adventurer's Codex player tools skills module."""
import time

from selenium.webdriver.support import expected_conditions as EC # noqa

from components.character import features, feats, traits
from components.character.tabs import Tabs
from utils import utils as ut


def test_add_feature(player_wizard, browser): # noqa
    """As a player, I can add a feature."""
    print('As a player, I can add a feature.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    features_table.add.click()
    feature.name = 'Add Name'
    feature.class_ = 'Add Class'
    feature.level = 1
    feature.description = 'Add Description'
    feature.tracked.click()
    feature.max_.clear()
    feature.max_ = 4
    feature.short_rest.click()

    assert feature.name.get_attribute('value') == 'Add Name'
    assert feature.class_.get_attribute('value') == 'Add Class'
    assert feature.level.get_attribute('value') == '1'
    assert feature.description.get_attribute('value') == 'Add Description'
    assert feature.max_.get_attribute('value') == '4'
    assert 'active' in feature.short_rest.get_attribute('class')

    feature.add.click()

    row = ut.get_table_row(features_table, 'table', 1)

    assert row.class_ == 'Add Class'
    assert row.feature == 'Add Name'


def test_feature_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from feature name field, OGL data auto-completes and the remaining fields pre-populate."""
    print('As a player, if I select from feature name field, OGL data auto-completes and the remaining fields pre-populate.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    features_table.add.click()
    ut.select_from_autocomplete(feature, 'name', '', browser)
    feature.add.click()

    row = ut.get_table_row(features_table, 'table', 1)

    assert row.class_ == 'Barbarian'
    assert row.feature == 'Rage'


def test_delete_feature(player_wizard, browser): # noqa
    """As a player, I can delete a feature."""
    print('As a player, I can delete a feature.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    features_table.add.click()
    ut.select_from_autocomplete(feature, 'name', '', browser)
    feature.add.click()

    rows = ut.get_table_rows(features_table, 'table', values=False)
    time.sleep(.3)
    rows[0][2].click()
    rows = ut.get_table_rows(features_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new Feature'


def test_add_feature(player_wizard, browser): # noqa
    """As a player, if I start typing in the name field and class field, I can select suggested items in the dropdown."""
    print('As a player, if I start typing in the name field and class field, I can select suggested items in the dropdown.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    features_table.add.click()
    ut.select_from_autocomplete(feature, 'name', '', browser)
    ut.select_from_autocomplete(feature, 'class_', '', browser)

    assert feature.name.get_attribute('value') == 'Rage (Barbarian, Lvl. 1)'
    assert feature.class_.get_attribute('value') == 'Barbarian'


def test_add_feature_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in feature table to open the feature add modal."""
    print('As a player, I can click the first row in feature table to open the feature add modal.')

    features_table = features.FeaturesTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    rows = ut.get_table_rows(features_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()


def test_edit_feature(player_wizard, browser): # noqa
    """As a player, I can edit a feature."""
    print('As a player, I can edit a feature.')

    feature = features.FeatureAddModal(browser)
    feature_edit = features.FeatureEditModal(browser)
    features_table = features.FeaturesTable(browser)
    feature_tabs = features.FeatureModalTabs(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    features_table.add.click()
    ut.select_from_autocomplete(feature, 'name', '', browser)
    feature.add.click()

    rows = ut.get_table_rows(features_table, 'table', values=False)
    time.sleep(.3)
    rows[0][0].click()
    time.sleep(.3)
    feature_tabs.edit.click()

    feature_edit.name.clear()
    feature_edit.class_.clear()
    feature_edit.level.clear()
    feature_edit.description.clear()

    feature_edit.name = 'Edited Name'
    feature_edit.class_ = 'Edited Class'
    feature_edit.level = 1
    feature_edit.description = 'Edited Description'
    feature_edit.tracked.click()
    feature_edit.max_.clear()
    feature_edit.max_ = 4
    feature_edit.short_rest.click()

    assert feature_edit.name.get_attribute('value') == 'Edited Name'
    assert feature_edit.class_.get_attribute('value') == 'Edited Class'
    assert feature_edit.level.get_attribute('value') == '1'
    assert feature_edit.description.get_attribute('value') == 'Edited Description'
    assert feature_edit.max_.get_attribute('value') == '4'
    assert 'active' in feature_edit.short_rest.get_attribute('class')
    feature_edit.done.click()

    rows = ut.get_table_rows(features_table, 'table', values=False)
    time.sleep(.3)

    row = ut.get_table_row(features_table, 'table', 1)
    assert row.feature == 'Edited Name'
    assert row.class_ == 'Edited Class'


def test_add_feat(player_wizard, browser): # noqa
    """As a player, I can add a feat."""
    print('As a player, I can add a feat.')

    feat = feats.FeatAddModal(browser)
    feats_table = feats.FeatsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    feats_table.add.click()
    feat.name = 'Add Name'
    feat.description = 'Add Description'
    feat.tracked.click()
    feat.max_.clear()
    feat.max_ = 4
    feat.short_rest.click()

    assert feat.name.get_attribute('value') == 'Add Name'
    assert feat.description.get_attribute('value') == 'Add Description'
    assert feat.max_.get_attribute('value') == '4'
    assert 'active' in feat.short_rest.get_attribute('class')

    feat.add.click()

    row = ut.get_table_row(feats_table, 'table', 1)

    assert row.feat == 'Add Name'


def test_feat_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from feat name field, OGL data auto-completes and the remaining fields pre-populate."""
    print('As a player, if I select from feat name field, OGL data auto-completes and the remaining fields pre-populate.')

    feat = feats.FeatAddModal(browser)
    feats_table = feats.FeatsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    feats_table.add.click()
    ut.select_from_autocomplete(feat, 'name', '', browser)
    feat.add.click()

    row = ut.get_table_row(feats_table, 'table', 1)

    assert row.feat == 'Grappler'


def test_delete_feat(player_wizard, browser): # noqa
    """As a player, I can delete a feat."""
    print('As a player, I can delete a feat.')

    feat = feats.FeatAddModal(browser)
    feats_table = feats.FeatsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    feats_table.add.click()
    ut.select_from_autocomplete(feat, 'name', '', browser)
    feat.add.click()

    rows = ut.get_table_rows(feats_table, 'table', values=False)
    time.sleep(.3)
    rows[0][1].click()
    rows = ut.get_table_rows(feats_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new Feat'


def test_add_feat(player_wizard, browser): # noqa
    """As a player, if I start typing in the name field and class field, I can select suggested items in the dropdown."""
    print('As a player, if I start typing in the name field and class field, I can select suggested items in the dropdown.')

    feat = feats.FeatAddModal(browser)
    feats_table = feats.FeatsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    feats_table.add.click()
    ut.select_from_autocomplete(feat, 'name', '', browser)

    assert feat.name.get_attribute('value') == 'Grappler'


def test_add_feat_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in feat table to open the feat add modal."""
    print('As a player, I can click the first row in feat table to open the feat add modal.')

    feats_table = feats.FeatsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    rows = ut.get_table_rows(feats_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()


def test_edit_feat(player_wizard, browser): # noqa
    """As a player, I can edit a feat."""
    print('As a player, I can edit a feat.')

    feat = feats.FeatAddModal(browser)
    feat_edit = feats.FeatEditModal(browser)
    feats_table = feats.FeatsTable(browser)
    feat_tabs = feats.FeatModalTabs(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    feats_table.add.click()
    ut.select_from_autocomplete(feat, 'name', '', browser)
    feat.add.click()

    rows = ut.get_table_rows(feats_table, 'table', values=False)
    time.sleep(.3)
    rows[0][0].click()
    time.sleep(.3)
    feat_tabs.edit.click()

    feat_edit.name.clear()
    feat_edit.description.clear()

    feat_edit.name = 'Edited Name'
    feat_edit.description = 'Edited Description'
    feat_edit.tracked.click()
    feat_edit.max_.clear()
    feat_edit.max_ = 4
    feat_edit.short_rest.click()

    assert feat_edit.name.get_attribute('value') == 'Edited Name'
    assert feat_edit.description.get_attribute('value') == 'Edited Description'
    assert feat_edit.max_.get_attribute('value') == '4'
    assert 'active' in feat_edit.short_rest.get_attribute('class')
    feat_edit.done.click()

    rows = ut.get_table_rows(feats_table, 'table', values=False)
    time.sleep(.3)

    row = ut.get_table_row(feats_table, 'table', 1)
    assert row.feat == 'Edited Name'


def test_add_trait(player_wizard, browser): # noqa
    """As a player, I can add a trait."""
    print('As a player, I can add a trait.')

    trait = traits.TraitAddModal(browser)
    traits_table = traits.TraitsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    traits_table.add.click()
    trait.name = 'Add Name'
    trait.race = 'Add Race'
    trait.description = 'Add Description'
    trait.tracked.click()
    trait.max_.clear()
    trait.max_ = 4
    trait.short_rest.click()

    assert trait.name.get_attribute('value') == 'Add Name'
    assert trait.class_.get_attribute('value') == 'Add Race'
    assert trait.level.get_attribute('value') == '1'
    assert trait.description.get_attribute('value') == 'Add Description'
    assert trait.max_.get_attribute('value') == '4'
    assert 'active' in trait.short_rest.get_attribute('class')

    trait.add.click()

    row = ut.get_table_row(traits_table, 'table', 1)

    assert row.race == 'Add Race'
    assert row.trait == 'Add Name'


def test_trait_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from trait name field, OGL data auto-completes and the remaining fields pre-populate."""
    print('As a player, if I select from trait name field, OGL data auto-completes and the remaining fields pre-populate.')

    trait = traits.TraitAddModal(browser)
    traits_table = traits.TraitsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    traits_table.add.click()
    ut.select_from_autocomplete(trait, 'name', '', browser)
    trait.add.click()

    row = ut.get_table_row(traits_table, 'table', 1)

    assert row.race == 'Dragonborn'
    assert row.trait == 'Ability Score Increase'


def test_delete_trait(player_wizard, browser): # noqa
    """As a player, I can delete a trait."""
    print('As a player, I can delete a trait.')

    trait = traits.TraitAddModal(browser)
    traits_table = traits.TraitsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    traits_table.add.click()
    ut.select_from_autocomplete(trait, 'name', '', browser)
    trait.add.click()

    rows = ut.get_table_rows(traits_table, 'table', values=False)
    time.sleep(.3)
    rows[0][2].click()
    rows = ut.get_table_rows(traits_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new Trait'


def test_add_trait(player_wizard, browser): # noqa
    """As a player, if I start typing in the name field and class field, I can select suggested items in the dropdown."""
    print('As a player, if I start typing in the name field and class field, I can select suggested items in the dropdown.')

    trait = traits.TraitAddModal(browser)
    traits_table = traits.TraitsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    traits_table.add.click()
    ut.select_from_autocomplete(trait, 'name', '', browser)
    ut.select_from_autocomplete(trait, 'race', '', browser)

    assert trait.name.get_attribute('value') == 'Ability Score Increase (Dragonborn)'
    assert trait.race.get_attribute('value') == 'Dwarf'


def test_add_trait_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in trait table to open the trait add modal."""
    print('As a player, I can click the first row in trait table to open the trait add modal.')

    traits_table = traits.TraitsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    rows = ut.get_table_rows(traits_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()


def test_edit_trait(player_wizard, browser): # noqa
    """As a player, I can edit a trait."""
    print('As a player, I can edit a trait.')

    trait = traits.TraitAddModal(browser)
    trait_edit = traits.TraitEditModal(browser)
    traits_table = traits.TraitsTable(browser)
    trait_tabs = traits.TraitModalTabs(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    traits_table.add.click()
    ut.select_from_autocomplete(trait, 'name', '', browser)
    trait.add.click()

    rows = ut.get_table_rows(traits_table, 'table', values=False)
    time.sleep(.3)
    rows[0][0].click()
    time.sleep(.3)
    trait_tabs.edit.click()

    trait_edit.name.clear()
    trait_edit.race.clear()
    trait_edit.description.clear()

    trait_edit.name = 'Edited Name'
    trait_edit.race = 'Edited Race'
    trait_edit.description = 'Edited Description'
    trait_edit.tracked.click()
    trait_edit.max_.clear()
    trait_edit.max_ = 4
    trait_edit.short_rest.click()

    assert trait_edit.name.get_attribute('value') == 'Edited Name'
    assert trait_edit.race.get_attribute('value') == 'Edited Race'
    assert trait_edit.description.get_attribute('value') == 'Edited Description'
    assert trait_edit.max_.get_attribute('value') == '4'
    assert 'active' in trait_edit.short_rest.get_attribute('class')
    trait_edit.done.click()

    rows = ut.get_table_rows(traits_table, 'table', values=False)
    time.sleep(.3)

    row = ut.get_table_row(traits_table, 'table', 1)
    assert row.trait == 'Edited Name'
    assert row.race == 'Edited Race'
