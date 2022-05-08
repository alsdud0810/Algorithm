import sys
from itertools import combinations

n=int(input())
data = [list(map(int,input().split())) for _ in range(n)]
member = [i for i in range(n)]

team_combi=[]
# 스타트 팀의 n/2의 조합을 구한다.
for team in combinations(member,n//2):
    team_combi.append(team)

minn=987654321
for k in range(len(team_combi)//2):
    team_a=team_combi[k]
    # 스타트 팀의 여집합으로 링크 팀을 구한다.
    team_b=list(set(member)-set(team_combi[k]))

    # 각 팀의 능력치 합을 구한다.
    start_team=0
    for i in range(len(team_a)):
        for j in team_a:
            start_team+= data[team_a[i]][j]
    
    link_team=0
    for i in range(len(team_b)):
        for j in team_b:
            link_team+= data[team_b[i]][j]
    # 능력치 차 최소 구한다.
    minn=min(minn,abs(start_team - link_team))

print(minn)