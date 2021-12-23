class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
def minus(self,t2):
        if self.s<t2.s:
            self.m-=1
            self.s+=60
        if self.m<t2.s:
            self.h-=1
            self.m+=60
        ht_res=self.h-t2.h
        mt_res=self.m-t2.m
        st_res=self.s-t2.s
        return ht_res,mt_res,st_res
        print(t1.minus(t2))