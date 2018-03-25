"""UAT test file for Adventurer's Codex player tools skills module."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # noqa
from selenium.webdriver.support.ui import WebDriverWait

from components.core.character import features, feats, traits
from components.core.character import tracked, proficiency, skills
from components.core.character.tabs import Tabs
from expected_conditions.conditions import modal_finished_closing
from expected_conditions.conditions import sorting_arrow_up, sorting_arrow_down
from expected_conditions.conditions import table_cell_updated
from utils import utils as ut


def test_add_feature(player_wizard, browser): # noqa
    """As a player, I can add a feature."""
    print('As a player, I can add a feature.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    tracked_table = tracked.TrackedTable(browser)
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

    assert tracked_table.tracked1_name.text == 'Add Name'
    assert tracked_table.tracked1_max.text == '4'
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
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, 'modal-backdrop fade')
        )
    )
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located(
            (By.ID, 'addFeature')
        )
    )
    rows[0][2].click()
    rows = ut.get_table_rows(features_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new Feature'


def test_add_autocomplete_feature(player_wizard, browser): # noqa
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

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, features_table.add_id)
        )
    )

    features_table.add.click()
    ut.select_from_autocomplete(feature, 'name', '', browser)
    feature.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(feature.modal_div_id)
    )

    rows = ut.get_table_rows(features_table, 'table', values=False)
    rows[0][0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, feature_tabs.edit_id)
        )
    )

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

    WebDriverWait(browser, 10).until(
        modal_finished_closing(feature_edit.modal_div_id)
    )

    row = ut.get_table_row(features_table, 'table', 1)

    assert row.feature == 'Edited Name'
    assert row.class_ == 'Edited Class'


def test_add_feat(player_wizard, browser): # noqa
    """As a player, I can add a feat."""
    print('As a player, I can add a feat.')

    feat = feats.FeatAddModal(browser)
    feats_table = feats.FeatsTable(browser)
    tracked_table = tracked.TrackedTable(browser)
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

    assert tracked_table.tracked1_name.text == 'Add Name'
    assert tracked_table.tracked1_max.text == '4'
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

    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located(
            (By.ID, 'addFeat')
        )
    )
    rows[0][1].click()
    rows = ut.get_table_rows(feats_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new Feat'


def test_add_autocomplete_feat(player_wizard, browser): # noqa
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

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, feats_table.add_id)
        )
    )

    feats_table.add.click()
    ut.select_from_autocomplete(feat, 'name', '', browser)
    feat.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(feat.modal_div_id)
    )

    rows = ut.get_table_rows(feats_table, 'table', values=False)
    rows[0][0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, feat_tabs.edit_id)
        )
    )

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

    WebDriverWait(browser, 10).until(
        modal_finished_closing(feat_edit.modal_div_id)
    )

    WebDriverWait(browser, 10).until(
        table_cell_updated(
            feats_table,
            'feat',
            'Edited Name',
            'table',
            1
        )
    )

    row = ut.get_table_row(feats_table, 'table', 1)

    assert row.feat == 'Edited Name'


def test_add_trait(player_wizard, browser): # noqa
    """As a player, I can add a trait."""
    print('As a player, I can add a trait.')

    trait = traits.TraitAddModal(browser)
    traits_table = traits.TraitsTable(browser)
    tracked_table = tracked.TrackedTable(browser)
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
    assert trait.race.get_attribute('value') == 'Add Race'
    assert trait.description.get_attribute('value') == 'Add Description'
    assert trait.max_.get_attribute('value') == '4'
    assert 'active' in trait.short_rest.get_attribute('class')

    trait.add.click()

    row = ut.get_table_row(traits_table, 'table', 1)

    assert tracked_table.tracked1_name.text == 'Add Name'
    assert tracked_table.tracked1_max.text == '4'
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

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, traits_table.add_id)
        )
    )

    traits_table.add.click()
    ut.select_from_autocomplete(trait, 'name', '', browser)
    trait.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(trait.modal_div_id)
    )

    rows = ut.get_table_rows(traits_table, 'table', values=False)
    rows[0][2].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(traits_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new Trait'


def test_add_autocomplete_trait(player_wizard, browser): # noqa
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

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, traits_table.add_id)
        )
    )

    traits_table.add.click()
    ut.select_from_autocomplete(trait, 'name', '', browser)
    trait.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(trait.modal_div_id)
    )

    rows = ut.get_table_rows(traits_table, 'table', values=False)
    rows[0][0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, trait_tabs.edit_id)
        )
    )

    trait_tabs.edit.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, trait_edit.name_id)
        )
    )

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

    WebDriverWait(browser, 10).until(
        modal_finished_closing(trait.modal_div_id)
    )

    WebDriverWait(browser, 10).until(
        table_cell_updated(
            traits_table,
            'trait',
            'Edited Name',
            'table',
            1
        )
    )

    row = ut.get_table_row(traits_table, 'table', 1)

    assert row.trait == 'Edited Name'
    assert row.race == 'Edited Race'


def test_add_proficiency(player_wizard, browser): # noqa
    """As a player, I can add a proficiency."""
    print('As a player, I can add a proficiency.')

    proficiency_add = proficiency.ProficiencyAddModal(browser)
    proficiency_table = proficiency.ProficiencyTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    proficiency_table.add.click()
    proficiency_add.name = 'Add Name'
    proficiency_add.type_ = 'Add Type'
    proficiency_add.description = 'Add Description'

    assert proficiency_add.name.get_attribute('value') == 'Add Name'
    assert proficiency_add.type_.get_attribute('value') == 'Add Type'
    assert proficiency_add.description.get_attribute('value') == 'Add Description'

    proficiency_add.add.click()

    row = ut.get_table_row(proficiency_table, 'table', 1)
    assert row.type == 'Add Type'
    assert row.proficiency == 'Add Name'

def test_proficiency_ogl_pre_pop(player_wizard, browser): # noqa
    """As a player, if I select from proficiency name field, OGL data auto-completes and the remaining fields pre-populate."""
    print('As a player, if I select from proficiency name field, OGL data auto-completes and the remaining fields pre-populate.')

    proficiency_add = proficiency.ProficiencyAddModal(browser)
    proficiency_table = proficiency.ProficiencyTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    proficiency_table.add.click()
    ut.select_from_autocomplete(proficiency_add, 'name', '', browser)
    proficiency_add.add.click()

    row = ut.get_table_row(proficiency_table, 'table', 1)

    assert row.type == 'Languages'
    assert row.proficiency == 'Abyssal'

def test_delete_proficiency(player_wizard, browser): # noqa
    """As a player, I can delete a proficiency."""
    print('As a player, I can delete a proficiency.')

    proficiency_add = proficiency.ProficiencyAddModal(browser)
    proficiency_table = proficiency.ProficiencyTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, proficiency_table.add_id)
        )
    )

    proficiency_table.add.click()
    ut.select_from_autocomplete(proficiency_add, 'name', '', browser)
    proficiency_add.add.click()

    rows = ut.get_table_rows(proficiency_table, 'table', values=False)

    WebDriverWait(browser, 10).until(
        modal_finished_closing(proficiency_add.modal_div_id)
    )

    rows[0][2].find_element_by_tag_name('a').click()
    rows = ut.get_table_rows(proficiency_table, 'table', values=False)

    assert rows[0][0].text == 'Add a new Proficiency'

def test_autocomplete_proficiency(player_wizard, browser): # noqa
    """As a player, if I start typing in the name field and class field, I can select suggested items in the dropdown."""
    print('As a player, if I start typing in the name field and type field, I can select suggested items in the dropdown.')

    proficiency_add = proficiency.ProficiencyAddModal(browser)
    proficiency_table = proficiency.ProficiencyTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    proficiency_table.add.click()
    ut.select_from_autocomplete(proficiency_add, 'name', '', browser)
    ut.select_from_autocomplete(proficiency_add, 'type_', '', browser)

    assert proficiency_add.name.get_attribute('value') == 'Abyssal'
    assert proficiency_add.type_.get_attribute('value') == 'Armor'

def test_add_proficiency_open_model_by_row(player_wizard, browser): # noqa
    """As a player, I can click the first row in proficiency table to open the proficiency add modal."""
    print('As a player, I can click the first row in proficiency table to open the proficiency add modal.')

    proficiency_table = proficiency.ProficiencyTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    rows = ut.get_table_rows(proficiency_table, 'table', values=False)

    assert rows[0][0].is_enabled()
    assert rows[0][0].is_displayed()

def test_edit_proficiency(player_wizard, browser): # noqa
    """As a player, I can edit a proficiency."""
    print('As a player, I can edit a proficiency.')

    proficiency_add = proficiency.ProficiencyAddModal(browser)
    proficiency_edit = proficiency.ProficiencyEditModal(browser)
    proficiency_table = proficiency.ProficiencyTable(browser)
    proficiency_tabs = proficiency.ProficiencyModalTabs(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, proficiency_table.add_id)
        )
    )

    proficiency_table.add.click()
    ut.select_from_autocomplete(proficiency_add, 'name', '', browser)
    proficiency_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(proficiency_add.modal_div_id)
    )

    rows = ut.get_table_rows(proficiency_table, 'table', values=False)
    rows[0][0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, proficiency_tabs.edit_id)
        )
    )

    proficiency_tabs.edit.click()

    proficiency_edit.name.clear()
    proficiency_edit.type_.clear()
    proficiency_edit.description.clear()

    proficiency_edit.name = 'Edited Name'
    proficiency_edit.type_ = 'Edited Type'
    proficiency_edit.description = 'Edited Description'

    assert proficiency_edit.name.get_attribute('value') == 'Edited Name'
    assert proficiency_edit.type_.get_attribute('value') == 'Edited Type'
    assert proficiency_edit.description.get_attribute('value') == 'Edited Description'

    proficiency_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(proficiency_edit.modal_div_id)
    )

    row = ut.get_table_row(proficiency_table, 'table', 1)

    assert row.proficiency == 'Edited Name'
    assert row.type == 'Edited Type'

def test_tracked_increase_decrease(player_wizard, browser): # noqa
    """As a player, I can increase or decrease tracked abilities with the stepper widget and the bar reflects these changes."""

    print('As a player, I can increase or decrease tracked abilities with the stepper widget and the bar reflects these changes.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    tracked_table = tracked.TrackedTable(browser)
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

    feature.add.click()

    tracked_table.tracked1_used_up.click()

    assert tracked_table.tracked1_used.text == '1'

    tracked_table.tracked1_used_down.click()

    assert tracked_table.tracked1_used.text == '0'

def test_tracked_reset(player_wizard, browser): # noqa
    """As a player, I can reset a tracked ability by clicking on the reset icon."""

    print('As a player, I can reset a tracked ability by clicking on the reset icon.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    tracked_table = tracked.TrackedTable(browser)
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

    feature.add.click()

    tracked_table.tracked1_used_up.click()

    assert tracked_table.tracked1_used.text == '1'

    tracked_table.tracked1_refresh.click()

    assert tracked_table.tracked1_used.text == '0'

def test_proficiency_types(player_wizard, browser): # noqa
    """As a player, I can mark a skill as none, half, proficient, or
       expertise and view these modifiers, and they are calculated correctly."""

    print(('As a player, I can mark a skill as none, half, proficient, or '
           'expertise and view these modifiers, and they are calculated '
           'correctly.'))

    skills_table = skills.SkillsTable(browser)
    skills_edit = skills.SkillsEditModal(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    acrobatics = ut.get_table_row(skills_table, 'table', values=False)
    none = acrobatics[0].find_element_by_tag_name('span').get_attribute('class')
    acrobatics[0].click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, skills_edit.half_xpath)
        )
    )
    skills_edit.half.click()
    skills_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(skills_edit.modal_div_xpath)
    )

    acrobatics = ut.get_table_row(skills_table, 'table', values=False)
    spans = acrobatics[0].find_element_by_tag_name('span')
    half = spans.find_element_by_tag_name('span').get_attribute('class')

    acrobatics[0].click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, skills_edit.proficient_xpath)
        )
    )
    skills_edit.proficient.click()
    skills_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(skills_edit.modal_div_xpath)
    )
    acrobatics = ut.get_table_row(skills_table, 'table', values=False)
    spans = acrobatics[0].find_element_by_tag_name('span')
    proficient = spans.find_element_by_tag_name('span').get_attribute('class')

    acrobatics[0].click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, skills_edit.expertise_xpath)
        )
    )
    skills_edit.expertise.click()
    skills_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(skills_edit.modal_div_xpath)
    )

    acrobatics = ut.get_table_row(skills_table, 'table', values=False)
    spans = acrobatics[0].find_element_by_tag_name('span')
    expertise = spans.find_element_by_tag_name('span').get_attribute('class')

    assert '' in none
    assert 'fa fa-adjust' in half
    assert 'fa fa-check' in proficient
    assert 'fa fa-check close-check' in expertise

def test_passive_score(player_wizard, browser): # noqa
    """As a player, I can view my passive score for each skill which is calculated correctly."""

    print('As a player, I can view my passive score for each skill which is calculated correctly.')

    skills_table = skills.SkillsTable(browser)
    tabs = Tabs(browser)
    tabs.skills.click()

    acrobatics = ut.get_table_row(skills_table, 'table')

    assert acrobatics.passive == '14'

def test_data_persists(player_wizard, browser): # noqa
    """As a player, all changes I make to features, feats, traits, proficiencies, tracking, and skills persist after I refresh the browser."""

    print('As a player, all changes I make to features, feats, traits, proficiencies, tracking, and skills persist after I refresh the browser.')

    feature = features.FeatureAddModal(browser)
    features_table = features.FeaturesTable(browser)
    feat = feats.FeatAddModal(browser)
    feats_table = feats.FeatsTable(browser)
    trait = traits.TraitAddModal(browser)
    traits_table = traits.TraitsTable(browser)
    tracked_table = tracked.TrackedTable(browser)
    proficiency_add = proficiency.ProficiencyAddModal(browser)
    proficiency_table = proficiency.ProficiencyTable(browser)
    skills_table = skills.SkillsTable(browser)
    skills_edit = skills.SkillsEditModal(browser)
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

    feature.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(feature.modal_div_id)
    )

    feats_table.add.click()
    ut.select_from_autocomplete(feat, 'name', '', browser)
    feat.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(feat.modal_div_id)
    )

    traits_table.add.click()
    ut.select_from_autocomplete(trait, 'name', '', browser)
    trait.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(trait.modal_div_id)
    )

    proficiency_table.add.click()
    ut.select_from_autocomplete(proficiency_add, 'name', '', browser)
    proficiency_add.add.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(proficiency_add.modal_div_id)
    )

    acrobatics = ut.get_table_row(skills_table, 'table', values=False)
    acrobatics[0].click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, skills_edit.half_xpath)
        )
    )

    skills_edit.half.click()
    skills_edit.done.click()

    WebDriverWait(browser, 10).until(
        modal_finished_closing(skills_edit.modal_div_xpath)
    )

    browser.refresh()

    row = ut.get_table_row(features_table, 'table', 1)

    assert tracked_table.tracked1_name.text == 'Add Name'
    assert tracked_table.tracked1_max.text == '4'
    assert row.class_ == 'Add Class'
    assert row.feature == 'Add Name'

    row = ut.get_table_row(feats_table, 'table', 1)

    assert row.feat == 'Grappler'

    row = ut.get_table_row(traits_table, 'table', 1)

    assert row.race == 'Dragonborn'
    assert row.trait == 'Ability Score Increase'

    row = ut.get_table_row(proficiency_table, 'table', 1)

    assert row.type == 'Languages'
    assert row.proficiency == 'Abyssal'
