
for i in range(1,51):
    with open(f'{i}주차.txt', "w", encoding="utf8") as report_file:
        report_file.write(f'-{i}주차 주간 보고')
        report_file.write(f'부서 : {부서}')
        report_file.write(f'이름 : {이름}')
        report_file.write(f'업무 요약 : {업무}')