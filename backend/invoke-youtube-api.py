from googleapiclient.discovery import build
import dotenv
import os

dotenv.load_dotenv()

# API 키 및 YouTube 비디오 ID 설정
api_key = os.environ["API_KEY"]  # 여기에 생성한 API 키를 입력하세요.
video_id = "-f750TSucjM"  # watch?v= 뒤에 있는 문자열

# YouTube API 클라이언트 생성
youtube = build("youtube", "v3", developerKey=api_key)

# 댓글과 댓글당 좋아요 수 가져오기
comments = []
likes_per_comment = []
request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=100,  # 모든 댓글 불러오기
    textFormat="plainText",
)

while request:
    response = request.execute()
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        likes = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
        comments.append(comment)
        likes_per_comment.append(likes)
    request = youtube.commentThreads().list_next(request, response)

# 결과 출력
for comment, likes in zip(comments, likes_per_comment):
    print(f"댓글: {comment}, 좋아요 수: {likes}")

print(len(comments))
