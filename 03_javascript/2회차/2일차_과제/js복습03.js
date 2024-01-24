// 4의 배수 5개씩 출력하기
let value = 100;
const endValue = 500;

while (value <= endValue) {
  let count = 1;
  let endCount = 5;

  let text = "";

  while (1 <= endCount) {
    text += " ";
    text += value;

    value += 4;
    count += 1;

    if (value > endValue) break;
  }

  console.log(text);
}