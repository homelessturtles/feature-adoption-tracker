from openai import OpenAI
import streamlit as st

openai_api_key = st.secrets["OPENAI_KEY"]
client = OpenAI(api_key=openai_api_key)

def summarize_usage(usage_stats) -> str:
    """
    Sends feature usage summary to GPT and returns a natural language report.
    """
    usage_str = "\n".join(f"{feature}: {count}" for feature, count in usage_stats.items())

    prompt = f"""
    You are a product analyst. Given the following feature usage counts, write a short report
    highlighting the most used features, any underused ones, and insights a product manager
    might care about. Keep it concise and clear.

    Feature Usage:
    {usage_str}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful product analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error generating summary: {e}"
