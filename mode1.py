from island import Island
from data_structures.bst import BinarySearchTree, BSTInOrderIterator, BSTPreOrderIterator, BSTPostOrderIterator

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.islands = islands
        self.crew = crew
        
    def _sort_islands_with_ratio_inorder_iterator(self) -> BinarySearchTree:
        island_ratio_bst = BinarySearchTree()
        
        for i in self.islands:
            ratio = i.marines / i.money
            
            island_ratio_bst[ratio] = Island(i.name, i.money, i.marines)
            
        in_order_iterator = BSTInOrderIterator(island_ratio_bst.root)
        return in_order_iterator
        

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        temp_crew = self.crew
        islands = []
        
        for i in self._sort_islands_with_ratio_inorder_iterator():
            island = i.item
            marines = island.marines
            
            if temp_crew >= marines:
                islands.append((Island(island.name, island.money, island.marines), marines))
                temp_crew -= marines
                
            elif temp_crew < marines:
                if temp_crew > 0:
                    islands.append((Island(island.name, island.money, island.marines), temp_crew))
                    temp_crew -= temp_crew
                else:
                    islands.append((Island(island.name, island.money, island.marines), 0))
                
        return islands

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        list_of_money = []
        for crews in crew_numbers:
            temp_crew = self.crew
            self.crew = crews
            
            selected = self.select_islands()
            self.crew = temp_crew
            
            current_money = 0
            for island, crews_selected in selected:
                current_money += min(island.money * crews_selected / island.marines, island.money)
                
            list_of_money.append(current_money)
                
        return list_of_money

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        for i in self.islands:
            if i.name == island.name:
                i.money = new_money
                i.marines = new_marines
                break