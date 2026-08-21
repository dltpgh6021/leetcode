# 0003. Longest Substring Without Repeating Characters

* **Difficulty:** Medium
* **Problem:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Problem Summary

주어진 문자열에서 중복되는 문자가 포함되지 않은 가장 긴 연속된 부분 문자열(Substring)의 길이를 구하는 문제입니다.

---

## Approach

### Solution 1. Sliding Window + Hash Set

#### Idea

부분 문자열을 직접 잘라내어 검사하는 대신, `left`와 `right` 두 개의 포인터를 사용해 가상의 창문(Window)을 만들고 문자열을 훑고 지나갑니다. 중복 여부를 빠르게 확인하기 위해 탐색 속도가 빠른 `Set`을 활용합니다.

#### Algorithm

1. 중복 문자를 추적할 집합(`Set`)과 시작점을 가리킬 `left` 포인터, 최대 길이를 저장할 변수를 초기화합니다.
2. `right` 포인터를 한 칸씩 이동시키며 현재 문자가 집합에 있는지 확인합니다.
3. 중복된 문자가 발견되면, 중복이 해소될 때까지 `left` 포인터가 가리키는 문자를 집합에서 지우고 `left`를 오른쪽으로 이동시킵니다.
4. 중복이 없으면 현재 문자를 집합에 추가하고, 현재 창문의 길이(`right - left + 1`)로 최대 길이를 갱신합니다.

#### Complexity

* **Time Complexity:** `O(N)` (각 문자는 `right`와 `left` 포인터에 의해 최대 두 번씩만 방문되므로 문자열 길이에 비례합니다.)
* **Space Complexity:** `O(M)` (`M`은 문자열에 등장하는 고유한 문자의 개수로, 알파벳/기호의 개수만큼 Set에 공간이 필요합니다.)

---

### Solution 2. Sliding Window + Hash Map (최적화)

#### Idea

Set을 사용하는 방식은 `left`를 한 칸씩 이동시켜야 하므로 낭비가 발생할 수 있습니다. 각 문자의 '마지막으로 등장한 인덱스'를 Dictionary에 저장해 두면, 중복 발견 시 `left` 포인터를 중복 문자의 바로 다음 위치로 단번에 점프시킬 수 있어 더 효율적입니다.

#### Algorithm

1. 각 문자의 가장 최근 인덱스를 저장할 딕셔너리(`Dictionary`)와 `left` 포인터를 초기화합니다.
2. 문자열을 순회(`right`)하면서, 현재 문자가 이미 딕셔너리에 있고 그 위치가 현재 `left`보다 크거나 같다면 중복이 발생한 것입니다.
3. 중복이 발생했다면, `left` 포인터를 이전에 등장했던 중복 문자의 위치 다음 칸(`dictionary[char] + 1`)으로 한 번에 이동시킵니다.
4. 현재 문자의 위치를 딕셔너리에 업데이트하고 최대 길이를 갱신합니다.

#### Complexity

* **Time Complexity:** `O(N)` (`left`를 반복해서 이동시킬 필요 없이 `right`만 한 번 순회하므로 더 빠릅니다.)
* **Space Complexity:** `O(M)` (고유 문자의 개수만큼 딕셔너리 공간이 필요합니다.)

---

## Learned

* **파이썬 내장 함수의 비용 인지:** 문자열 슬라이싱(`s[left:right]`)이나 리스트 내 탐색(`in`)은 내부적으로 `O(N)`의 시간이 소모되므로 중첩 루프 안에서는 사용을 피해야 합니다.
* **빠른 탐색을 위한 자료구조 선택:** 요소의 '존재 여부(중복)'를 확인할 때는 `List` 대신 탐색 시간이 `O(1)`인 `Set`이나 `Dictionary`를 사용하는 습관을 들여야 합니다.
* **연속된 구간 문제의 치트키:** '가장 긴 연속된 부분 문자열/배열'을 구하는 문제는 일차적으로 슬라이딩 윈도우(Sliding Window)와 **투 포인터(Two Pointers)** 접근법을 떠올려야 합니다.
* **억지스러운 인덱스 조정 피하기:** `IndexError`를 막기 위해 코드 중간에 작위적인 인덱스 덧셈/뺄셈이 들어간다면, 루프 설계 자체를 다시 점검해 보는 것이 좋습니다.

---

## Tags

`String` `Hash Table` `Sliding Window` `Two Pointers`