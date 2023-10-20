from island import Island
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    :Creates a navigator that selects islands to plunder based on the score of each island. but changes islands as rutheless pirates plunder them.
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Initialises Mode2Navigator.
        
        :return: None
        
        :Time Complexity: O(1)
        """
        self.n_pirates = n_pirates
        self.islands = []
        

    def add_islands(self, islands: list[Island]):
        """
        Adds islands to the instance variable self.islands.
        
        :return: None
        
        :Time Complexity: Best case O(1) when there are no islands to add. Worst Case O(N) (where N is the number of islands) when N number of islands are to be added.
        """
        for i in islands:
            self.islands.append(i) # O(1)+O(1)+....+O(N)

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        :Simulates a day of plundering.
        
        :param: crew(int) - The number of pirates available for plundering.
        
        :return: A list of tuples of the form (Island, int) where the int is the number of marines sent to the island.
        
        :Time Complexity: Best Case O(1) when there are no islands to plunder. Worst Case O(NlogN) + O(M) * O(logN), where N is the number of islands and M is the number of crews.
        """
        pirate_score_heap = islands_from_score_heap(self.islands, crew) # O(NlogN)
        result = []
        
        for i in range(self.n_pirates): # O(M)
            island = None
            
            if len(pirate_score_heap) > 0:
                score, island, crew_Sent, plundered = pirate_score_heap.get_max()  # sink? O(logN)
                
                if island.money - plundered <= 0:
                    self.islands.remove(island)
                else:
                    island.marines = max(0, island.marines-crew_Sent)
                    island.money -= plundered
                    pirate_score_heap = islands_from_score_heap(self.islands, crew)
                    
                
            if island == None:
                result.append((None, 0))
                continue
                
            result.append((island, crew_Sent))

        return result
                
                
def islands_from_score_heap(islands, crew) -> MaxHeap:
    """
    :Creates MaxHeap of islands based on the score of each island.
    
    :param: islands(list of Island objects), crew(int).
    
    :Time Complexity: Best/Worst complexity is O(NlogN), where N is the number of islands.
    
    :return: MaxHeap of islands based on the score of each island.
    """
    pirate_score_heap = MaxHeap(len(islands))

    for island in islands:
        plundered = min(island.money, island.money * crew / island.marines)
            
        crew_sent = min(crew, island.marines)
        
        score = 2 * (crew - crew_sent) + plundered
        
        pirate_score_heap.add((score, island, crew_sent, plundered))
        
    return pirate_score_heap        


if __name__ == "__main__":
    a = Island("A", 400, 100)
    b = Island("B", 300, 150)
    c = Island("C", 100, 5)
    d = Island("D", 350, 90)
    e = Island("E", 300, 100)
    islands = [
        a, b, c, d, e
    ]
    
    nav = Mode2Navigator(10)
    nav.add_islands(islands)
    
    nav.simulate_day(100)
    
    nav.add_islands([Island("F", 900, 150)])
    
    nav.simulate_day(100)