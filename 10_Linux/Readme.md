# 리눅스와 기본 명령어 알아보기

1. 맥북에 리눅스 환경 설치 진행 (UTM , Ubuntu 설치)
   
2. 리눅스 사용법
   - CommandNames 들은 쉘의 검색 PATH 안에 있어야 한다.
   - 쉘은 터미널을 통해 명령이 제출될 때 명령의 의미를 해석하는 것.
   - Linux 명령은 CommandName -options input 의 구조를 따른다.
   - 일부 명령에는 긴 형식과 짧은 형식 옵션이 있을 수 있다. (ex --universal)
   - 짧은 형식 옵션에는 대시 1개(-)가 있고 긴 형식 옵션에는 대시 2개(--)가 있습니다.

![image](https://github.com/BE02LEEJAEHOON/oz_class/assets/155046462/a9c67d7b-5c06-4a15-a287-2e57f54dc072)


[] -> 선택사항
<> -> 필수사항
... -> 반복 할 수 있음
| -> 둘 중 하나만 사용

ex)
which [-a] <SOMETHING>
which [-a | -f] <SOMETHING>
which [-a | -f] filename ...


3. cat 명령어
   - cat 명령은 파일(들)을 순서대로 읽고 그 내용을 읽은 순서대로 표준 출력(standard output)에 쓰이는 명령
  

4. Input과 Output 내용 정리
   - Standard Output, Standard Input, Standard Error는 표준 데이터 스트림이다.
   - Standard Output, Standard Error은 기본 적으로 Terminal에 연결되어 있다.
   - Standard Input Data Stream은 기본적으로 키보드에 연결되어 있다.

  
5. Redirect Standard Output
   - cat 1> output.txt (1 생략 가능)
   - cat 1>> output.txt (>을 2개 넣을 경우 내용이 바뀌는게 아닌 추가가 된다)
  

6. Redirect Standard Error, Input
   - cat 2>> error.txt
   - 읽기는 0< 으로 시작
  

7. Piping
   - 파이핑은 한 명령의 표준 출력을 다른 명령의 표준 입력에 연결하는 것이다.
   - 대부분의 키보드에서 SHIFT + BACKSLASH(\)를 눌러 엑세스할 수 있는 파이프 문자(|)를 사용하여 파이프 한다.
   -  ex) date | cut --delimiter ' ' --fields 1 > today.txt
   -  ex) date | cut > today.txt --delimiter ' ' --fields 1
      (둘다 똑같은 명령어.. 순서만 다를 뿐!)
  

8. Tee 명령어
   - T자 형태처럼??
   - ex) date | tee date.txt | cut --delimiter ' ' --fields 1 ( 또는 뒤에 필드 부분은 --field=1 으로도 가능 단수복수 차이)
   - 만약 하단 명령어를 타이핑 한다면 전체 데이터를 출력하는 date.txt가 만들어지고, 요일 부분만 짜른 today.txt가 만들어진다.
     date | tee date.txt | cut delimiter ' ' --field=1 > today.txt


9. xargs 명령어
   - xargs 유틸리티를 사용하여 표준 입력에서 명령을 작성하고 실행할 수 있다. 일반적으로 pipe를 통해 다른 명령과 함께 사용된다.
   - xargs는 빈칸이나 새 줄로 구분된 표준 입력에서 인수를 읽고 명령의 인수로 입력을 사용하여 지정된 명령을 실행한다. 명령이 제공되지 않을 경우 기본값은 /bin/echo이다.
   - ex) date | xargs echo 'Hello World'


10. Aliases (별칭)
   - 별칭을 사용하면 파이프라인과 명령을 기억하기 쉬운 별명으로 저장하여 나중에 훨씬 쉽게 사용 할 수 있다.
   - 홈 디렉터리의 .bash_aliases 파일에서 별칭을 정의한다. 존재하지 않는 경우 표시된 대로 정확하게 철자를 작성해야한다. 앞에 마침표(.)가 포함되어야 하며 파일 확장자(ex: .txt  .pdf)가 없어야 한다.
   - ex) alias getdates='date | teee /home~~~~~~ 변수 선언이랑 비슷한듯??ㅎㅎ;




# 리눅스 명령어로 파일 관리하기

