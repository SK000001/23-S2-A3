from island import Island
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.n_pirates = n_pirates
        self.islands = []
        

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """
        for i in islands:
            self.islands.append(i)

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        pirate_score_heap = islands_from_score_heap(self.islands, crew)
        result = []
        
        for i in range(self.n_pirates):
            island = None
            
            if len(pirate_score_heap) > 0:
                score, island, crew_Sent, plundered = pirate_score_heap.get_max()
                
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
    pirate_score_heap = MaxHeap(len(islands))

    for i in islands:
        plundered = min(i.money, i.money * crew / i.marines)
            
        crew_sent = min(crew, i.marines)
        
        score = 2 * (crew - crew_sent) + plundered
        
        pirate_score_heap.add((score, i, crew_sent, plundered))
        
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
    
    nav = Mode2Navigator(3)
    nav.add_islands(islands)
    
    nav.simulate_day(100)
    
    nav.add_islands([Island("F", 900, 150)])
    
    nav.simulate_day(100)