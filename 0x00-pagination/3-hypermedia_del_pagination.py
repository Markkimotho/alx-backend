#!/usr/bin/env python3
"""Module for Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with hypermedia
        pagination information based on the index and page size.
        """
        indexed_dataset = self.indexed_dataset()
        dataset_size = len(indexed_dataset)

        if index is None:
            index = 0
        else:
            assert 0 <= index < dataset_size, "Index is out of range."

        data = []
        next_index = index

        while len(data) < page_size and next_index < dataset_size:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index if next_index < dataset_size else None
        }

    def delete_item(self, index: int):
        """
        Delete an item from the indexed dataset.
        """
        if index in self.__indexed_dataset:
            del self.__indexed_dataset[index]
            self.__indexed_dataset = {
                i: self.__indexed_dataset[i] for i in range(
                                             len(self.__indexed_dataset))
            }
