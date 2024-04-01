import random
import re
import time

import allure

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step('get sortable items')
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    # def change_list_order(self):
    #     self.element_is_visible(self.locators.TAB_LIST).click()
    #     order_before = self.get_sortable_items(self.locators.LIST_ITEM)
    #     item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
    #     item_what = item_list[0]
    #     item_where = item_list[1]
    #     self.action_drag_and_drop_to_element(item_what, item_where)
    #     order_after = self.get_sortable_items(self.locators.LIST_ITEM)
    #     return order_before, order_after
    @allure.step('change sortable order')
    def change_sortable_order(self, tab_name):
        tabs = {
            'list': {'title': self.locators.TAB_LIST, 'items': self.locators.LIST_ITEM},
            'grid': {'title': self.locators.TAB_GRID, 'items': self.locators.GRID_ITEM},
        }
        self.element_is_visible(tabs[tab_name]['title']).click()
        order_before = self.get_sortable_items(tabs[tab_name]['items'])
        item_list = random.sample(self.elements_are_visible(tabs[tab_name]['items']), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(tabs[tab_name]['items'])
        return [order_before, order_after]


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    @allure.step('click selectable item')
    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step('select list item')
    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.TAB_LIST_ITEM)
        active_element = self.element_is_visible(self.locators.TAB_ITEM_ACTIVE)
        return active_element.text

    @allure.step('select grid item')
    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_LIST).click()
        self.click_selectable_item(self.locators.GRID_LIST_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.step('get px from width and height')
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('get max and min size')
    def get_max_min_size(self, element):
        size = self.element_is_visible(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('change size of resizable box')
    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return [max_size, min_size]

    @allure.step('change size of resizable')
    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return [max_size, min_size]


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    @allure.step('check drop simple')
    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE_TAB)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE_TAB)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('check drop accept')
    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_ACCEPT_TAB)
        not_drag_div = self.element_is_visible(self.locators.NOT_DRAG_ME_ACCEPT_TAB)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT_TAB)
        self.action_drag_and_drop_to_element(not_drag_div, drop_div)
        drop_text_not_accept = drop_div.text  # Not accepted
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        drop_text_accept = drop_div.text  # Accepted
        return [drop_text_not_accept, drop_text_accept]

    @allure.step('check drop prevent propogation')
    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT_TAB)
        not_greedy_outer_box = self.element_is_visible(self.locators.NOT_GREEDY_OUTER_PREVENT_TAB)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_PREVENT_TAB)
        greedy_outer_box = self.element_is_visible(self.locators.GREEDY_OUTER_PREVENT_TAB)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_PREVENT_TAB)
        # Not greedy
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_outer_box = not_greedy_outer_box.text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        # Greedy
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_outer_box = greedy_outer_box.text
        text_greedy_inner_box = greedy_inner_box.text
        return [text_not_greedy_outer_box, text_not_greedy_inner_box], [text_greedy_outer_box, text_greedy_inner_box]

    @allure.step('check drop will revert draggable')
    def drop_will_revert_draggable(self, type_drag):
        draggable = {
            'will': self.locators.WILL_DRAG_REVERT_TAB,
            'will_not': self.locators.NOT_DRAG_REVERT_TAB
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        will_revert = self.element_is_visible(draggable[type_drag])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT_TAB)
        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(2)
        position_after_revert = will_revert.get_attribute('style')
        return [position_after_move, position_after_revert]


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    @allure.step('get before and after positions')
    def get_before_and_after_position(self, drag_element, x_offset=random.randint(0, 50),
                                      y_offset=random.randint(0, 50)):
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, x_offset, y_offset)
        after_position = drag_element.get_attribute('style')
        return [re.findall(r'\d[0-9]|\d', before_position), re.findall(r'\d[0-9]|\d', after_position)]

    @allure.step('check simple drag me')
    def simple_drag_me(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        simple_coords = self.get_before_and_after_position(drag_div)
        return simple_coords

    @allure.step('check axis drag me')
    def axis_drag_me(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        x_drag_div = self.element_is_visible(self.locators.AXIS_DRAG_X)
        y_drag_div = self.element_is_visible(self.locators.AXIS_DRAG_Y)
        x_coords = self.get_before_and_after_position(x_drag_div, y_offset=0)
        y_coords = self.get_before_and_after_position(y_drag_div, x_offset=0)
        return x_coords, y_coords
