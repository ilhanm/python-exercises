#challenge
#içerisinde sayılar olan 2 dosyanın ortak sayılarını barındıran liste
def getListOfNumbers(filepath: str)->list:
    with open(filepath,"r") as openfile:
        nums1=openfile.readlines()    
    return [int(num) for num in nums1]
nums1,nums2=getListOfNumbers("numbers1.txt"), getListOfNumbers("numbers2.txt")
commonNumbers=[num for num in set(nums1) if num in nums2]
file1Difference=[num for num in set(nums1) if num not in nums2]
print(commonNumbers)
print(file1Difference)

