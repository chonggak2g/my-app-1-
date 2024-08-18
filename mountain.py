# 탐방 코스 데이터를 딕셔너리 형태로 저장합니다.
courses = [
    {"name": "코스 A", "difficulty": "쉬움", "time": 1},
    {"name": "코스 B", "difficulty": "중간", "time": 2},
    {"name": "코스 C", "difficulty": "어려움", "time": 3},
    {"name": "코스 D", "difficulty": "쉬움", "time": 1.5},
    {"name": "코스 E", "difficulty": "중간", "time": 2.5},
]

def recommend_course(difficulty, max_time):
    recommended_courses = []
    for course in courses:
        if course["difficulty"] == difficulty and course["time"] <= max_time:
            recommended_courses.append(course["name"])

    return recommended_courses

def main():
    # 사용자에게 난이도와 소요 시간을 입력받습니다.
    difficulty = input("난이도를 입력하세요 (쉬움, 중간, 어려움): ")
    max_time = float(input("소요 시간을 입력하세요 (시간 단위): "))

    # 추천 코스를 찾습니다.
    recommendations = recommend_course(difficulty, max_time)

    # 추천 결과를 출력합니다.
    if recommendations:
        print("추천하는 탐방 코스:")
        for course in recommendations:
            print(course)
    else:
        print("조건에 맞는 탐방 코스가 없습니다.")

if __name__ == "__main__":
    main()