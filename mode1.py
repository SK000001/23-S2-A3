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
        
        self.island_ratio_bst = islands_from_ratio_bst(self.islands)

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        temp_crew = self.crew
        islands = []
        
        for i in BSTInOrderIterator(self.island_ratio_bst.root):
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
            
        self.island_ratio_bst = islands_from_ratio_bst(self.islands)
        
def islands_from_ratio_bst(islands) -> BinarySearchTree:
        island_ratio_bst = BinarySearchTree()
        copy_island = [Island(i.name, i.money, i.marines) for i in islands]
        
        for i in copy_island:
            ratio = i.marines / i.money
            
            island_ratio_bst[ratio] = Island(i.name, i.money, i.marines)
            
        return island_ratio_bst
    
if __name__ == "__main__":
    a = Island("A", 400, 100)
    b = Island("B", 300, 150)
    c = Island("C", 100, 5)
    d = Island("D", 350, 90)
    e = Island("E", 300, 100)
    islands = [
        a, b, c, d, e
    ]
    
    nav = Mode1Navigator(islands, 500)
    selected = nav.select_islands()
    
    print(nav.select_islands_from_crew_numbers([0, 200, 500, 300, 40]))
    
    # for i, j in selected:
    #     print(i.name, j)