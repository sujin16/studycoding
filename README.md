
# 코딩 테스트 & 알고리즘 공부


## JAVA 자료구조
``` java
//1.Stack
Stack<Integer>s = new Stack<>();
s.push(3);
s.push(1);
while(!s.empty()){
  s.pop();
}
```
``` java
//2.Queue
Queue<Integer>q = new Queue<>();
q.offer(3);
q.offer(3);
while(!q.isEmpty()){
  s.poll();
}
```
CollectionFrameWork url : https://joooootopia.tistory.com/13


### 그리디 알고리즘(2021.2.25 ~)


그리디 알고리즘은 최적의 해를 보장할 수 없다.<br>
현재 상황에서 최적의 방법을 고르는 것을 의미한다.가장 좋아 보이는 것을 계속 선택해도 최적의
해를 구할 수 있는지를 검토 한다. 

- 1이 될 때까지 &nbsp;&nbsp;[greedy_1.py](https://github.com/sujin16/studycoding/blob/main/code/greedy_1.py)
- 곱하기 혹은 더하기 &nbsp;&nbsp;[multi_add.py](https://github.com/sujin16/studycoding/blob/main/code/multi_or_add.py)
- 모험가 길드 &nbsp;&nbsp;[trip_guild.py](https://github.com/sujin16/studycoding/blob/main/code/trip_guild.py)


### 구현(2021.2.25 ~)

- 상하좌우 &nbsp;&nbsp; [RLUD.py](https://github.com/sujin16/studycoding/blob/main/code/RLUD.py) &nbsp; [RLUD.java](https://github.com/sujin16/studycoding/blob/main/code/RLUD.java)
- 시각 ** &nbsp;&nbsp; [Time.java](https://github.com/sujin16/studycoding/blob/main/code/Time.java)
- 왕실의 나이트  &nbsp;&nbsp;[king_night.py](https://github.com/sujin16/studycoding/blob/main/code/king_night.py) &nbsp;&nbsp; [King.java](https://github.com/sujin16/studycoding/blob/main/code/King.java)
- 문자열 재정렬 &nbsp;&nbsp;[ReSort.java](https://github.com/sujin16/studycoding/blob/main/code/ReSort.java)



### 그래프 탐색 알고리즘 : DFS , BFS (2021.2.26 ~)

DFS(깊이우선탐색)
1. 탐색 시작 노드를 스택에 삽입하고 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 더  이상 2. 과정을 수행할 수 없을 때 까지 반복

Code : [DFS.Java](https://github.com/ndb796/python-for-coding-test/blob/master/5/8.java) &nbsp; &nbsp; [DFS.py](https://github.com/ndb796/python-for-coding-test/blob/master/5/8.py)

BFS(너비우선탐색) : 가까운 노드를 우선적으로 방문 !! 
1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다
2. 큐에소 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중 방문하지 않은 노드를 큐에 삽입하고 방문 처리
3. 더 이상 2. 이 과정이 수행할 수 없을 때까지 반복

Code : [BFS.java](https://github.com/ndb796/python-for-coding-test/blob/master/5/9.java) &nbsp; &nbsp; [BFS.py](https://github.com/ndb796/python-for-coding-test/blob/master/5/9.py)

-음료수 얼려 먹기 


Dijstra Algorithm

Shortest Path 찾기




