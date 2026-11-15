# Deadline tracker v1: print my assignments

assignments = [
     "11/15 기말과제 발표자료",
    "11/15 기말과제 발표 동영상",
    "11/17 10주차 과제",
    "11/17 11주차과제_matlab코드 파이썬프로그램 변환",
    "11/27 레포트",
    "11/28 소년이 온다 독후감",
]

print("My assignments:")
for assignment in assignments:
    print("-", assignment)

print("Total", len(assignments))