class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cntDomains = {}
        for cntDom in cpdomains:
            cnt, domain = cntDom.split()
            domain = domain.split(".")
            print(domain)
            for i in range(len(domain)):
                dom = ".".join(domain[i:])
                cntDomains[dom] = cntDomains.get(dom, 0) + int(cnt)
        
        res = []
        for domain, count in cntDomains.items():
            string = str(count) + " " + domain
            res.append(string)

        return res
                
