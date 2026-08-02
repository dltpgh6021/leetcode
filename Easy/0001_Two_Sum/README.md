# 0001. Two Sum

* **Difficulty:** Easy
* **Problem:** https://leetcode.com/problems/two-sum/

## Problem Summary

정수 배열 `nums`와 정수 `target`이 주어질 때, 합이 `target`이 되는 두 원소의 인덱스를 반환한다.

조건

* 정답은 하나만 존재한다.
* 같은 원소를 두 번 사용할 수 없다.

---

## Approach

### Solution 1. Brute Force

모든 원소 쌍을 확인하여 합이 `target`인지 검사한다.

### Algorithm

1. 첫 번째 원소를 선택한다.
2. 그 이후의 모든 원소와 합을 계산한다.
3. 합이 `target`이면 두 인덱스를 반환한다.

### Complexity

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

---

### Solution 2. Hash Map (Optimal)

현재 숫자를 순회하면서 필요한 값(`target - nums[i]`)이 이미 등장했는지 해시맵에서 확인한다.

없다면 현재 숫자와 인덱스를 해시맵에 저장한다.

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

## Learned

* Brute Force는 구현은 간단하지만 시간 복잡도가 크다.
* `unordered_map`을 이용하면 탐색을 `O(1)`에 수행할 수 있어 전체 시간 복잡도를 `O(n)`으로 줄일 수 있다.
* LeetCode에서는 입출력을 직접 구현하지 않고, `Solution` 클래스의 함수만 작성하여 제출한다.

---

## Tags

`Array` `Hash Table`
