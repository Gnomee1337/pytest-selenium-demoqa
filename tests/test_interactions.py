import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite("Interactions")
class TestInteractions:
    @allure.feature("Sortable Page")
    class TestSortablePage:
        @allure.title("Check sortable")
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_result = sortable_page.change_sortable_order('list')
            grid_result = sortable_page.change_sortable_order('grid')
            assert list_result[0] != list_result[1], 'List order doesnt changed'
            assert grid_result[0] != grid_result[1], 'Grid order doesnt changed'

    @allure.feature("Selectable Page")
    class TestSelectablePage:
        @allure.title("Check selectable")
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            list_item_selected = selectable_page.select_list_item()
            grid_item_selected = selectable_page.select_grid_item()
            assert len(list_item_selected) > 0, 'List item doesnt selected'
            assert len(grid_item_selected) > 0, 'Grid item doesnt selected'

    @allure.feature("Resizable Page")
    class TestResizablePage:
        @allure.title("Check resizable")
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            box_results = resizable_page.change_size_resizable_box()
            resize_results = resizable_page.change_size_resizable()
            assert ('500px', '300px') == box_results[0], 'Max size not equal to (500px, 300px)'
            assert ('150px', '150px') == box_results[1], 'Min size not equal to (150px, 150px)'
            assert resize_results[0] != resize_results[1], 'Resizable has not been changed'

    @allure.feature("Droppable Page")
    class TestDroppablePage:
        @allure.title("Check simple droppable")
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            simple_result = droppable_page.drop_simple()
            assert simple_result == 'Dropped!', "'Drag me' element has not been dropped"

        @allure.title("Check accept droppable")
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            accept_results = droppable_page.drop_accept()
            assert accept_results[0] == 'Drop here', "'Not Acceptable' element has been accepted"
            assert accept_results[1] == 'Dropped!', "'Acceptable' element has not been dropped"

        @allure.title("Check prevent propogation droppable")
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy_result, greedy_result = droppable_page.drop_prevent_propogation()
            assert not_greedy_result == ['Dropped!', 'Dropped!'], "'Not greedy' droppable has not been changed"
            assert greedy_result == ['Outer droppable', 'Dropped!'], "'Greedy' droppable has not been changed"

        @allure.title("Check revert draggable droppable")
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_results = droppable_page.drop_will_revert_draggable('will')
            will_not_results = droppable_page.drop_will_revert_draggable('will_not')
            assert will_results[0] != will_results[1], "'Will Revert' element has not been reverted"
            assert will_not_results[0] == will_not_results[1], "'Not Revert' element has been reverted"

    @allure.feature("Draggable Page")
    class TestDraggablePage:
        @allure.title("Check simple draggable")
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            axis_drag_result = draggable_page.axis_drag_me()
            print(axis_drag_result)
            assert axis_drag_result[0][0] != axis_drag_result[0][1], "'Only X' has not been moved"
            assert axis_drag_result[1][0] != axis_drag_result[1][1], "'Only Y' has not been moved"
