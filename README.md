
# 코딩 테스트 & 알고리즘 공부



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

-음료수 얼려 먹기 ** 


-미로찾기 ** 




### 정렬 알고리즘 : 선택, 삽입,퀵, 계수 (2021.03.01 ~)

- 두 배열의 원소 교체



### 이진 탐색 알고리즘 (2021.03.01 ~)
순차 탐색 : 앞에서부터 데이터를 하나씩 확인하는 방법
이진 탐색: 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색 하는 방법

- 파라메트릭 서치 : 최적화 문제를 결정문제(예 ,아니요)로 바꾸어 해결하는 기법
- 떡볶이 떡 만들기 [binary_search.py](https://github.com/sujin16/studycoding/blob/main/code/binary_search.py) &nbsp; &nbsp;&nbsp; &nbsp;[binarySearch1.java](https://github.com/sujin16/studycoding/blob/main/code/binarySearch1.java)
- 정렬된 배열에서 특정 수의 개수 구하기 [binary_search2.py](
https://github.com/sujin16/studycoding/blob/main/code/binary_search2.py) &nbsp; &nbsp;&nbsp; &nbsp;[binarySearch2.java](https://github.com/sujin16/studycoding/blob/main/code/binarySearch2.java)




### 다이나믹 프로그래밍 (2021.2.27 ~3.2 ~ ) 

메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상 시키는 방법
이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산 하지 않도록 한다

작은 문제의 답을 모아서 문제를 풀 때, 동일한 작은 문제를 반복적으로 해결할 때 사용

#### 메모이제이션 : 한번 계산한 결과를 메모리 공간에 메모하는 기법 
- 개미 전사
- 1로 만들기
- 효율적인 화폐 구성
- 금광
- 병사 [dynamic5.java](https://github.com/sujin16/studycoding/tree/main/code/dynamic5.java)&nbsp; &nbsp;&nbsp; &nbsp; [dynamic5.py](https://github.com/sujin16/studycoding/tree/main/code/dynamic5.py)





### 최단경로 알고리즘 (2021.3.2 ~ ) 

다익스트라 : 음의 간선이 없을 때, 특정한 노드에서 출발하여 다른 모든 노드를 가는 최단경로. 그리드 알고리즘으로 분류. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택



플로이드 워셜 : 모든 노드에서 다른 노드 까지의 최단 경로를 모두 계산. 2차원 테이블에 최단 거리 정보를 저장. 간선의 정보가 적을 때 사용.각 단계마다 특정한 노드 k 를 거쳐 가는 경우를 확인 







