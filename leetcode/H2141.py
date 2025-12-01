n = 10
batteries = [108,36,400,51,463,126,53,357,718,915,37,526,533,846,122,356,773,118,462,425,213,288,293,166,490,93,604,283,667,356,33,978,894,481,675,492,242,395,24,985,795,401,640,246,116,787,50,484,422,315,860,583,493,948,811,331,959,676,596,763,869,240,527,336,89,467,330,21,136,13,482,348,436,134,901,419,242,151,879,717,798,386,599,839,18,136,490,66,329,127,988,420,803,82,579,99,305,551,766,669,799,137,313,897,946,27,75,989,300,468,358,435,996,617,248,565,477,580,323,800,365,88,621,775,849,619,421,482,670,722,363,649,598,913,122,567,524,339,391]

class Solution:
    def maxRunTime(self, n, batteries) -> int:
        batteries.sort()

        def check_time_runnable(n, batteries, time_check):
            time_left = time_check
            puters_run = 0
            for battery in batteries:
                if time_left > battery:
                    time_left -= battery
                elif time_left == battery:
                    puters_run += 1
                    time_left = time_check
                else:
                    puters_run += 1
                    time_left = max(time_left, time_check - (battery - time_left))
            
                if puters_run >= n:
                    return True

            return False
        
        best_possible = (len(batteries)//n+1)*max(batteries)

        min_max = [0, best_possible]

        while min_max[1] > min_max[0]:
            check = (min_max[0] + min_max[1] + 1)//2
            print(f"Currently checking {min_max}, test index {check}")
            if check_time_runnable(n, batteries, check):
                min_max[0] = check
            else:
                min_max[1] = check - 1
        
        return min_max[0]


print(Solution.maxRunTime(Solution, n, batteries))
        