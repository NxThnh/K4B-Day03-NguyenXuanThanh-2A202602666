"""
📚 [REFERENCE ONLY / CODE MẪU THAM KHẢO]
🧠 CẤP ĐỘ 3: NATIVE MCP AGENT (Native Tool Calling + MCP Server Integration)
⚠️ Lưu ý: File này chỉ dùng để đọc tham khảo kiến trúc. Không chỉnh sửa hay debug file này.
"""

import json

def get_weather(city: str) -> str:
    return f"Thời tiết {city}: 28°C, Nắng nhẹ."

def run_level3_demo():
    print("=== DEMO CẤP ĐỘ 3: NATIVE MCP AGENT ===")
    user_goal = "Tra cứu ca lỗi gán nhãn 2D QC-2D-014"
    print(f"🎯 Goal: {user_goal}")
    print("🧠 [Thought]: Phát sinh Native Tool Call 'query_defect_case'...")
    print("🛠️ [Native Tool Call]: query_defect_case({'defect_code': 'QC-2D-014'})")
    print("👁️ [MCP Server Observation]: {'status': 'SUCCESS', 'defect_code': 'QC-2D-014', 'severity': 'Cao'}")
    print("🏁 [Final Answer]: Ca lỗi QC-2D-014 là lỗi nhãn 2D mức độ cao và cần Rework.")

if __name__ == "__main__":
    run_level3_demo()