1. File System 기본
   - 예를 들어, ls -F 명령어 실행 시 리스트 옆에 /가 붙으면 폴더형식이라는 걸 알 수 있다. (파일 형식은 슬래쉬가 붙지 않는다)
   -  ls -l 실행 시, 리스트 목록 앞에 drwxr 이라고 되어 있는데 여기서 rwx는 (d = directory / r = read / w = write / x = execute) 의 약자이다
   -  ![image](https://github.com/BE02LEEJAEHOON/oz_class/assets/155046462/28c018e6-1fd0-4628-b7c6-6293c699ca16)
   -  ![image](https://github.com/BE02LEEJAEHOON/oz_class/assets/155046462/3ed29b5b-91d0-4a59-9b0f-2c06c73c050f)
  

2. cd 명령어
   - Linux파일 시스템은 슬래시(/)로 표시된 기본(또는 루트) 디렉토리에서 시작하는 트리형 구조를 따른다. 파일 시스템의 위치는 파일 경로를 사용하여 표시된다.
   - 기본 디렉토리(/)에서 시작하는 경로를 절대 경로라고 한다. shell의 현재 작업 디렉토리에서 시작하는 경로를 상대 경로라고 한다.
   - 예를 들어, 이 두 예제 모두 zidol 이라는 사용자의 문서 폴더에 있는 'file1.txt'라는 파일을 참조한다. 상대 경로는 shell이 zidol의 홈 디렉토리에 있다고 가정한다.
     절대 경로 : /home/zidol/Documents/file1.txt
     상대 경로 : Documents/file1.txt
     
   ##cd 란? => change directory (경로변경)
         * cd /   최상위 디렉토리(루트 디렉토리) 이동
         * cd ~   홈 디렉토리로 이동
         * cd -   이전 경로로 이동
         * cd ..  상위 디렉토리로 이동


3. File Extension
   - 리눅스는 확장자에 대해서 그리 중요하지 않다..? 리눅스는 헤더 부분을 읽기 때문에 상관이 없다..? (ex jpg -> png 바꾸거나 txt -> pdf 를 바꿔도 신경쓰지 않는다..?)



4. Wild Card
   - 리눅스에서 와일드 카드란 file명 혹은 directory 이름을 패턴의 형식으로 출력하게 만들어주는 아주 유용한 명령어다.
   - 정규식은 텍스트를 일치시키는데 사용할 수 있는 패턴이다. Linux에서는 사용자가 명령을 실행 하려는 파일에 대해 다소 일반적인 표현을 만들 수 있도록 하는데 사용된다.
     파일 이름과 일치하는 정규식을 만드는 것을 글로빙(globbing)이라고 한다. 정규식 패턴은 와일드카드라는 특수 구성요소를 사용하여 만들 수 있다.
     와일드카드는 Shell 에 대한 특정 의미를 갖는 기호이다. 아래에는 가장 일반적인 3가지 유형의 와일드카드다.

            * : 일치 되는 모든 "문자열"을 찾아주는 명령어 (길이에 관계없이 무엇이든 일치한다)
               // ls 예시
     
               $ ls * // 현재 디렉토리에 있는 모든 파일 list 출력
               $ ls *.c // 현재 디렉토리에 있는 .c 파일 list 출력
               $ ls ma* // ma으로 시작하는 현재 디렉토리에 있는 모든 파일 출력
               $ ls *aba* // aba가 들어있는 현재 디렉토리에 있는 모든 파일 출력
​

            ? : 일치 되는 모든 "문자"를 찾아주는 명령어 , ? 에 들어갈 수 있는 패턴을 설정해주면 ?에 들어갈 문자를 알지 못하더라도 원하는 내용을 출력하거나 삭제할 수 있음 (무엇이든 일치하지만 한 장소에만 해당된다)
               // ls 예시
               // 현재 디렉토리에 존재하는 파일 : main.c happy.txt a1 a2 a3
               
               $ ls m???.c // main.c 출력
               $ ls a? // a1 a2 a3 출력 
               $ ls ?? // a1 a2 a3 출력
               $ ls ?app?.t?t // happy.txt 출력
               ​

         [ ] : 대괄호 안에 있는 caracter들의 패턴에 일치하는 것을 찾아주는 명령어 (한 장소에 대해서만 내부 옵션과 일치한다)
               [ ] 안에  숫자의 패턴을 넣고싶다면 [ 1 - 9 ] 를 넣게 되면 그에 맞게 찾아줌
               [ ab ] 이렇게 설정하게 되면, a와 b로 시작하는 것을 찾아줌
                // ls 예시
               // 현재 디렉토리에 존재하는 파일 : main.c happy.txt a1 a2 a3 a4
               
               $ ls [a]* // a1 a2 a3 a4 출력
               $ ls [a][1-4] // a1 a2 a3 a4 출력
               $ ls [mh]* // main.c happy.txt 출력 
               // *[mh] 할 경우에는 m과 h가 들어가 있는 것을 모두 출력해줌
               $ ls *[2-4] // a2 a3 a4


      **깜짝 퀴즈**
      .txt로 끝나는 홈 디렉토리의 모든 파일을 나열하는 명령어는? (~는 '홈 디렉토리'를 의미한다)
         정답 : ls ~/*.txt

 

5. touch, mkdir 명령어
   - touch : 영어 뜻대로 손본다? 살짝 수정한다 이런느낌대로 파일의 날짜를 수정하는 명령어인데 , 옵션없이 그냥 파일명만 지을 경우 "빈 파일"을 만드는 명령어기도 해서 빈 파일을 만들 때도 쓰이는 명령어다.
             형식은 touch [옵션] [파일] 이고 옵션없이 사용하면 그냥 빈 파일을 만든다.

   - mkdir (make directory) : 영어 뜻대로 디렉토리를 만드는 명령어다. 명령어 형식은 mkdir [옵션] [파일이름....] 이며, 절대위치를 적지 않으면 현재 위치에 디렉토리를 만든다.

   *쉽게 이해하려면 touch는 파일은 만들 때 사용하고, mkdir은 폴더를 만들 때 사용된다고 보면 될듯..?
