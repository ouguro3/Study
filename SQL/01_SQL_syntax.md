## SQL 문법

SQL은 크게 다음과 같은 형태로 사용된다
___
- SELECT 칼럼, 계산값
- FROM 테이블 명
- WHERE 조건
- GROUP BY 그룹화
- HAVING 그룹화에 사용되는 조건
___
### 1. SELECT
#### 1-1) 필요한 칼럼만 호출
```SQL
SELECT 호출하려는 칼럼명
FROM DB 명.테이블 명;
```  

예) classicmodels.customers의 customerNumber를 조회
```SQL
SELECT customerNumber
FROM classicmodels.customers; 
```
#### 1-2) 모든 결과 조회  

`*`연산자 사용 
```SQL
SELECT *
FROM DB 명.테이블 명;
```
#### 1-3) 여러개의 칼럼 출력

칼럼 명에 `,` 추가
```SQL
SELECT 칼럼 명 1, 칼럼 명 2,
FROM DB 명.테이블 명;
```

#### 1-4) 칼럼 명 변경

`AS` 사용 
```SQL
SELECT 칼럼 명 as 변경 칼럼 명
FROM DB 명. 테이블 명;
```
**칼럼 뒤에 `AS`를 입력하지 않아도 변수명을 변경할 수 있다**  

예)
```SQL
SELECT ProductCode N_productCode
FROM classicmodels.product;
```
#### 1-5) 중복 제외  
`DISTINCT`를 사용하면 중복을 제외하고 데이터를 조회할 수 있다
```SQL
SELECT DISTINCT 칼럼 명
FROM DB 명.테이블 명;
```
### 2. FROM
우리가 사용하는 데이터는 보통 데이터베이스에 여러가지 테이블로 나누어져 보관되어 있다   
`예) 매출 데이터 : sales,  상품 데이터 : product`  

이때 sales 테이블에 있는 정보를 호출하는 명령어는 다음과 같다 
```SQL
SELECT 계산식 또는 칼럼 명
FROM DB 명.SALES;
``` 
DB 명은 sales 테이블이 생성된 데이터베이스 명이다  
테이블이 어떤 데이터베이스에 저장되어 있는지 기재해 주어야 이를 인지한다  
매번 DB 명을 입력하는 것이 번거롭다면 USE 구문을 사용해 해결할 수 있다  
```SQL
USE DB 명;

SELECT 계산식 또는 칼럼 명
FROM SALES;

```
### 3. WHERE
select ~ from 명령어에 where 구문을 추가해 조건에 맞는 데이터만 출력할 수 있다  
```SQL
SELECT 계산식 또는 칼럼 명
FROM DB 명.테이블 명 
WHERE 조건;
```
#### 3-1) 조건의 범위 지정

`BETWEEN`을 사용하면 조건의 범위를 지정해줄 수 있다  
```SQL
SELECT *
FROM DB 명.테이블 명
WHERE 칼럼 BETWEEN 시작점 AND 끝점;
```
#### 3-2) 대소 관계 표현
대소 관계는 연산자를 이용해 지정할 수 있다  

|연산자|설명|  
|:---:|---|  
|`=`| 동일하다|
|`>`|초과|
|`<`|미만|
|`>=`|이상|
|`<=`|이하|
|`<>`|같지않다|  

#### 3-3) IN 연산자  
특정 값을 포함한 데이터만 출력할 수 있다  
`,`를 사용해 여러개 가능
```SQL
SELECT 칼럼 명
FROM DB 명.테이블 명
WHERE 칼럼 명 IN (특정 값);
```
#### 3-4) NOT IN 연산자  
특정 값들을 제외하고 결과를 출력할 수 있다
```SQL
SELECT 컬럼 명
FROM DB 명.테이블 명
WHERE 칼럼 명 NOT IN (제외할 값);
```  
#### 3-5) 결측치
데이터를 수집하다 보면 결측치가 생성된다  
특정 값이 결측치인 데이터를 출력할 수 있다
```SQL
SELECT 칼럼 명 또는 계산식
FROM DB 명.테이블 명
WHERE 칼럼 IS NULL;
```
반대로 NULL 값이 아닌 것만 출력하고 싶다면 IS NOT NULL
```SQL
SELECT 칼럼 명 또는 계산식
FROM DB 명.테이블 명
WHERE 칼럼 IS NOT NULL;
```

#### 3-6) LIKE '%TEXT%'
특정 필드에 어떤 텍스트가 포함되어 있는 데이터를 출력할 수 있다  
```SQL
SELECT 칼럼 명
FROM DB 명.테이블 명
WHERE 칼럼 LIKE '%특정 텍스트%';
```
```SQL
# 예) 주소 칼럼에서 부산이라는 텍스트가 포함된 데이터를 모두 조회
SELECT *
FROM DB 명.테이블 명
WHERE 주소 LIKE '%부산%';
```
### 4. GROUP BY
칼럼의 값들을 그룹화해 각 값들의 평균, 개수 등을 구할 때 사용한다  
GROUP BY 는 보통 집계 함수와 함께 사용된다
```SQL
SELECT 칼럼 명 또는 계산식
FROM DB 명.테이블 명
GRUOP BY 그룹화 할 칼럼
```
```SQL
# 예) 제조 국가별, 제조사별 평균 자동차 가격 구하기
SELECT 제조 국가, 제조사명, AVG(가격)
FROM DB 명.테이블 명
GROUP BY 제조 국가, 제조사명
```
GRUOP BY 와 자주 사용되는 집계 함수 3가지  

|함수|의미|
|:----:|:----:|
|AVG()|평균|
|COUNT()|개수 구하기|
|SUM()|합계|

### 5. JOIN
여러가지 테이블로 나뉜 정보를 조합 하려면 테이블 결합 함수를 사용한다
#### 5-1) LEFT JOIN
특정 테이블 정보를 기준으로 타 테이블을 결합
```SQL
SELECT *
FROM TABLE_A
LEFT JOIN TABLE_B
ON TABLE_A.컬럼 = TABLE_B.컬럼 
```
ON 에는 어떤 키값으로 데이터를 결합할지 입력한다  
LEFT JOIN은 FROM 절에 테이블을 기준으로 매칭되는 정보를 호출한다  
TABLE A의 정보는 모두 출력되나 TABLE B는 TABLE A에 존재하는 정보만 결합된다  
그외의 정보는 없는것으로 처리되어 NULL 값이 된다
#### 5-2) INNER JOIN
두가지 테이블에 공통으로 존재하는 정보만 출력된다  
```SQL
SELECT *
FROM TABLE_A
INNER JOIN TABLE_B
ON TABLE_A.칼럼 = TABLE_B.칼럼
```
#### 5-3) FULL JOIN
FULL JOIN은 TABLE_A 또는 TABLE_B와 매칭되는 정보를 모두 출력한다  
그러니까 FULL JOIN의 값은 매우 커질 수 있다  
```SQL
SELECT *
FROM TABLE_A
FULL JOIN TABLE_B
ON TABLE_A.칼럼 = TABLE_B.칼럼
```
#### 6. CASE WHEN
조건에 따른 값을 다르게 출력할 때 사용한다  
(if문을 떠올리면 된다)
```SQL
SELECT 
CASE WHEN 조건 1 THEN 결과 1
CASE WHEN 조건 2 THEM 결과 2
ELSE 결과 3 END
FROM DB 명.테이블 명;
```