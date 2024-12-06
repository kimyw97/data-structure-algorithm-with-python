totalAmount=34200;
countOfManWon = int(totalAmount/10000);
remains = totalAmount % 10000;
print('{0}중 만원짜리는 {1}개이고 그 외 금액은 {2}입니다.'.format(totalAmount, countOfManWon, remains))

#이등변 삼각형 넓이 구하기
width, height = input('밑변과 높이를 입력해주세요.').split();
print('넓이는 %f입니다.'%(int(width)*int(height)/2));

#자동판매기
insertAmount = input('동전을 넣어주세요');
cost = input('가격을 입력해주세요');
change = int(insertAmount) - int(cost);
change500 = change // 500
change100 = (change - change500 * 500) // 100
print('잔돈은 100원 {0}개 500원 {1}개입니다'.format(int(change100),int(change500)))

#성적처리
krGrade = input('국어 점수');
enGrade = input('영어 점수');
mtGrade = input('수학 점수')
print('과목별 성적')
print('===============================')
print('국어: {0} 영어: {1} 수학: {2}'.format(krGrade, enGrade, mtGrade))
print('===============================')
print('총점: %d' %(int(krGrade)+ int(enGrade) + int(mtGrade)))
print('평균: %d' %((int(krGrade)+ int(enGrade) + int(mtGrade))/3))

