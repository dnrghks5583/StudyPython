def solution(cacheSize, cities):
    
    if cacheSize == 0 :
        return len(cities) * 5

    answer = 0
    cache = []
    for city in cities :
        
        city = city.upper()
        if city in cache : # cache hit
            cache.remove(city)
            cache.append(city)
            answer += 1
            continue
        # cache miss
        if len(cache) < cacheSize : 
            cache.append(city)
        else :
            cache.remove(cache[0])
            cache.append(city)
        answer += 5
    return answer

if __name__ == '__main__' :
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(cacheSize, cities))