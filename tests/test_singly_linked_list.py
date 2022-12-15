import copy
from unittest import TestCase, mock

from data_structures.linked_lists.singly_linked_list import LinkedList


class TestSinglyLinkedList(TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()
        self.sample_data = [1, 10, 3, 8, 12, 9, 4, 15, 24]

    def append_items(self, items=None):
        if items is None:
            items = self.sample_data
        for number in items:
            self.linked_list.append(number)

    def prepend_items(self):
        for number in self.sample_data:
            self.linked_list.prepend(number)

    @mock.patch('builtins.print')
    def assert_valid_print(self, items, mock_print):
        self.linked_list.print_list()
        mock_print.assert_called_with(
            " ".join(map(str, items))
        )

    def test_append_empty_linked_list(self):
        self.assertIsNone(self.linked_list.head)
        self.linked_list.append(15)
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(self.linked_list.head.data, 15)
        self.assertIsNone(self.linked_list.head.next)

    def test_append(self):
        self.append_items()
        self.assert_valid_print(self.sample_data)

    def test_prepend_empty_linked_list(self):
        self.assertIsNone(self.linked_list.head)
        self.linked_list.prepend(15)
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(self.linked_list.head.data, 15)
        self.assertIsNone(self.linked_list.head.next)

    def test_prepend(self):
        self.prepend_items()
        self.assert_valid_print(self.sample_data[::-1])

    def test_delete_by_value_not_exists(self):
        self.append_items()
        self.linked_list.delete_by_value(2)
        self.assert_valid_print(self.sample_data)

    def test_delete_by_value_head(self):
        self.append_items()
        self.linked_list.delete_by_value(self.sample_data[0])
        self.assert_valid_print(self.sample_data[1:])

    def test_delete_by_value(self):
        self.append_items()
        self.linked_list.delete_by_value(self.sample_data[3])
        sample_data = copy.copy(self.sample_data)
        sample_data.remove(self.sample_data[3])
        self.assert_valid_print(sample_data)

    def test_delete_at_pos(self):
        self.append_items()
        self.linked_list.delete_at_pos(3)
        sample_data = copy.copy(self.sample_data)
        sample_data.remove(self.sample_data[3])
        self.assert_valid_print(sample_data)

    def test_delete_at_pos_head(self):
        self.append_items()
        self.linked_list.delete_at_pos(0)
        self.assert_valid_print(self.sample_data[1:])

    @mock.patch('builtins.print')
    def test_delete_at_pos_out_of_range(self, mock_print):
        self.append_items()
        self.linked_list.delete_at_pos(len(self.sample_data))
        mock_print.assert_called_with("There is no node at this position")

    def test_length(self):
        self.append_items()
        self.assertEqual(len(self.sample_data), self.linked_list.length())

    def test_swap_nodes_not_exits(self):
        self.append_items()
        self.assertIsNone(self.linked_list.swap_nodes(12, 100))

    def test_swap_nodes(self):
        self.append_items()
        key1, key2 = 10, 12
        list_after_swap = copy.copy(self.sample_data)
        ind1, ind2 = self.sample_data.index(key1), self.sample_data.index(key2)
        list_after_swap[ind1] = self.sample_data[ind2]
        list_after_swap[ind2] = self.sample_data[ind1]
        self.linked_list.swap_nodes(key1, key2)
        self.assert_valid_print(list_after_swap)

    def test_reverse(self):
        self.append_items()
        self.linked_list.reverse()
        self.assert_valid_print(reversed(self.sample_data))

    def test_rotate(self):
        self.append_items()
        ind = 4
        self.linked_list.rotate(ind)
        self.linked_list.print_list()
        rotated = self.sample_data[ind:] + self.sample_data[:ind]
        self.assert_valid_print(rotated)

    def test_merge_sort(self):
        data1 = list(sorted(self.sample_data))
        self.append_items(data1)
        data2 = [3, 4, 5, 8, 13]
        list2 = LinkedList()
        for item in data2:
            list2.append(item)
        self.linked_list.merge_sorted(list2)
        self.assert_valid_print(sorted(data1 + data2))

    def test_remove_duplicates(self):
        data = copy.copy(self.sample_data)
        data.append(data[0])
        self.append_items(data)
        self.linked_list.remove_duplicates()
        self.assert_valid_print(self.sample_data)

    def test_get_nth_from_last(self):
        self.append_items()
        n = 5
        nth_item = self.linked_list.get_nth_from_last(n)
        self.assertEqual(nth_item, self.sample_data[-n])

    def test_count_occurrences(self):
        self.append_items()
        num = 5
        counted = self.linked_list.count_occurrences(num)
        self.assertEqual(counted, self.sample_data.count(num))

    def test_is_palindrome_false(self):
        self.append_items()
        self.assertFalse(self.linked_list.is_palindrome())

    def test_is_palindrome_true(self):
        data = copy.copy(self.sample_data)
        data.extend(self.sample_data[::-1])
        self.append_items(data)
        self.assertTrue(self.linked_list.is_palindrome())

    def test_move_tail_to_head(self):
        self.append_items()
        self.linked_list.move_tail_to_head()
        self.linked_list.print_list()
        data = [self.sample_data[-1]] + self.sample_data[:-1]
        self.assert_valid_print(data)
