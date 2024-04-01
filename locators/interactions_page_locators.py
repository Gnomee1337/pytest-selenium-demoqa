from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a#demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, "div#demo-tabpane-list div[class='list-group-item list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, "div#demo-tabpane-grid div[class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a#demo-tab-list')
    TAB_LIST_ITEM = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    TAB_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")

    GRID_LIST = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_LIST_ITEM = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, "div.constraint-area span.react-resizable-handle.react-resizable-handle-se")
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div#resizableBoxWithRestriction")
    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR, "div#resizable span.react-resizable-handle.react-resizable-handle-se")
    RESIZABLE = (By.CSS_SELECTOR, "div#resizable")


class DroppablePageLocators:
    # Simple Tab
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-simple')
    DRAG_ME_SIMPLE_TAB = (By.CSS_SELECTOR, 'div#draggable')
    DROP_HERE_SIMPLE_TAB = (By.CSS_SELECTOR, 'div#simpleDropContainer div#droppable')

    # Accept Tab
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-accept')
    DRAG_ME_ACCEPT_TAB = (By.CSS_SELECTOR, 'div#acceptable')
    NOT_DRAG_ME_ACCEPT_TAB = (By.CSS_SELECTOR, 'div#notAcceptable')
    DROP_HERE_ACCEPT_TAB = (By.CSS_SELECTOR, 'div#acceptDropContainer div#droppable')

    # Prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-preventPropogation')
    DRAG_ME_PREVENT_TAB = (By.CSS_SELECTOR, 'div#dragBox')
    NOT_GREEDY_OUTER_PREVENT_TAB = (By.CSS_SELECTOR, 'div#notGreedyDropBox p:nth-child(1)')
    NOT_GREEDY_INNER_PREVENT_TAB = (By.CSS_SELECTOR, 'div#notGreedyInnerDropBox')
    GREEDY_OUTER_PREVENT_TAB = (By.CSS_SELECTOR, 'div#greedyDropBox p:nth-child(1)')
    GREEDY_INNER_PREVENT_TAB = (By.CSS_SELECTOR, 'div#greedyDropBoxInner')

    # Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-revertable')
    WILL_DRAG_REVERT_TAB = (By.CSS_SELECTOR, 'div#revertable')
    NOT_DRAG_REVERT_TAB = (By.CSS_SELECTOR, 'div#notRevertable')
    DROP_HERE_REVERT_TAB = (By.CSS_SELECTOR, 'div#revertableDropContainer div#droppable')


class DraggablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a#draggableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, 'div#dragBox')

    AXIS_TAB = (By.CSS_SELECTOR, 'a#draggableExample-tab-axisRestriction')
    AXIS_DRAG_X = (By.CSS_SELECTOR, 'div#restrictedX')
    AXIS_DRAG_Y = (By.CSS_SELECTOR, 'div#restrictedY')
