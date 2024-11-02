import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost

def main():
    cables = [4, 3, 2, 6]
    result = min_connection_cost(cables)
    print(f"The minimum total connection cost is: {result}")

if __name__ == "__main__":
    main()
