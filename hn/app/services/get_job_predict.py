from app.models.score import Score

class GetJobPredictService:

    def get_job_predict(self, input_score: Score) -> str:
        print(f"Received Score with id: {input_score.id}")
        return "builder"

get_job_predict_service = GetJobPredictService()
