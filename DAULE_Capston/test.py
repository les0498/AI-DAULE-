# 다른 프로젝트에서 파일을 읽어 결과 사용하는 코드
emotion = "emotion_result.txt"  # 표정 인식 결과가 저장된 파일명

with open(emotion, "r", encoding="utf-8") as EMO:
    EMO = EMO.read()

# result 변수에는 파일에서 읽어온 결과가 저장됨
print("\n사용자 표정 결과:", EMO)