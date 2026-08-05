class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            L = arr[l:m+1]
            R = arr[m+1:r+1]

            ll, rr = 0, 0
            curr = l
            while ll < len(L) and rr < len(R):
                if L[ll] <= R[rr]:
                    arr[curr] = L[ll]
                    ll += 1
                else:
                    arr[curr] = R[rr]
                    rr += 1
                curr += 1

            while ll < len(L):
                arr[curr] = L[ll]
                ll += 1
                curr += 1

            while rr < len(R):
                arr[curr] = R[rr]
                rr += 1
                curr += 1

        def mergeSort(arr, l, r):
            if (r-l+1) <= 1:
                return

            m = (l+r) // 2

            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)

            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums)-1)
        return nums