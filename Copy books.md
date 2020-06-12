## Description
Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.

## Method1: Binary search
What is the range of time spent by copiers?
[max(pages), sum(pages)].
So we look for an integer that lies in this range and satisfies the condition where the number of copiers is not greater than k.
```Python
    def copyBooks(self, pages, k):
        if not pages:
            return 0
        left = max(pages)
        right = sum(pages)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.getNumOfCopiers(pages, mid) > k:
                left = mid 
            else:
                right = mid 
        print(left, right)
        if self.getNumOfCopiers(pages, left) <= k:
            return left 
        return right 

    def getNumOfCopiers(self, pages, time):
        copier = 0
        lastCopied = float("inf")
        for i in range(len(pages)):
            if pages[i] > time:
                return float("inf")
            if pages[i] + lastCopied > time:
                copier += 1 
                lastCopied = pages[i]
            else:
                lastCopied += pages[i]
        return copier

```


