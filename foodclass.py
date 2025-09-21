import heapq

class FoodRatings:
    def _init_(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        """
        Initialize food rating system.
        foods[i] belongs to cuisines[i] and has initial rating ratings[i].
        """
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_to_heap:
                self.cuisine_to_heap[c] = []
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        """
        Change rating of the given food to newRating.
        """
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        """
        Return the highest rated food for the given cuisine.
        If multiple, return lexicographically smallest.
        """
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
        return ""


# Example test
if _name_ == "_main_":
    foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
    cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
    ratings = [9, 12, 8, 15, 14, 7]
    fr = FoodRatings(foods, cuisines, ratings)

    print(fr.highestRated("japanese"))  # "ramen"
    fr.changeRating("sushi", 16)
    print(fr.highestRated("japanese"))  # "sushi"