class Solution:
    def maximumTime(self, time: str) -> str:
        arr=list(time)
        if(arr[0]=="?" and arr[1]=='?'):
            arr[0]="2"
            arr[1]="3"
        if(arr[0]=="?"):
            if(arr[1]=="0" or arr[1]=="1" or arr[1]=="2" or arr[1]=="3"):
                arr[0]="2"
            else:
                arr[0]="1"
        if(arr[1]=="?"):
            if(arr[0]=="2"):
                arr[1]="3"
            else:
                arr[1]="9"
        if(arr[3]=="?"):
            arr[3]="5"
        if(arr[4]=="?"):
            arr[4]="9"
        str1 = ""

        # traverse in the string
        for ele in arr:
            str1 += ele
        return str1