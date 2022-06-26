## Sorting

# Most Common sorting algorithms
* Bubble sort
* Selection sort
* Insersion sort
* Merge sort
* Quick sort
* Heap sort
* Radix sort

# Stable vs Unstable Algorithms
Stable sorting algorithms preserve the relative order of equal elements, while unstable sorting algorithms don't. In other words, stable sorting maintains the position of two equals elements relative to one another.

# Which sort is best?
 Insertion sort when really small data size, or  values are alreadt almost sorted
 Bubble sort - pretty much never
 selection sort - pretty much never
 Merge sort - We are guaranteed to use this so long as space complexity is not a problem, we are     also guranteed to remain in O(nlogn)
 Quicksort - best sorting algorithm only if we are guaranteed a decent pivot worst case O(n^2) on a bad pivot


# Can we beart O(n log n)?
 its mathematically impossible to beat this time complexity. You can however, improve this should we not have to compare inputs

 * these are called non-comparison sort
 such as counting sort and radix sort - these are only valid to work with integers ina  small range

 # Interview questions - determining which sorting algorithm to use
* #1 - Sort 10 schools around your house by distance: insertion

* #2 - eBay sorts listings by the current Bid amount: quicksort or radiz or counting sort

* #3 - Sport scores on ESPN: quicksort

* #4 - Massive database (can't fit all into memory) needs to sort through past year's user data: Merge sort

* #5 - Almost sorted Udemy review data needs to update and add 2 new reviews: insertion sort

* #6 - Temperature Records for the past 50 years in Canada: radix count or counting sort or quick sort

* #7 - Large user name database needs to be sorted. Data is very random: quick sort

* #8 - You want to teach sorting for the first time: bubble sort, selection sort