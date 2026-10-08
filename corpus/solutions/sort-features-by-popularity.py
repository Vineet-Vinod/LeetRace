class Solution:
    def sortFeatures(self, features: list[str], responses: list[str]) -> list[str]:
        popularity = Counter()
        feature_set = set(features)
        for response in responses:
            popularity.update(set(response.split()) & feature_set)
        return sorted(features, key=lambda feature: -popularity[feature])
