#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        date_arr = date.split(" ")
        res = ""
        month_dict = {
            "Jan" : "01",     
            "Feb" : "02",     
            "Mar" : "03",     
            "Apr" : "04",     
            "May" : "05",     
            "Jun" : "06",     
            "Jul" : "07",     
            "Aug" : "08",     
            "Sep" : "09",     
            "Oct" : "10",     
            "Nov" : "11",     
            "Dec" : "12",     
        }
        for i, n in enumerate(date_arr):
            if i == 0:
                num = date_arr[i][:-2]
                if int(num) < 10:
                    res += "0" + num
                    print(res)
                else:
                    res += num
            elif i == 1:
                month = date_arr[i]
                res = month_dict[month] + "-" + res
            else:
                res = date_arr[i] + "-" + res 
        return res





# @lc code=end





