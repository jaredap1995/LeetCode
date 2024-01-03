def findContentChildren(g, s):
        g.sort()
        s.sort()

        g_idx = 0
        s_idx = 0

        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] > s[s_idx]:
                  s_idx += 1
            else: 
                  g_idx += 1
                  s_idx += 1
                  
        return g_idx


g=[1,2,3]
s=[1,1]
print(findContentChildren(g,s))