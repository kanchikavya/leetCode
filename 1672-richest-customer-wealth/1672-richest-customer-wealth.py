class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m_max = 0
        for i in range(len(accounts)):
            s_sum=0
            for j in range(len(accounts[i])):
                # if(accounts[j]> accounts[j+1 - 1]):
                    # return accounts[j]

                s_sum +=accounts[i][j]
            if(s_sum > m_max):
                m_max = s_sum
                
        return m_max

        