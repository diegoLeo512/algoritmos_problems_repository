#include <iostream>
#include <vector>

double findMedianSortedArrays(std::vector<double> &nums1, std::vector<double> &nums2);

int main(int argc, char* argv[]) {
    if (argc < 4) {
        std::cerr << "Usage: " << argv[0] << " n m nums1_elem1 nums1_elem2 ... nums1_elemN nums2_elem1 nums2_elem2 ... nums2_elemM" << std::endl;
        return 1;
    }

    int n = std::atoi(argv[1]);
    int m = std::atoi(argv[2]);

    if (argc != 3 + n + m) {
        std::cerr << "Invalid number of arguments." << std::endl;
        return 1;
    }

    std::vector<double> nums1(n);
    std::vector<double> nums2(m);

    for (int i = 0; i < n; ++i) {
        nums1[i] = std::atof(argv[3 + i]);
    }

    for (int i = 0; i < m; ++i) {
        nums2[i] = std::atof(argv[3 + n + i]);
    }

 
    std::cout << "Median: " << findMedianSortedArrays(nums1, nums2) << std::endl;

    return 0;
}



double findMedianSortedArrays(std::vector<double> &nums1, std::vector<double> &nums2)
{

    std::vector<int> merged_arr;
    int i = 0;
    int j = 0;

    while (i < nums1.size() || j < nums2.size())
    {
        if (i < nums1.size() && j < nums2.size())
        {
            if (nums1[i] < nums2[j])
            {
                merged_arr.push_back(nums1[i]);
                i++;
            }
            else
            {
                merged_arr.push_back(nums2[j]);
                j++;
            }
        }
        else if (i >= nums1.size() && j < nums2.size())
        {
            merged_arr.push_back(nums2[j]);
            j++;
        }
        else
        {
            merged_arr.push_back(nums1[i]);
            i++;
        }
    }

    if (merged_arr.size() % 2 == 1)
    {
        return static_cast<double>(merged_arr[merged_arr.size() / 2]);
    }
    else
    {
        int mid = merged_arr.size() / 2;
        return static_cast<double>(merged_arr[mid - 1] + merged_arr[mid]) / 2.0;
    }
}
