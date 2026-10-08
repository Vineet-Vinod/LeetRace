class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        eligible = [
            restaurant
            for restaurant in restaurants
            if (not veganFriendly or restaurant[2] == 1)
            and restaurant[3] <= maxPrice
            and restaurant[4] <= maxDistance
        ]
        eligible.sort(key=lambda restaurant: (-restaurant[1], -restaurant[0]))
        return [restaurant[0] for restaurant in eligible]
