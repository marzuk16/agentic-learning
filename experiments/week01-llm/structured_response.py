from pathlib import Path

from openai import OpenAI
from pydantic import ValidationError

from schema import ReviewResponse

MAX_RETRIES = 3

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="none",
)

BASE_DIR = Path(__file__).resolve().parent
java_code = (BASE_DIR / "Sample.java").read_text(encoding="utf-8")

def build_prompt(code: str) -> str:
    return f"""
Review the following Java code.

Return ONLY valid JSON.

JSON Schema:

{{
    "summary": "",
    "bugs": [],
    "improvements": []
}}

Java Code:

{code}
"""


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="mlx-community/Qwen3-8B-4bit",
        temperature=0,
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    print(f"Finish Reason : {response.choices[0].finish_reason}")
    print(f"Token Usage   : {response.usage}")

    return response.choices[0].message.content


def parse_review(json_response: str) -> ReviewResponse:
    return ReviewResponse.model_validate_json(json_response)


def main() -> None:
    prompt = build_prompt(java_code)

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n========== Attempt {attempt} ==========\n")

        try:
            json_response = call_llm(prompt)

            print("Raw Response:\n")
            print(json_response)

            review = parse_review(json_response)

            print("\nValidation Successful ✅\n")

            print("Summary")
            print("-" * 40)
            print(review.summary)

            print("\nBugs")
            print("-" * 40)
            for bug in review.bugs:
                print(f"• {bug}")

            print("\nImprovements")
            print("-" * 40)
            for improvement in review.improvements:
                print(f"• {improvement}")

            break

        except ValidationError as e:
            print("\n❌ JSON Validation Failed")
            print(e)

        except Exception as e:
            print("\n❌ Unexpected Error")
            print(e)

    else:
        print("\nFailed after maximum retry attempts.")


if __name__ == "__main__":
    main()