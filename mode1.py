from island import Island
from data_structures.bst import BinarySearchTree, BSTInOrderIterator

class Mode1Navigator:
    """
    Creates a navigator that selects islands to plunder based on the ratio of marines to money. wont change islands as rutheless pirates plunder them.
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        :Initialises the Mode1Navigator.
        :param: islands(list of Island object), crew(int).
        
        :return: None
        
        :Time Complexity: O(NlogN), where N is the number of islands.
        """
        self.islands = islands  # O(1)
        self.crew = crew    # O(1)
        
        self.island_ratio_bst = islands_from_ratio_bst(self.islands) # O(NlogN), N being number of islands

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        :Selects Islands to plunder.
        
        :return: A list of tuples of the form (Island, int) where the int is the number of marines sent to the island.
        
        :Time Complexity: O(NlogN), where N is the number of islands.
        """
        temp_crew = self.crew
        islands = []
        
        # traversing the island_ratio_bst in order
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
        :Calculates the most money you can make with different crew configurations.
        :param: crew_numbers(list of int) - A list of crew configurations.
        
        :Return: A list of floats, where each float is the most money you can make with the corresponding crew configuration.
        
        :Time Complexity: Best case is O(1) when the crew_numbers is empty. Worst case is O(NlogN), where N is the number of islands.
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
        :Updates the money and marines of an island.
        :param: island(Island object) - island to be updated, new_money(float) - new island money, new_marines(int) - new island marines.
        
        :Return: None
        
        :Time Complexity: Best Case is O(1)+O(NlogN) when island is found at start. Worst case is O(N)+O(NlogN) ( where N is the number of islands ) when island is found at the end.
        """
        for i in self.islands:
            if i.name == island.name:
                i.money = new_money
                i.marines = new_marines
                break
            
        self.island_ratio_bst = islands_from_ratio_bst(self.islands)
        
def islands_from_ratio_bst(islands) -> BinarySearchTree:
    """
    :Creates a BinarySearchTree of islands with the ratio of marines to money as the key.
    :param: islands(list of Island objects).
    
    :Return: A BinarySearchTree of islands with the ratio of marines to money as the key.
    
    :Time Complexity: Worst/Best is O(NlogN), where N is the number of islands.
    """
    
    island_ratio_bst = BinarySearchTree()
    copy_island = [Island(i.name, i.money, i.marines) for i in islands]
    
    for i in copy_island:
        ratio = i.marines / i.money
        
        island_ratio_bst[ratio] = Island(i.name, i.money, i.marines)
        
    return island_ratio_bst
    
if __name__ == "__main__":
    a = Island("A", 300, 100)
    b = Island("B", 100, 50)
    c = Island("C", 20, 5)
    d = Island("D", 200, 60)
    e = Island("E", 500, 2000)
    islands = [
        a, b, c, d, e
    ]
    
    nav = Mode1Navigator(islands, 500)
    selected = nav.select_islands()
    
    print(nav.select_islands_from_crew_numbers([0, 200, 500, 300, 40]))
    
    for i, j in selected:
        print(i.name, j)