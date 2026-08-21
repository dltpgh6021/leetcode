초기 작성하신 코드를 바탕으로 정리한 템플릿입니다. 이 내용을 먼저 Git에 올리시고, 나중에 슬라이딩 윈도우와 해시를 적용한 풀이(Solution 2)를 추가하면서 업데이트해 나가시면 훌륭한 공부 기록이 될 것입니다.

# 0003. Longest Substring Without Repeating Characters

* **Difficulty:** Medium
* **Problem:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Problem Summary

주어진 문자열에서 중복되는 문자가 포함되지 않은 가장 긴 연속된 부분 문자열(Substring)의 길이를 구하는 문제입니다.

---

## Approach

### Solution 1. Brute Force (완전 탐색)

#### Idea

가능한 모든 시작점(`left`)에 대해 끝점(`right`)을 하나씩 늘려가며 부분 문자열을 직접 잘라냅니다. 새로 추가할 문자가 잘라낸 부분 문자열 안에 존재하는지 매번 검사하여 가장 긴 길이를 찾습니다.

#### Algorithm

1. 문자열의 모든 인덱스를 시작점(`left`)으로 두고 순회합니다.
2. 시작점부터 시작하여 끝점(`right`)을 1씩 늘려가며 부분 문자열(`substr`)을 슬라이싱하여 만듭니다.
3. 바로 다음에 올 문자(`c`)가 현재 부분 문자열 안에 존재하는지 `in` 연산자를 통해 검사합니다. (이때 범위를 벗어나는 `IndexError`를 방지하기 위해 예외 처리를 합니다.)
4. 중복 문자가 발견되면 현재 부분 문자열의 길이를 최대 길이(`max_len`)와 비교하여 갱신하고, 탐색을 중지(`break`)한 뒤 다음 시작점(`left`)으로 넘어갑니다.

#### Complexity

* **Time Complexity:** `O(N^3)` (이중 루프 `O(N^2)` 안에서 문자열 슬라이싱과 `in` 연산으로 인해 추가적인 `O(N)`의 탐색이 발생하여 시간이 오래 걸립니다.)
* **Space Complexity:** `O(N)` (매 반복마다 `substr = s[left:right]`를 통해 새로운 문자열 객체를 메모리에 생성합니다.)

---

## Learned

* **파이썬 내장 함수의 비용 인지:** 문자열 슬라이싱(`s[left:right]`)이나 리스트 내 탐색(`in`)은 한 줄짜리 코드지만 내부적으로 `O(N)`의 시간이 소모됩니다. 중첩 루프 안에서는 사용을 주의해야 한다는 점을 배웠습니다.
* **빠른 탐색을 위한 자료구조의 필요성:** 원소의 '존재 여부(중복)'를 확인할 때는 매번 전체를 훑는 방식보다 탐색 시간이 `O(1)`인 `Set`이나 `Dictionary`를 사용하는 것이 효율적임을 인지하게 되었습니다.
* **연속된 구간 문제 접근법:** '가장 긴 연속된 부분 문자열'을 구할 때는 매번 처음부터 다시 검사하는 대신, **슬라이딩 윈도우(Sliding Window)** 기법을 통해 중복이 사라질 때까지 시작점만 옮겨가는 방식이 훨씬 효율적임을 알게 되었습니다.
* **인덱스 예외 처리 점검:** `IndexError`를 막기 위해 코드 중간에 조건문(`if right == l:`)을 넣기보다는, 루프의 범위(`range`)나 로직 자체를 개선하여 자연스럽게 예외를 방지하는 설계가 필요함을 배웠습니다.

---

## Tags

`String` `Brute Force`